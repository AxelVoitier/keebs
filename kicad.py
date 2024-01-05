# Copyright (c) 2023 Axel Voitier
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words kicad altium geda pyparsing uncasted reexport keebs
# spell-checker:ignore sexpr descr alphanums subcls uvia mult tstamp Pcbplotparams
""""""
from __future__ import annotations

# System imports
import collections
import logging
import math
import re
import types
import typing
import uuid
from abc import abstractmethod
from contextlib import suppress
from copy import deepcopy
from enum import Enum
from numbers import Number
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    ClassVar,
    Iterator,
    Literal,
    Optional,
    Protocol,
    Self,
    runtime_checkable,
)

# Third-party imports
import attrs
import clyo
import pyparsing as pp
from attr import field, fields
from attrs import define
from rich import print

# Local imports

if TYPE_CHECKING:
    from typing import TypeAlias

    from ergogen import Keyboard

    SExpr: TypeAlias = str | Number | list['SExpr']

_logger = logging.getLogger(__name__)
kicad_cli = clyo.ClyoTyper(help='KiCAD-related commands')


class SParser:
    # Inspired by https://gist.github.com/hastern/ac2d7eab7a2a85f588d1
    _Open = pp.Suppress('(')
    _String = pp.QuotedString(quoteChar='"', unquoteResults=True)
    _Attribute = _String ^ pp.common.number ^ pp.Word(pp.alphanums + '_-.')
    _Close = pp.Suppress(')')
    _SExpr = pp.Forward()
    _SubSExpr = pp.Group(pp.ZeroOrMore(_SExpr | _Attribute))
    _SExpr << (_Open + _SubSExpr + _Close)

    @classmethod
    def parse(cls, content: str | Path, unquote: bool = True) -> SExpr:
        if isinstance(content, Path):
            content = content.read_text()

        if not unquote:
            cls._String.unquote_results = False

        result = cls._SExpr.parse_string(content).as_list()[0]

        if not unquote:
            cls._String.unquote_results = True

        return result

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        msg = 'SParser is not meant to be instantiated'
        raise NotImplementedError(msg)


# Need to have our own fence object for required fields since kicad file format
# has that weird thing of mixing optional fields followed by required ones.
# And that does not express well in Python/attrs world, since optional params/fields
# must always come after the required ones.
# Therefore, after declaring an optional field, attrs does not let us declare fields
# that don't have a default value. In such case, we use the following special
# object as default value
REQUIRED: Any = object


class Token:
    """Base class to model all kicad SExpr tokens.

    Provides all the tooling needed for parsing, converting, and serialising tokens.

    Note that actual token classes are expected to not only subclass this Token class.
    But also be attrs.define() wrapped, with fields to be parsed/serialised declared
    the way attrs declares fields.
    """

    #
    # Token name <-> class matching, and versioning section
    #

    __inheritors__: dict[type, dict[str, type[Self]]] = collections.defaultdict(dict)

    def __init_subclass__(cls, *args: Any, **kwargs: Any) -> None:
        """We keep track of all inheritors of Token in order to match their
        token name with corresponding class when we parse.
        """

        super().__init_subclass__(*args, **kwargs)

        our_name = cls.token_name(usage='parse')
        for base in cls.mro()[1:-1]:
            cls.__inheritors__[base][our_name] = cls

    @classmethod
    def token_name_to_class(cls, token_name: str) -> type[Self] | None:
        """Returns the token class corresponding to token_name"""
        return cls.__inheritors__[Token].get(token_name, None)

    @classmethod
    def token_name(cls, usage: Literal['parse', 'export']) -> str:
        """Returns the token name for this class.

        usage corresponds to whether this is used for parsing or export.
        The difference being that for export we need to remove the version suffix.
        Whereas for parsing we need to keep it to not confuse the parser later on.

        Subclasses can also reimplement it to implement different behaviours of
        token name when parsing or exporting.
        """

        name = cls._camel_to_snake(cls.__name__)
        if (usage == 'export') and cls._extract_version(name):
            name = name.rsplit('_', maxsplit=1)[0]
        return name

    @staticmethod
    def _camel_to_snake(name: str) -> str:
        """Converts a class name in Camel form into a snake form corresponding to
        the way token names are made."""

        # From https://stackoverflow.com/a/1176023
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    def _extract_version(name: str) -> int | None:
        """Token classes can have a _VERSION suffix used for versioning the
        various file formats kicad had."""

        with suppress(Exception):  # If it fails for any reason, we return None
            return int(name.rsplit('_', maxsplit=1)[-1])
        return None

    @classmethod
    def _get_versionned_token_class(cls) -> type[Token]:
        """Handles versionned tokens

        The logic is that versionned token classes have a date suffix in their name.
        We extract that suffix for each subclass of our current class (who should just
        be an empty class only used to fullfill token name matching).
        We build a list of candidate subclasses, and then pick the one that matches
        the current file version.
        """

        if (not Version.CURRENT) or not (subclasses := cls.__inheritors__[cls]):
            return cls

        candidates: dict[int, type[Self]] = {}
        for subcls_name, subcls in subclasses.items():
            if version := cls._extract_version(subcls_name):
                candidates[version] = subcls

        if not candidates:
            return cls

        current_version = Version.CURRENT.version
        for class_version in sorted(candidates, reverse=True):
            if class_version <= current_version:
                # print(f'New class for {current_version=} is {cls.__name__}')
                return candidates[class_version]

        msg = f'No version suitable for {cls.__name__} with {current_version=}'
        raise ValueError(msg)

    #
    # Fields helpers section
    #

    @staticmethod
    def _get_field_types(
        field: attrs.Attribute[Any],
    ) -> tuple[type[Any], tuple[type[Any], ...] | None]:
        """Determines proper field type.

        Takes care of interpreting Unions and Generics.
        """

        field_type = field.type
        field_type_args = None

        if isinstance(field_type, types.UnionType):
            # If it is a Union, keep only non-None type (assuming an optional is declared
            # with None at the end of the union list).
            field_type = typing.get_args(field_type)
            if field_type[-1] is type(None):
                field_type = field_type[:-1]
            if len(field_type) == 1:
                field_type = field_type[0]

        if isinstance(field_type, types.GenericAlias):
            # We cannot use generic types in isinstance/issubclass.
            # Therefore we need to extract their origin type, as well as argument type.
            field_type_args = typing.get_args(field_type)
            field_type = typing.get_origin(field_type)

        return field_type, field_type_args

    @staticmethod
    def _is_literal_field(field: attrs.Attribute[Any], field_type: type[Any]) -> bool:
        """Recognises a boolean field to be matched with a literal"""

        return issubclass(field_type, bool) and field.metadata.get('literal', False)

    @staticmethod
    def _match_literal_field(field: attrs.Attribute[Any], arg: Any) -> bool:
        """Matches an argument with a literal boolean field"""

        if not isinstance(arg, str):
            # Cannot even match if argument is not a string
            return False

        # Allows for other literal value than field name
        literal = field.metadata['literal']
        if isinstance(literal, bool):
            literal = field.name

        return arg == literal

    @staticmethod
    def _is_named_value(arg: Any, match_name: str) -> bool:
        """Recognises a case of uncasted "(name value)" simple S-Expression"""

        return isinstance(arg, list) and (len(arg) == 2) and (arg[0] == match_name)

    @staticmethod
    def _is_optional_field(field: attrs.Attribute[Any]) -> bool:
        """Recognises a field that is not required"""

        return field.default not in (attrs.NOTHING, REQUIRED)

    #
    # Token parsing section
    #

    @classmethod
    def from_sexpr(cls, sexpr: SExpr) -> Token | str | Number:
        """Takes the output from SParser and produces object representation of it."""

        # print('evaluating', sexpr)
        if isinstance(sexpr, (str, Number)):
            return sexpr

        token_name = sexpr[0]
        token_class = cls.token_name_to_class(token_name)
        if token_class is None:
            # If we don't have one, we resort to keeping it in list form.
            # Can be more intelligently used later (or just appended as raw data
            # in a dedicated token class member).
            token_class = list
            attributes = sexpr
        else:
            # Otherwise we strip out the token name itself from what needs to be
            # deeply/recursively parsed.
            attributes = sexpr[1:]

        # Deep convertion here:
        args: list[Self | str | Number] = [cls.from_sexpr(attribute) for attribute in attributes]

        # Actual object instantiation...
        # print('token is', token_name, token_class, args)
        if issubclass(token_class, list):
            return token_class(args)
        elif issubclass(token_class, Token):
            # ... except if it is a token class, in which case we deffer to the
            # (much more) complex from_sexpr_data().
            # This split allows subclasses to customise args before feeding them
            # back to Token.from_sexpr_data().
            return token_class.from_sexpr_data(args)
        else:
            return token_class(*args)

    @classmethod
    def from_sexpr_data(cls, args: list[Self | str | Number]) -> Token:
        """Given a list of args, re-interpret them following kicad ways of expressing
        token attributes to transform them into more precise kwargs and instantiate token objects.

        While it looks like we could just use that list of attributes as positional arguments
        to instantiate token objects, turns out that some peculiarities of kicad token attributes
        do not play well with the way Python and attrs match positional args to fields.

        This method handles:
        - Optional attributes appearing in the middle of required ones
        - Optional bool attributes that are just self-named flags
        - So-called named values, ie. (name value) sub-SExpr instead of being a plain value attrib

        It also handles grouping sequences of similarly typed tokens into list fields of a token
        class (eg. graphic items). Or grouping a bunch of (named) sub-SExpr into dict fields
        (eg. settings). These two constructs can also be used to lazily not model every possible
        token construct, and use them as catch-all fields in certain places.
        """
        # print(cls.__name__, f'{args=}')

        cls = cls._get_versionned_token_class()
        attrs.resolve_types(cls, include_extras=True)

        # To build the kwargs, we take each declared field, and try to match it
        # to 0, 1, or more positional args. To match, we rely on type hints.
        kwargs = {}
        for field in fields(cls):  # noqa: F402
            field: attrs.Attribute[Any]
            field_type, field_type_args = cls._get_field_types(field)

            # print(
            #     f'> {field.name}, {field.type}, {field_type}, {field_type_args}, '
            #     f'{field.default=}, {field.kw_only=}'  # , {args[0]}'
            # )
            # Process optionals
            if cls._is_optional_field(field):
                if not args:  # Not even any positional argument left, skip this field
                    continue

                if cls._is_literal_field(field, field_type):
                    # Case of literals that are just boolean True if present
                    if not cls._match_literal_field(field, args[0]):
                        continue  # Not matching => skip this field
                    args[0] = True

                elif cls._is_named_value(args[0], field.name):  # noqa: SIM114
                    pass  # Handled later

                # Optional lists and dicts handling
                elif not isinstance(field_type, tuple) and issubclass(field_type, (list, dict)):
                    pass  # Handled later

                # If type of this optional field does not match next positional arg, skip this field
                elif not isinstance(args[0], field_type):
                    continue

                # TODO: Handle case of kw_only field, which, by luck is no issue for the only cases
                # of optional kw_only field (title_block in kicad_pcb)

            if not isinstance(field_type, tuple):  # issubclass can't handle Union field type
                if issubclass(field_type, list):
                    # Case of a list[AToken] definition.
                    # We exhaust all of this AToken type in the positional args to fill the list.
                    list_ = []
                    i = 0
                    while i < len(args):
                        if not isinstance(args[i], field_type_args):
                            if field.kw_only:
                                i += 1
                            else:
                                break
                        else:
                            list_.append(args.pop(i))

                    kwargs[field.name] = list_
                    continue

                elif issubclass(field_type, dict):
                    # Case of a dict[str, Any] definition.
                    # We exhaust all positional args that are non-empty lists (must have a name)
                    # to fill the dict.
                    dict_ = {}
                    i = 0
                    while i < len(args):
                        if not (isinstance(args[i], list) and args[i]):
                            if field.kw_only:
                                i += 1
                            else:
                                break
                        else:
                            name, *value = args.pop(i)
                            if len(value) == 1:  # Pop-out the list container in simple cases
                                value = value[0]
                            dict_[name] = value

                    kwargs[field.name] = dict_
                    continue

            i = 0
            while i < len(args):
                if cls._is_named_value(args[i], field.name):
                    kwargs[field.name] = args.pop(i)[1]
                    break

                if isinstance(args[i], field_type):
                    kwargs[field.name] = args.pop(i)
                    break

                if field.kw_only:
                    i += 1
                else:
                    # Any other case, the next positional arg is our current field value
                    kwargs[field.name] = args.pop(i)
                    break

        # print(cls.__name__, f'{kwargs=}')

        if args:
            msg = f'Unprocessed args in {cls.__name__}: {args}'
            raise ValueError(msg)

        return cls(**kwargs)

    #
    # Convertions section
    #

    def to_version(self, version: int) -> Token:
        """Converts this token to a different version if possible.

        If we are not a versionned token, or we already are of that version, returns ourself.
        If the requested version is less than our current version, an error is raised
        (ie. not supporting downgrade).

        Tries to find and call converter methods on ourself, conventionally named "to_XXX",
        with XXX being the supported version. If that does not match the requested version but
        is still more recent than our own version, we first convert ourself to this
        intermediate version before recursively invoking to_version() on it.
        """

        our_version = self._extract_version(type(self).__name__)
        if (our_version is None) or (our_version == version):
            return self
        if our_version > version:
            msg = f'{type(self).__name__}: Cannot downgrade to version {version}'
            raise ValueError(msg)

        if to_version_fn := getattr(self, f'to_{version}', None):
            target_cls_name = f'{type(self).__name__.rsplit("_", maxsplit=1)[0]}_{version}'
            target_cls = globals()[target_cls_name]
            return to_version_fn(target_cls)

        # Need to search for an intermediate version to convert to
        for attr_name in dir(self):
            if (not attr_name.startswith('to_')) or (attr_name in ('to_version', 'to_footprint')):
                continue
            to_version = self._extract_version(attr_name)
            if to_version is None:
                continue
            to_version_fn = getattr(self, attr_name)
            if not callable(to_version_fn):
                continue

            target_cls_name = f'{type(self).__name__.rsplit("_", maxsplit=1)[0]}_{to_version}'
            target_cls = globals()[target_cls_name]
            if to_version == version:  # Would handle 0-padding
                return to_version_fn(target_cls)
            elif to_version < version:
                return to_version_fn(target_cls).to_version(version)
            else:
                continue

        msg = f'{type(self).__name__}: No suitable convertion path found to version {version}'
        raise ValueError(msg)

    def to_footprint(self) -> Token:
        """Converts ourself to our footprint variant.

        Assumes that it can be instanciated with the same fields.
        If not, subclasses are free to reimplement.
        """

        our_name = type(self).__name__
        if not our_name.startswith('Gr'):
            return self

        target_name = our_name.replace('Gr', 'Fp', 1)
        target_cls = globals()[target_name]
        return target_cls(**attrs.asdict(self, recurse=False))

    #
    # Token serialising section
    #

    if TYPE_CHECKING:
        # The iterator to_sexpr_elements() returns.
        _ToSExprIterator: TypeAlias = Iterator[
            tuple[
                attrs.Attribute[Any] | None,
                SExpr | '_ToSExprIterator',
            ]
        ]

    def to_sexpr_list(self) -> SExpr:
        """Deeply converts this token to SExpr list-form"""

        def walker(it: Token._ToSExprIterator) -> Iterator[SExpr]:
            """Walk-down a token-sexpr iterator as returned by to_sexpr_elements().

            Returns the SExpr elements as an iterator, that just needs to be wrapped
            in a list() to be joined."""

            for _, value in it:
                if isinstance(value, Iterator):
                    yield list(walker(value))
                elif value in ('', '\n'):
                    continue
                else:
                    yield value

        return list(walker(self.to_sexpr_elements()))

    def to_sexpr_text(self) -> str:
        """Deeply converts this token to SExpr text-form.

        Handles formatting such as indentation, float format and spaces between attributes,
        following metadata of token fields provided at their declaration.
        """

        indent = 0
        INDENT_BY = 2
        skip_space = False

        def float_to_str(value: float, field: attrs.Attribute[Any]) -> str:
            """Format a float value.

            Handles a precision level, as well as if we need to remove trailing zeros or not.
            """

            precision = field.metadata.get('precision', 6) if field else 6
            s = f'{value:.{precision}f}'
            strip_0 = field.metadata.get('strip_0', True) if field else True
            if strip_0:
                return s.rstrip('0.')
            else:
                return s

        def list_walker(field: attrs.Attribute[Any], value: list[SExpr]) -> Iterator[str]:
            """Walk-down a list. Returns an iterator of strings representing SExpr elements"""

            for item in value:
                if isinstance(item, list):
                    yield f'({joiner(list_walker(field, item))})'
                elif isinstance(item, float):
                    yield float_to_str(item, field)
                else:
                    yield str(item)

        def walker(it: Token._ToSExprIterator) -> Iterator[str]:
            """Walk-down a token-sexpr iterator as returned by to_sexpr_elements().

            Returns an iterator of strings representing SExpr elements."""

            nonlocal indent, skip_space
            indent += INDENT_BY

            for field, value in it:
                local_indent = 0
                if field:
                    if field.metadata.get('newline_before', False):
                        yield '\n'
                    if local_indent := field.metadata.get('indent', False):
                        if isinstance(local_indent, bool):
                            local_indent = INDENT_BY
                        indent += local_indent

                if isinstance(value, Iterator):
                    str_value = f'({joiner(walker(value))})'
                elif isinstance(value, list):
                    str_value = f'({joiner(list_walker(field, value))})'
                elif isinstance(value, float):
                    str_value = float_to_str(value, field)
                else:
                    str_value = str(value)

                if field:
                    skip_space = field.metadata.get('skip_space', False)
                yield str_value

                if local_indent:
                    indent -= local_indent

                if field and field.metadata.get('newline_after', False):
                    yield '\n'

            indent -= INDENT_BY
            yield None

        def joiner(it: Iterator[str]) -> str:
            """Takes an iterator from one of the walker functions, and handles joining,
            spacing, newlines, and indentation."""

            nonlocal skip_space
            s = ''
            had_newline = False
            for item in it:
                if had_newline:
                    s += ' ' * indent

                if item is not None:
                    is_newline = item == '\n'
                    if not is_newline and not had_newline and s and not skip_space:
                        s += ' '
                    skip_space = False
                    had_newline = is_newline
                    if is_newline:
                        s = s.rstrip(' ')
                    s += item
                else:
                    had_newline = False

            return s

        return f'({joiner(walker(self.to_sexpr_elements()))})\n'

    def to_sexpr_elements(self) -> _ToSExprIterator:
        """Iterates over the fields of this token, and yield tuples of (field, value).

        With field being the attrs.Attribute field object from the token attrs class
        declaration, meant to provide access to things like field name, type or metadata.
        It might also be None in some peculiar cases (eg. when yielding the token name,
        or a newline).

        And value being the actual element value. That value may be a raw value, or it can
        be enclosed in a list (eg. named values). If a string value needs to be quoted,
        it will be here.
        Additionally, value can also be another iterator, which means it recursed into
        another token object. Every time an iterator is encountered, serialisers functions
        calling to_sexpr_elements() have to enclose the elements this need iterator yield
        into a sub list or sub SExpr.

        Finally, due to constraints, some newlines (the ones declared in metadata of list
        and dict fields with newline_before_first and newline_after_last) will be yielded
        by to_sexpr_elements(). If your serialiser does not need them (eg. like in the case
        of to_sexpr_list() serialiser), you may freely ignore them.

        You may as well freely ignore an empty string value, as it might be generated by
        internal token declarations (such as _LayerDef for instance).
        """

        attrs.resolve_types(type(self), include_extras=True)
        yield None, self.token_name(usage='export')

        for field in fields(type(self)):
            field: attrs.Attribute[Any]
            field_type, field_type_args = self._get_field_types(field)
            value = getattr(self, field.name)

            if self._is_optional_field(field) and (
                (value is None) or not isinstance(value, field_type)
            ):
                # print(f'skipping {field.name} on {type(self).__name__}')
                continue

            if value is REQUIRED:
                msg = f'Field {field.name} of {type(self).__name__} is missing'
                raise ValueError(msg)

            if isinstance(field_type, tuple):
                for type_ in field_type:
                    if isinstance(value, type_):
                        field_type = type_
                        break
                else:
                    msg = f'Field {field.name} of {type(self).__name__} is not of correct type: {field_type}'
                    raise ValueError(msg)

            # print(
            #     '>',
            #     type(self).__name__,
            #     field.name,
            #     field.type,
            #     repr(field_type),
            #     field_type_args,
            #     type(value),
            #     value,
            # )

            if self._is_literal_field(field, field_type) and isinstance(value, bool):
                if not value:
                    continue

                literal = field.metadata['literal']
                if isinstance(literal, bool):
                    literal = field.name

                yield field, literal
                continue

            elif issubclass(field_type, str):
                if field.metadata.get('quoted', True):
                    value = f'"{value}"'
                if field.metadata.get('is_named', False):
                    value = [field.name, value]

                yield field, value
                continue

            elif issubclass(field_type, Number):
                if field.metadata.get('is_named', False):
                    value = [field.name, value]

                yield field, value
                continue

            elif issubclass(field_type, Enum):
                value = value.value
                if field.metadata.get('quoted', False):
                    value = f'"{value}"'
                if field.metadata.get('is_named', False):
                    value = [field.name, value]

                yield field, value
                continue

            elif issubclass(field_type, uuid.UUID):
                value = str(value)
                if field.metadata.get('quoted', False):
                    value = f'"{value}"'
                if field.metadata.get('is_named', True):
                    value = [field.name, value]

                yield field, value
                continue

            elif issubclass(field_type, Token):
                yield field, value.to_sexpr_elements()
                continue

            elif issubclass(field_type, list):
                if field.metadata.get('newline_before_first', False):
                    yield None, '\n'

                for item in value:
                    if isinstance(item, Token):
                        yield field, item.to_sexpr_elements()
                    else:
                        yield field, item

                if field.metadata.get('newline_after_last', False):
                    yield None, '\n'

                continue

            elif issubclass(field_type, dict):
                if field.metadata.get('newline_before_first', False):
                    yield None, '\n'

                for key, item in value.items():
                    if isinstance(item, list):
                        if not item:
                            if isinstance(key, str):
                                key = f'"{key}"'
                            yield field, key
                        else:
                            yield field, [key, *item]
                    else:
                        if isinstance(item, str) and not item:
                            item = '""'
                        yield field, [key, item]

                if field.metadata.get('newline_after_last', False):
                    yield None, '\n'

                continue


#
# Converters function usable in fields declarations
#


def str_to_bool(value: str | int | bool) -> bool:
    """Converts a boolean value expressed in a setting (for instance)"""

    return value in ('true', 'yes', '1', 1, True)


def str_to_hex(value: str | int) -> int:
    """Converts an hexadecimal value expressed in a setting (for instance)"""

    if isinstance(value, str):
        return int(value, 0)
    else:
        return value


def to_uuid(value: str | uuid.UUID) -> uuid.UUID:
    """Converts a string into an UUID object (if not already one)"""

    return uuid.UUID(value) if isinstance(value, str) else value


#
# Token classes declarations
#


@define
class Lib(Token):
    class LibType(Enum):
        KiCad = 'KiCad'
        Legacy = 'Legacy'
        AltiumDesigner = 'Altium Designer'
        Eagle = 'Eagle'
        GEDA_Pcb = 'GEDA/Pcb'

    name: str = field(metadata=dict(is_named=True))
    type: LibType = field(  # noqa: A003
        converter=LibType, metadata=dict(is_named=True, quoted=True, skip_space=True)
    )
    uri: str = field(metadata=dict(is_named=True, skip_space=True))
    options: str = field(metadata=dict(is_named=True, skip_space=True))
    descr: str = field(metadata=dict(is_named=True, skip_space=True))


@define
class FpLibTable(Token):
    version: Version = field(metadata=dict(newline_before=True, newline_after=True))
    libs: list[Lib] = field(metadata=dict(newline_after=True))


@define
class General(Token):
    thickness: float = field(metadata=dict(is_named=True, newline_before=True, newline_after=True))


@define
class Paper(Token):
    class PaperSize(Enum):
        A0 = 'A0'
        A1 = 'A1'
        A2 = 'A2'
        A3 = 'A3'
        A4 = 'A4'
        A5 = 'A5'
        A = 'A'
        B = 'B'
        C = 'C'
        D = 'D'
        E = 'E'
        USLetter = 'USLetter'
        USLegal = 'USLegal'
        USLedger = 'USLedger'
        User = 'User'

    paper_size: PaperSize = field(converter=PaperSize, metadata=dict(quoted=True))
    width: float | None = None
    height: float | None = None
    portrait: bool = field(default=False, metadata=dict(literal=True))


@define
class Page(Paper):  # Older compatible name for paper
    pass


@define
class Comment(Token):
    n: int
    comment: str


@define
class TitleBlock(Token):
    title: str | None = None
    date: str | None = None
    rev: str | None = None
    company: str | None = None
    comment: list[Comment] | None = None


@define
class _LayerDef(Token):
    """This is an "internal" token declaration to model layers declared in
    the header of a kicad_pcb token.

    These SExpr do not correspond to a usual named-token form. Therefore, they
    need to be instantiated manually by the Layers token itself.
    """

    @classmethod
    def token_name(cls, usage: Literal['parse', 'export']) -> str:
        # Since we are an internal token declaration, our name does not correspond
        # to a token one. When we serialise (ie. export), we need to return an empty
        # string to avoid outputting a spurious name.

        if usage == 'export':
            return ''
        else:
            return super(cls, cls).token_name(usage)

    class LayerType(Enum):
        jumper = 'jumper'
        mixed = 'mixed'
        power = 'power'
        signal = 'signal'
        user = 'user'

    ordinal: int
    canonical_name: str
    type: LayerType = field(converter=LayerType)  # noqa: A003
    user_name: str | None = None


@define
class Layers(Token):
    layers: list[_LayerDef] = field(metadata=dict(newline_before_first=True, newline_after=True))

    @classmethod
    def from_sexpr_data(cls, args: list[Self | str | Number]) -> Self:
        """Overloads to manually instantiate _LayerDef objects."""

        new_args = [_LayerDef(*layer) for layer in args]
        return super().from_sexpr_data(new_args)


@define
class Pcbplotparams(Token):
    params: dict[str, Any] = field(
        metadata=dict(newline_before_first=True, newline_after=True, strip_0=False)
    )


@define(kw_only=True)
class Setup(Token):
    other_settings: dict[str, Any] = field(
        metadata=dict(newline_before_first=True, newline_after=True)
    )
    plot_settings: Pcbplotparams = field(metadata=dict(newline_after=True))


@define
class Net(Token):
    ordinal: int
    net_name: str


@define
class NetClass(Token):
    name: str
    description: str
    clearance: float
    trace_width: float
    via_dia: float
    via_drill: float
    uvia_dia: float
    uvia_drill: float
    add_net: str


@define
class Version(Token):
    CURRENT: ClassVar[Self | None] = None

    version: int

    def __attrs_post_init__(self) -> None:
        # Saves a "global" value of ourself to be able to access the current
        # file version as early as possible (ie. we cannot wait that it is set
        # on the main file token (eg. kicad_pcb) version member as this happens
        # last and we need to access it before to build versionned tokens).
        type(self).CURRENT = self


@define(kw_only=True)
class KicadPcb(Token):
    """Token for a .kicad_pcb file."""

    version: Version
    generator: str = field(metadata=dict(is_named=True, newline_after=True, quoted=False))
    general: General = field(metadata=dict(newline_before=True, newline_after=True))
    paper: Paper | Page = field(metadata=dict(newline_before=True, newline_after=True))
    title_block: TitleBlock | None = None
    layers: Layers = field(default=REQUIRED, metadata=dict(newline_after=True))
    setup: Setup = field(default=REQUIRED, metadata=dict(newline_before=True, newline_after=True))
    # properties
    nets: list[Net] = field(
        default=REQUIRED, metadata=dict(newline_before=True, newline_after=True)
    )
    net_classes: list[NetClass] | None = None  # Old versions
    footprints: list[Footprint] | None = field(
        default=REQUIRED, metadata=dict(newline_before=True, newline_after=True)
    )
    graphic_items: list[GraphicItem] = field(
        default=REQUIRED, metadata=dict(newline_before=True, newline_after=True)
    )
    data: list[Token | list] = field(
        default=REQUIRED,
        metadata=dict(newline_before=True, newline_after=True, newline_after_last=True),
    )

    @classmethod
    def from_sexpr_data(cls, args: list[Self | str | Number]) -> Self:
        if args[1][0] == 'host':  # Older host variant of generator
            args[1] = ['generator', ' '.join(args[1][1:])]

        return super().from_sexpr_data(args)


@define
class Footprint(Token):
    """Token for a .kicad_mod file."""

    name: str  # Aka library_link when placed in a PCB

    # In .kicad_mod only
    version: Version | None = None
    generator: str | None = field(
        default=None, metadata=dict(is_named=True, newline_after=True, quoted=False)
    )

    # In .kicad_pcb only
    locked: bool | None = field(default=None, metadata=dict(literal=True))
    placed: bool | None = field(default=None, metadata=dict(literal=True))

    layer: Layer = field(default=REQUIRED, metadata=dict(newline_after=True))

    # In .kicad_pcb only
    tstamp: uuid.UUID | None = field(
        default=None, converter=to_uuid, metadata=dict(newline_after=True)
    )
    at: At | None = field(default=None, metadata=dict(newline_after=True))

    # Covers things like attr, descr, tags, property, path, ...
    settings: dict[str, Any] = field(default=REQUIRED, metadata=dict(newline_after=True))

    graphic_items: list[GraphicItem] = field(default=REQUIRED, metadata=dict(newline_after=True))
    data: list[Token | list] = field(default=REQUIRED, metadata=dict(newline_after=True))


@define(order=True)
class XY(Token):
    """XY token that we also use as a base class for any token behaving like a point.

    We take the opportunity to define some common operators and methods on it that will
    simplify math operations later on.

    Can also be used as a vector.
    """

    x: float
    y: float

    def __add__(self, other: XY | float) -> Self:
        if isinstance(other, XY):
            return type(self)(x=self.x + other.x, y=self.y + other.y)
        else:
            return type(self)(x=self.x + other, y=self.y + other)

    def __sub__(self, other: XY | float) -> Self:
        if isinstance(other, XY):
            return type(self)(x=self.x - other.x, y=self.y - other.y)
        else:
            return type(self)(x=self.x - other, y=self.y - other)

    def __mul__(self, mult: float) -> Self:
        return type(self)(x=self.x * mult, y=self.y * mult)

    def __truediv__(self, quotient: float) -> Self:
        return type(self)(x=self.x / quotient, y=self.y / quotient)

    def __abs__(self) -> Self:
        return type(self)(x=abs(self.x), y=abs(self.y))

    def __neg__(self) -> Self:
        return type(self)(x=-self.x, y=-self.y)

    @property
    def mag(self) -> float:
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def dist(self, other: XY) -> float:
        return (self - other).mag

    def cast_to[T: 'XY'](self, cls: type[T]) -> T:
        """Casts a point-like token into another point-like token.

        Needed just to have correct token names when serialising.
        """

        if type(self) is not cls:
            return cls(x=self.x, y=self.y)
        else:
            return self


@define
class At(XY):
    angle: float | None = None
    unlocked: bool = field(default=False, metadata=dict(literal=True))


@define
class Start(XY):
    pass


@define
class Mid(XY):
    pass


@define
class End(XY):
    pass


@define
class Color(Token):
    r: float
    g: float
    b: float
    a: float


@define
class Stroke(Token):
    class StrokeType(Enum):
        dash = 'dash'
        dash_dot = 'dash_dot'
        dash_dot_dot = 'dash_dot_dot'
        dot = 'dot'
        default = 'default'
        solid = 'solid'

    width: float = field(metadata=dict(is_named=True))
    type: StrokeType = field(converter=StrokeType, metadata=dict(is_named=True))
    color: Color | None = None


@define
class Layer(Token):
    canonical_name: str


@define
class GraphicItem(Token):
    """A base token class usable to group all graphic items."""


@define
class Effects(Token):
    data: dict[str, Any]


@define
class FpText(GraphicItem):
    class FpTextType(Enum):
        reference = 'reference'
        value = 'value'
        user = 'user'

    type: FpTextType = field(converter=FpTextType)  # noqa: A003
    text: str
    at: At
    layer: Layer
    hide: bool = field(default=False, metadata=dict(literal=True, newline_after=True))
    effects: Effects = field(default=REQUIRED, metadata=dict(newline_after=True, indent=True))
    tstamp: uuid.UUID = field(
        default=REQUIRED, converter=to_uuid, metadata=dict(newline_after=True)
    )


@define
class FpTextBox(GraphicItem):
    data: dict[str, Any]


@define
class Line:
    """Base definition of a line defined by 2 points.

    Used not only to declare the various flavours and version of line tokens.
    But also to provide some math-related methods.
    """

    start: XY
    end: XY

    @property
    def center(self) -> XY:
        """Returns the center point of the line."""

        return (self.start + self.end) / 2

    def translate(self, vector: XY) -> Self:
        """Returns a new line being this line translated by the provided vector."""

        return type(self)(
            start=self.start + vector,
            end=self.end + vector,
        )

    def rotate_90deg(self) -> Self:
        """Returns a new line rotated by 90 degrees around 0."""

        return type(self)(
            start=XY(x=-self.start.y, y=self.start.x),
            end=XY(x=-self.end.y, y=self.end.x),
        )

    def intersect(self, other: Line) -> XY:
        """Returns the intersection point between two lines (even if the point is virtually
        not on the lines, ie. not on the line segments limited by the start and end points)."""

        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        x3, y3 = other.start.x, other.start.y
        x4, y4 = other.end.x, other.end.y

        x1y2_y1x2 = (x1 * y2) - (y1 * x2)
        x3y4_y3x4 = (x3 * y4) - (y3 * x4)
        denominator = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        return XY(
            x=((x1y2_y1x2 * (x3 - x4)) - ((x1 - x2) * x3y4_y3x4)) / denominator,
            y=((x1y2_y1x2 * (y3 - y4)) - ((y1 - y2) * x3y4_y3x4)) / denominator,
        )


@define
class Line_20171130(Line):
    angle: float
    layer: Layer
    width: float

    def to_20221018(self, target_cls: type[Line_20221018]) -> Line_20221018:
        return target_cls(
            start=self.start,
            end=self.end,
            angle=self.angle if self.angle != 90 else None,
            stroke=Stroke(width=self.width, type=Stroke.StrokeType.solid),
            layer=self.layer,
            tstamp=uuid.uuid4(),
        )


@define
class Line_20221018(Line):
    angle: float | None = None
    stroke: Stroke = field(default=REQUIRED, metadata=dict(newline_before=True))
    layer: Layer = REQUIRED
    tstamp: uuid.UUID = field(default=REQUIRED, converter=to_uuid)


@define
class FpLine(GraphicItem):
    pass


@define
class FpLine_20171130(FpLine, Line_20171130):
    pass


@define
class FpLine_20221018(FpLine, Line_20221018):
    pass


@define
class GrLine(GraphicItem):
    pass


@define
class GrLine_20171130(GrLine, Line_20171130):
    pass


@define
class GrLine_20221018(GrLine, Line_20221018):
    pass


@define
class FpRect(GraphicItem):
    data: dict[str, Any]


@define
class FpCircle(GraphicItem):
    data: dict[str, Any]


@runtime_checkable
class Arc(Protocol):
    """Base definition of an arc.

    Used not only to declare the various flavours and version of arc tokens.
    But also to provide some math-related methods.

    Relies on the presence of an end field, and center property to do its math.
    """

    end: End

    @property
    @abstractmethod
    def center(self) -> XY:
        """Center of the arc circle."""

        raise NotImplementedError

    @property
    def radius(self) -> float:
        """Radius of the arc circle."""

        return self.end.dist(self.center)

    @property
    def end_angle(self) -> float:
        """Returns the angle formed between the end point and the virtual zero point."""

        relative_end = (self.end - self.center) / self.radius
        return math.atan2(relative_end.y, relative_end.x)

    def point_at(self, angle: float) -> XY:
        """Returns the point on the arc circle at the given angle from the virtual zero point."""

        return XY(
            x=self.center.x + (self.radius * math.cos(angle)),
            y=self.center.y + (self.radius * math.sin(angle)),
        )


@define
class Arc_20171130(Arc):
    start: Start  # It is the center point actually
    end: End
    angle: float
    layer: Layer
    width: float

    @property
    def center(self) -> XY:
        return self.start.cast_to(XY)

    def to_20221018(self, target_cls: type[Arc_20221018]) -> Arc_20221018:
        """Converts to a 20221018 arc by recalculating the real arc start, and mid points."""

        end_angle = self.end_angle
        angle_rad = math.radians(self.angle)
        start = self.point_at(end_angle + angle_rad).cast_to(Start)
        middle = self.point_at(end_angle + (angle_rad / 2)).cast_to(Mid)

        return target_cls(
            start=start,
            mid=middle,
            end=self.end,
            stroke=Stroke(width=self.width, type=Stroke.StrokeType.solid),
            layer=self.layer,
            tstamp=uuid.uuid4(),
        )


@define
class Arc_20221018(Arc):
    start: Start
    mid: Mid
    end: End
    stroke: Stroke = field(metadata=dict(newline_before=True))
    layer: Layer
    tstamp: uuid.UUID = field(converter=to_uuid)

    @property
    def center(self) -> XY:
        """Center of the arc circle.

        This version of arc does not hold the center point information.
        Instead, we have to recalculate it, using chords defined by the three
        start, middle, and end points.
        """
        sm = Line(start=self.start, end=self.mid)
        sm_chord = sm.translate(-sm.center).rotate_90deg().translate(sm.center)

        me = Line(start=self.mid, end=self.end)
        me_chord = me.translate(-me.center).rotate_90deg().translate(me.center)

        return sm_chord.intersect(me_chord).cast_to(XY)


@define
class FpArc(GraphicItem):
    pass


@define
class FpArc_20171130(FpArc, Arc_20171130):
    pass


@define
class FpArc_20221018(FpArc, Arc_20221018):
    pass


@define
class GrArc(GraphicItem):
    pass


@define
class GrArc_20171130(GrArc, Arc_20171130):
    pass


@define
class GrArc_20221018(GrArc, Arc_20221018):
    pass


def convert_pcb_to_footprint(
    pcb: KicadPcb,
    name: str,
    generator: str = 'pcbnew',
    existing_footprint: Footprint | None = None,
) -> Footprint:
    """Takes a kicad PCB definition and convert it into a footprint.

    For now limited to very basic graphic items.
    If an existing_footprint is provided, it will reuse it but clear it of all its
    graphic items apart from FpText ones of types reference or value.
    """

    if not existing_footprint:
        footprint = Footprint(
            name=name,
            version=Version(20221018),
            generator=generator,
            layer=Layer(canonical_name='F.Cu'),
            settings=dict(attr=['board_only', 'exclude_from_pos_files', 'exclude_from_bom']),
            graphic_items=[
                FpText(
                    type=FpText.FpTextType.reference,
                    text='REF**',
                    at=At(x=0, y=-0.5, unlocked=True),
                    layer=Layer(canonical_name='F.SilkS'),
                    hide=True,
                    effects=Effects(data=dict(font=[['size', 1, 1], ['thickness', 0.1]])),
                    tstamp=uuid.uuid4(),
                ),
                FpText(
                    type=FpText.FpTextType.value,
                    text=name,
                    at=At(x=0, y=1, unlocked=True),
                    layer=Layer(canonical_name='F.Fab'),
                    hide=True,
                    effects=Effects(data=dict(font=[['size', 1, 1], ['thickness', 0.15]])),
                    tstamp=uuid.uuid4(),
                ),
            ],
            data=[],
        )
    else:
        footprint = deepcopy(existing_footprint)
        footprint.graphic_items = [
            item
            for item in footprint.graphic_items
            if isinstance(item, FpText)
            and (item.type in (FpText.FpTextType.reference, FpText.FpTextType.value))
        ]

    version = footprint.version.version

    def sorting_key(item: GraphicItem) -> Any:
        """Tries to sort like kicad seems to sort."""

        i1 = i2 = i3 = None
        if isinstance(item, FpText):
            i1 = 1
            i2 = (
                FpText.FpTextType.reference,
                FpText.FpTextType.value,
                FpText.FpTextType.user,
            ).index(item.type)
            i3 = item.text
        elif isinstance(item, Line):
            i1 = 2
            i2 = round(item.start.x, 6)
            i3 = round(item.start.y, 6)
        elif isinstance(item, Arc):
            i1 = 3
            i2 = round(item.start.x, 6)
            i3 = round(item.start.y, 6)
        else:
            i1 = 100

        return i1, i2, i3

    for item in sorted(pcb.graphic_items, key=sorting_key):
        fp_item = item.to_version(version).to_footprint()
        footprint.graphic_items.append(fp_item)

    return footprint


@kicad_cli.command('parse')
def cli_parse(
    filename: Path,
    reexport: Optional[Path] = None,
) -> None:
    obj = Token.from_sexpr(SParser.parse(filename))
    print('>>>', obj)

    if reexport:
        reexport.write_text(obj.to_sexpr_text())


@kicad_cli.command('convert-pcb-to-footprint')
def cli_convert_pcb_to_footprint(
    pcb_path: Path,
    footprint_path: Path,
) -> None:
    name = pcb_path.stem
    pcb: KicadPcb = Token.from_sexpr(SParser.parse(pcb_path))

    footprint = None
    if (footprint_path.suffix == '.kicad_mod') and footprint_path.exists():
        footprint = Token.from_sexpr(SParser.parse(footprint_path))

    footprint = convert_pcb_to_footprint(pcb, name, 'ergogen_keebs', footprint)

    # print(footprint)
    # print('--------')
    # print(footprint.to_sexpr_list())
    # print(footprint.to_sexpr_text())

    if footprint_path.suffix == '.pretty':
        footprint_path /= f'{name}.kicad_mod'
    footprint_path.parent.mkdir(exist_ok=True)
    footprint_path.write_text(footprint.to_sexpr_text())


@kicad_cli.command('update-fabrication-files')
def cli_update_fabrication_files(
    ergogen_yaml: Path,
    points_yaml: Annotated[Optional[Path], clyo.Option()] = None,  # noqa: UP007
    units_yaml: Annotated[Optional[Path], clyo.Option()] = None,  # noqa: UP007
    project: Annotated[Optional[str], clyo.Option()] = None,  # noqa: UP007
) -> None:
    from ergogen import Keyboard

    keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)

    if project:
        _update_project(keeb, keeb.fabrication[project])
    else:
        for project_data in keeb.fabrication.values():
            _update_project(keeb, project_data)


def _update_project(
    keeb: Keyboard,
    project: dict[str, dict[str, dict[str, str]]],
) -> None:
    project_folder = Path(project['folder'])
    if not project_folder.exists():
        msg = f'KiCad project folder "{project_folder!s}" does not exist'
        raise ValueError(msg)
    project_file_stem = project_folder / project['project-name']

    ergogen_lib = _ergogen_lib_info(project_folder)
    ergogen_lib_path = Path(ergogen_lib.uri.replace('${KIPRJMOD}', str(project_folder)))

    for obj_type, objs in project['objects'].items():
        if obj_type == 'outlines':
            for obj in objs:
                source_path = Path(f'ergogen-output/pcbs/{obj}.kicad_pcb')
                target_path = ergogen_lib_path / f'{obj}.kicad_mod'

                source_pcb: KicadPcb = Token.from_sexpr(SParser.parse(source_path))
                if target_path.exists():
                    target_footprint: Footprint = Token.from_sexpr(SParser.parse(target_path))
                else:
                    target_footprint = None

                target_footprint = convert_pcb_to_footprint(
                    source_pcb,
                    obj,
                    generator='ergogen',
                    existing_footprint=target_footprint,
                )

                target_path.parent.mkdir(exist_ok=True)
                target_path.write_text(target_footprint.to_sexpr_text())


def _ergogen_lib_info(project_folder: Path) -> Lib:
    def make_ergogen_lib() -> Lib:
        return Lib(
            name='Ergogen',
            type=Lib.LibType.KiCad,
            uri='${KIPRJMOD}/Ergogen.pretty',
            options='',
            descr='',
        )

    fp_lib_table_path = project_folder / 'fp-lib-table'
    if fp_lib_table_path.exists():
        fp_lib_table: FpLibTable = Token.from_sexpr(SParser.parse(fp_lib_table_path))
        for lib in fp_lib_table.libs:
            if lib.name == 'Ergogen':
                ergogen_lib = lib
                break
        else:
            ergogen_lib = make_ergogen_lib()
            fp_lib_table.libs.append(ergogen_lib)
            fp_lib_table_path.write_text(fp_lib_table.to_sexpr_text())
    else:
        ergogen_lib = make_ergogen_lib()
        fp_lib_table = FpLibTable(version=Version(version=7), libs=[ergogen_lib])
        fp_lib_table_path.write_text(fp_lib_table.to_sexpr_text())

    return ergogen_lib
