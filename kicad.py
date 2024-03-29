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
import functools
import logging
import math
import re
import types
import typing
import uuid
from abc import abstractmethod
from contextlib import _GeneratorContextManager, contextmanager, suppress
from copy import deepcopy
from enum import Enum
from functools import partial
from itertools import chain
from pathlib import Path
from types import GeneratorType
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Callable,
    ClassVar,
    Iterator,
    Literal,
    Optional,
    Protocol,
    Union,
    overload,
    runtime_checkable,
)

# Third-party imports
import attrs
import clyo
from attr import field, fields
from attrs import define
from clyo import ProgressContext, StatusContext
from rich import print
from typing_extensions import Self

# Local imports

if TYPE_CHECKING:
    from collections.abc import Iterable
    from numbers import Number
    from typing import TypeAlias

    from ergogen import Keyboard, Points

    SExpr: TypeAlias = str | float | int | list['SExpr']

_logger = logging.getLogger(__name__)
kicad_cli = clyo.ClyoTyper(help='KiCAD-related commands')


class SParser:
    # The following is no longer used as pyparsing is ULTRA slow
    # # Inspired by https://gist.github.com/hastern/ac2d7eab7a2a85f588d1
    # _Open = pp.Suppress('(')
    # _String = pp.QuotedString(quoteChar='"', unquoteResults=True)
    # _Attribute = _String ^ pp.common.number ^ pp.Word(pp.alphanums + '_-.')
    # _Close = pp.Suppress(')')
    # _SExpr = pp.Forward()
    # _SubSExpr = pp.Group(pp.ZeroOrMore(_SExpr | _Attribute))
    # _SExpr << (_Open + _SubSExpr + _Close)

    # @classmethod
    # def _parse_pyparsing(cls, content: str, *, unquote: bool = True) -> SExpr:
    #     if not unquote:
    #         cls._String.unquote_results = False

    #     result = cls._SExpr.parse_string(content).as_list()[0]
    #     # print(f'Done parsing: {len(result)} elements')

    #     if not unquote:
    #         cls._String.unquote_results = True

    #     return result

    # The following regexp-based version is inspired by:
    # https://rosettacode.org/wiki/S-expressions#Python
    # Adapted to fix a few quirks, comply with KiCad variant of SExpr (numbers and strings),
    # and optimise the speed of it.
    # sq: handles escaped "
    # num:
    #   - accept +number notation
    #   - accept scientific notation, eg. +1.23e4 (that's for some buggy ergogen
    #     outputs with almost nul values)
    #   - match only if followed by space, ) or newline. This allows for:
    #     - avoid catching SEM.VER.SION style as a number (SEM.VER) and a string (.SION)
    #     - avoid breaking apart things like 0x1234 (will match as string instead)
    _SExpr_RE = r"""(?mx)
        \s*(?:
            (?P<lparen>\() |   # Opening parenthesis
            (?P<rparen>\)) |   # Closing parenthesis
            (?P<number>(?:[+-]?\d+\.\d+(?=[ )\n])) |  # Real
                       (?:[+-]?\d+(?=[ )\n])) |  # Integer
                       (?:[+-]?\d+\.\d+[eE][+-]?\d+(?=[ )\n])) |  # Sci-real
                       (?:[+-]?\d+[eE][+-]?\d+(?=[ )\n]))  # Sci-integer
            ) |
            (?P<quoted_string>"((?:[^"]|(?<=\\)")*)") |
            (?P<string>[^()\s]+)
        )"""

    @classmethod
    def _parse_regex(cls, content: str, *, unquote: bool = True) -> SExpr:
        progress = ProgressContext()
        progress.increase('parse', len(content), flush=True)
        last_pos = 0

        stack: list[list[SExpr]] = []
        out: list[SExpr] = []

        for match in re.finditer(cls._SExpr_RE, content):
            start = match.start()
            progress.advance('parse', steps=start - last_pos)
            last_pos = start

            if match['lparen'] is not None:
                stack.append(out)
                out = []

            elif match['rparen'] is not None:
                assert stack, 'Trouble with nesting of brackets'
                tmpout, out = out, stack.pop()
                out.append(tmpout)
                progress.increase('parse', len(tmpout))

            elif (value := match['number']) is not None:
                v = float(value) if '.' in value else int(value)
                out.append(v)

            elif (value := match['quoted_string']) is not None:
                if unquote:
                    out.append(value[1:-1].replace(r'\"', '"'))
                else:
                    out.append(value.replace(r'\"', '"'))

            elif (value := match['string']) is not None:
                out.append(value)

            else:
                msg = f'Error: "{match.group()}" => {match.groupdict()}'
                raise RuntimeError(msg)

        progress.advance('parse', steps=len(content) - last_pos, flush=True)

        assert not stack, 'Trouble with nesting of brackets'
        return out[0]

    @classmethod
    def parse(cls, content: str, *, unquote: bool = True) -> SExpr:
        # result = cls._parse_pyparsing(content, unquote=unquote)
        return cls._parse_regex(content, unquote=unquote)

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

    __slots__ = ()

    CURRENT_CONTEXT: ClassVar[list[type[Token]]] = []

    @staticmethod
    @contextmanager
    def with_context(context: type[Token]) -> Iterator[None]:
        Token.CURRENT_CONTEXT.append(context)
        try:
            yield
        finally:
            Token.CURRENT_CONTEXT.pop()

    @classmethod
    def as_context(cls) -> _GeneratorContextManager[None]:
        return cls.with_context(cls)

    #
    # Token name <-> class matching, and versioning section
    #

    __inheritors__: ClassVar[
        dict[type, dict[str, dict[str, type[Self]]]]
    ] = collections.defaultdict(
        partial(collections.defaultdict, dict),
    )

    def __init_subclass__(cls, *args: Any, **kwargs: Any) -> None:
        """We keep track of all inheritors of Token in order to match their
        token name with corresponding class when we parse.
        """

        super().__init_subclass__(*args, **kwargs)

        if hasattr(cls, '__attrs_attrs__'):
            attrs.resolve_types(cls, include_extras=True)

        token_name = cls.token_name(usage='parse')
        if token_name:
            class_name = f'{cls.__module__}.{cls.__qualname__}'
            for base in cls.mro()[1:-1]:
                Token.__inheritors__[base][token_name][class_name] = cls
                # This last dict level is here to keep only the last "declared"
                # class for a given class name. It is needed because this method
                # sees a class more than once: first the original one, then the
                # attrs.define() wrapped one (because it uses slots by default).
                # They have the same name, but are not the same objects, such
                # that a simple set cannot be used.
                # We only want to keep the wrapped one.
                # Also, filtering on __attrs_attrs__ is not sufficient as in the case
                # of a class subclassing another attrs.defined one, this special
                # member will be present even in the original one (and that's not
                # the one we want).
                # So, in practice, we don't really care about the class name here.
                # We only need it to base our set (ie. dict keys) on it, while
                # being interested only in the value (ie. class object) it represents.

    @classmethod
    @functools.cache
    def token_name_to_classes(cls, token_name: str) -> Iterable[type[Token]]:
        """Returns the token class corresponding to token_name"""
        return Token.__inheritors__[Token][token_name].values()

    @classmethod
    @functools.cache
    def token_name(cls, usage: Literal['parse', 'export']) -> str | None:
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

    @classmethod
    def accept(cls, sexpr: SExpr) -> bool:
        """Says if this class accept the current sexpr.

        During the resolution of token name to class, this method is invoked on a
        tentative class. By default, to cover the most common and simple case, if
        a token class has a unique token name (ie. no two token classes share the same token name),
        then just accepting it regardless of the SExpr content should be fine.

        But in case several token classes share the same token name, then they are all asked
        to accept or not. In the end, if more than one accepts, an error is raised.
        Therefore, token class reimplementing this method should really be certain to
        accept only what is for them.
        Note that it is fine if none accept, as in that case the SExpr will be kept in raw form.

        To determine if they should accept or not, token classes can implement any strategy
        they want. The provided SExpr may help by inspecting its structure.
        Another helper is the Token.CURRENT_CONTEXT stack. The last element of that stack
        is the parent token class. And by walking up the stack, one can retrace the entire
        current hierarchy of token classes.
        """
        return True

    @staticmethod
    @functools.cache
    def _camel_to_snake(name: str) -> str:
        """Converts a class name in Camel form into a snake form corresponding to
        the way token names are made."""

        # From https://stackoverflow.com/a/1176023
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    @staticmethod
    @functools.cache
    def _extract_version(name: str) -> int | None:
        """Token classes can have a _VERSION suffix used for versioning the
        various file formats kicad had."""

        with suppress(Exception):  # If it fails for any reason, we return None
            return int(name.rsplit('_', maxsplit=1)[-1])
        return None

    @classmethod
    @functools.cache  # Pretty much one static per (class, version) pair
    def _get_versionned_token_class(cls, current_version: int) -> type[Token]:
        """Handles versionned tokens

        The logic is that versionned token classes have a date suffix in their name.
        We extract that suffix for each subclass of our current class (who should just
        be an empty class only used to fullfill token name matching).
        We build a list of candidate subclasses, and then pick the one that matches
        the current file version.
        """

        if not (subclasses := cls.__inheritors__[cls]):
            return cls

        candidates: dict[int, type[Self]] = {}
        for more_subclasses in subclasses.values():
            for subcls_name, subcls in more_subclasses.items():
                if version := cls._extract_version(subcls_name):
                    candidates[version] = subcls

        if not candidates:
            return cls

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
    @functools.cache
    def _get_field_types(
        field_type: Any,
    ) -> tuple[type[Any], tuple[type[Any], ...] | None]:
        """Determines proper field type.

        Takes care of interpreting Unions and Generics.
        """

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

        return (
            (type(field_type) is not tuple) and (field_type is bool) and field.metadata['literal']
        )

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

        return (type(arg) is list) and (len(arg) == 2) and (arg[0] == match_name)  # noqa: E721

    @staticmethod
    @functools.cache
    def _is_optional_field(default: Any) -> bool:
        """Recognises a field that is not required"""

        return default not in (attrs.NOTHING, REQUIRED)

    #
    # Token parsing section
    #

    @classmethod
    def from_file(cls, path: Path) -> Self:
        ProgressContext().add_task('parse', f'Loading {path}')

        sexpr = SParser.parse(path.read_text())
        result = cls.from_sexpr(sexpr)

        ProgressContext().flush('parse')
        ProgressContext().update('parse', visible=False)
        return result

    @classmethod
    def from_text(cls, content: str) -> Self:
        ProgressContext().add_task('parse', 'Loading')

        sexpr = SParser.parse(content)
        result = cls.from_sexpr(sexpr)

        ProgressContext().flush('parse')
        ProgressContext().update('parse', visible=False)
        return result

    @classmethod
    def from_sexpr(cls, sexpr: SExpr) -> Token | str | Number:
        """Takes the output from SParser and produces object representation of it."""

        # print('evaluating', sexpr)
        if (type(sexpr) is str) or (type(sexpr) is float) or (type(sexpr) is int):  # noqa: E721
            return sexpr

        token_name = sexpr[0]
        token_classes = cls.token_name_to_classes(token_name)
        candidates = [
            tentative_class for tentative_class in token_classes if tentative_class.accept(sexpr)
        ]
        if not candidates:
            token_class = None
        elif len(candidates) == 1:
            token_class = candidates[0]
        else:
            msg = f'Got more than one accepting token class for {sexpr=}: {candidates=}'
            raise RuntimeError(msg)

        if token_class is None:
            # If we don't have one, we resort to keeping it in list form.
            # Can be more intelligently used later (or just appended as raw data
            # in a dedicated token class member).
            token_class = list
            is_token = False
            attributes = sexpr
            nargs = len(attributes)
        else:
            # Otherwise we strip out the token name itself from what needs to be
            # deeply/recursively parsed.
            attributes = sexpr[1:]
            nargs = len(attributes) + 1
            is_token = True

        # Deep convertion here:
        # with cls._with_context(token_class):
        #     args: list[Self | str | Number] = [
        #         cls.from_sexpr(attribute) for attribute in attributes
        #     ]
        args: list[Self | str | Number]
        if is_token:
            Token.CURRENT_CONTEXT.append(token_class)
            try:
                args = [cls.from_sexpr(attribute) for attribute in attributes]
            finally:
                Token.CURRENT_CONTEXT.pop()
        else:
            args = [cls.from_sexpr(attribute) for attribute in attributes]

        # Actual object instantiation...
        # print('token is', token_name, token_class, args)
        if not is_token:  # Ie. it's a list
            obj = token_class(args)
            ProgressContext().advance('parse', steps=nargs)
            return obj
        else:
            # ... except if it is a token class, in which case we deffer to the
            # (much more) complex from_sexpr_data().
            # This split allows subclasses to customise args before feeding them
            # back to Token.from_sexpr_data().
            obj = token_class.from_sexpr_data(args)
            ProgressContext().advance('parse', steps=nargs)
            return obj

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

        if Version.CURRENT is not None:
            cls = cls._get_versionned_token_class(Version.CURRENT.version)

        # To build the kwargs, we take each declared field, and try to match it
        # to 0, 1, or more positional args. To match, we rely on type hints.
        kwargs = {}
        # Optimisation: Instead of popping each arg we use, we rather keep an index
        # on the current positional arg. Except in (rare) case of kw_only, where we will pop them.
        consummed_args = 0
        # Optimisation: Minimize calling len(). In case of kw_only, we have to
        # decrement len_args each time we pop an arg.
        len_args = len(args)
        for field in fields(cls):  # noqa: F402
            field: attrs.Attribute[Any]
            field_type, field_type_args = cls._get_field_types(field.type)
            kw_only = field.kw_only

            # print(
            #     f'> {field.name}, {field.type}, {field_type}, {field_type_args}, '
            #     f'{field.default=}, {field.kw_only=}'  # , {args[consummed_args]}'
            # )
            # Process optionals
            if cls._is_optional_field(field.default):
                if (
                    len_args == consummed_args
                ):  # Not even any positional argument left, skip this field
                    continue

                if cls._is_literal_field(field, field_type):
                    # Case of literals that are just boolean True if present
                    if not cls._match_literal_field(field, args[consummed_args]):
                        continue  # Not matching => skip this field
                    args[consummed_args] = True

                elif cls._is_named_value(args[consummed_args], field.name):  # noqa: SIM114
                    pass  # Handled later

                # Optional lists and dicts handling
                elif (type(field_type) is not tuple) and issubclass(field_type, (list, dict)):
                    pass  # Handled later

                # If type of this optional field does not match next positional arg, skip this field
                elif not isinstance(args[consummed_args], field_type):
                    continue

                # TODO: Handle case of kw_only field, which, by luck is no issue for the only cases
                # of optional kw_only field (title_block in kicad_pcb)

            if type(field_type) is not tuple:  # issubclass can't handle Union field type
                if issubclass(field_type, list):
                    # Case of a list[AToken] definition.
                    # We exhaust all of this AToken type in the positional args to fill the list.

                    if kw_only:
                        list_ = []
                        i = consummed_args
                        while i < len_args:
                            if not isinstance(args[i], field_type_args):
                                i += 1
                            else:
                                list_.append(args.pop(i))
                                len_args -= 1
                    else:
                        i = 0
                        for i, arg in enumerate(args[consummed_args:]):
                            if not isinstance(arg, field_type_args):
                                break
                        else:
                            i += 1  # Case of a list terminating on a matching item
                        list_ = args[consummed_args : consummed_args + i]
                        consummed_args += i

                    kwargs[field.name] = list_
                    continue

                elif issubclass(field_type, dict):
                    # Case of a dict[str, Any] definition.
                    # We exhaust all positional args that are non-empty lists (must have a name)
                    # to fill the dict.
                    dict_ = {}
                    if kw_only:
                        i = consummed_args
                        while i < len_args:
                            if not ((type(args[i]) is list) and args[i]):  # noqa: E721  # Opti.
                                i += 1
                            else:
                                name, *value = args.pop(i)
                                len_args -= 1

                                if len(value) == 1:
                                    value = value[0]
                                dict_[name] = value
                    else:
                        for arg in args[consummed_args:]:
                            if not ((type(arg) is list) and arg):  # noqa: E721  # Opti.
                                break
                            name, *value = args[consummed_args]
                            consummed_args += 1

                            if len(value) == 1:
                                value = value[0]
                            dict_[name] = value

                    kwargs[field.name] = dict_
                    continue

            if kw_only:
                i = consummed_args
                while i < len_args:
                    if cls._is_named_value(args[i], field.name):
                        kwargs[field.name] = args.pop(i)[1]
                        len_args -= 1
                        break

                    if isinstance(args[i], field_type):
                        kwargs[field.name] = args.pop(i)
                        len_args -= 1
                        break

                    i += 1
            else:
                arg = args[consummed_args]
                if cls._is_named_value(arg, field.name):
                    kwargs[field.name] = arg[1]
                    consummed_args += 1

                else:
                    # Any other case, the next positional arg is our current field value
                    kwargs[field.name] = arg
                    consummed_args += 1

        # print(cls.__name__, f'{kwargs=}')

        if consummed_args < len_args:
            # print(f'{consummed_args=}, {args[:consummed_args]=}, {args[consummed_args:]=}')
            args = args[consummed_args:]
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

    def to_file(self, path: Path) -> None:
        ProgressContext().add_task('export', f'Exporting to {path}', total=self._count_elements())

        path.write_text(self.to_sexpr_text())

        ProgressContext().flush('export')
        ProgressContext().update('export', visible=False)

    if TYPE_CHECKING:
        # The iterator to_sexpr_elements() returns.
        _ToSExprIterator: TypeAlias = Iterator[
            Union[
                tuple[
                    attrs.Attribute[Any],
                    SExpr | '_ToSExprIterator',
                ],
                tuple[
                    None,
                    str | None,
                ],
            ]
        ]

        NewlinesFilter: TypeAlias = Callable[
            [attrs.Attribute[Any] | None, Any | None, dict[str, bool]], dict[str, bool]
        ]

    def to_sexpr_list(self) -> SExpr:
        """Deeply converts this token to SExpr list-form"""
        ProgressContext().add_task('export', 'Exporting', total=self._count_elements())

        def list_walker(value: list[SExpr]) -> Iterator[SExpr]:
            for item in value:
                item_type = type(item)
                if item_type is GeneratorType:
                    yield list(walker(item))
                elif item_type is list:
                    yield list(list_walker(item))
                elif item in ('', '\n'):
                    continue
                else:
                    yield item

        def walker(it: Token._ToSExprIterator) -> Iterator[SExpr]:
            """Walk-down a token-sexpr iterator as returned by to_sexpr_elements().

            Returns the SExpr elements as an iterator, that just needs to be wrapped
            in a list() to be joined."""

            for _, value in it:
                value_type = type(value)
                if value_type is GeneratorType:
                    yield list(walker(value))
                elif value_type is list:
                    yield list(list_walker(value))
                elif value in ('', '\n'):
                    continue
                elif value is not None:
                    yield value

        to_return = list(walker(self.to_sexpr_elements()))
        ProgressContext().flush('export')
        ProgressContext().update('export', visible=False)
        return to_return

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

            precision = field.metadata['precision']
            s = f'{value:.{precision}f}'
            if (s[-1] == '0') and field.metadata['strip_0']:
                return s.rstrip('.0')
            else:
                return s

        def list_walker(field: attrs.Attribute[Any] | None, value: list[SExpr]) -> Iterator[str]:
            """Walk-down a list. Returns an iterator of strings representing SExpr elements"""

            for item in value:
                item_type = type(item)
                if item_type is list:
                    yield f'({joiner(list_walker(field, item))})'
                elif item_type is float:
                    yield float_to_str(item, field)
                elif item_type is GeneratorType:
                    yield f'({joiner(walker(item))})'
                else:
                    yield str(item)

        def walker(it: Token._ToSExprIterator) -> Iterator[str | None]:
            """Walk-down a token-sexpr iterator as returned by to_sexpr_elements().

            Returns an iterator of strings representing SExpr elements."""

            nonlocal indent, skip_space
            indent += INDENT_BY

            for field, value in it:
                if not field:  # value is str | None
                    yield value

                else:
                    local_indent = 0
                    if local_indent := field.metadata['indent']:
                        if type(local_indent) is bool:  # noqa: E721  # Opti.
                            local_indent = INDENT_BY
                        indent += local_indent

                    value_type = type(value)
                    if value_type is GeneratorType:
                        str_value = f'({joiner(walker(value))})'
                    elif value_type is list:
                        str_value = f'({joiner(list_walker(field, value))})'
                    elif value_type is float:
                        str_value = float_to_str(value, field)
                    elif value_type is str:
                        str_value = value
                    else:
                        str_value = str(value)

                    skip_space = field.metadata['skip_space']
                    yield str_value

                    if local_indent:
                        indent -= local_indent

            indent -= INDENT_BY
            yield None

        def joiner(it: Iterator[str | None]) -> str:
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
                    if s and (s[-1] == ' ') and is_newline:
                        s = s.rstrip(' ')
                    s += item
                else:
                    had_newline = False

            return s

        return f'({joiner(walker(self.to_sexpr_elements()))})\n'

    def _count_elements(self) -> int:
        """Recurse to walk down our fields in order to know how much elements we have."""

        our_fields = fields(type(self))
        count = len(our_fields) + 1

        for field in our_fields:
            field: attrs.Attribute[Any]
            field_type, _ = self._get_field_types(field.type)

            value = getattr(self, field.name)
            if value is None:
                continue

            if type(field_type) is tuple:
                for type_ in field_type:
                    if isinstance(value, type_):
                        field_type = type_
                        break
                else:
                    msg = f'Field {field.name} of {type(self).__name__} is not of correct type: {field_type}'
                    raise ValueError(msg)

            if field_type is list:
                for item in value:
                    if isinstance(item, Token):
                        count += item._count_elements()

            elif issubclass(field_type, Token):
                count += value._count_elements()

        return count

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

        progress = ProgressContext()
        Token.CURRENT_CONTEXT.append(type(self))
        yield None, self.token_name(usage='export')
        progress.advance('export', 1)

        newlines_filter: NewlinesFilter = None
        if hasattr(self, 'newlines_filter'):
            newlines_filter = self.newlines_filter
            newlines: dict[str, bool] = dict(at_end=False)
            newlines_filter(None, None, newlines)

        for field in fields(type(self)):
            field: attrs.Attribute[Any]
            field_type, field_type_args = self._get_field_types(field.type)
            value = getattr(self, field.name)

            nl_before_first = field.metadata['newline_before_first']
            nl_before = field.metadata['newline_before']
            nl_after = field.metadata['newline_after']
            nl_after_last = field.metadata['newline_after_last']
            nl_force = field.metadata['force_newline_if_none']
            if newlines_filter:
                newlines['before_first'] = nl_before_first
                newlines['before'] = nl_before
                newlines['after'] = nl_after
                newlines['after_last'] = nl_after_last
                newlines['force_if_none'] = nl_force
                newlines = newlines_filter(field, value, newlines)
                nl_before_first = newlines['before_first']
                nl_before = newlines['before']
                nl_after = newlines['after']
                nl_after_last = newlines['after_last']
                nl_force = newlines['force_if_none']

            if self._is_optional_field(field.default) and (
                (value is None) or not isinstance(value, field_type)
            ):
                # print(f'skipping {field.name} on {type(self).__name__}')
                if nl_force:
                    yield None, '\n'

                progress.advance('export', 1)
                continue

            if value is REQUIRED:
                msg = f'Field {field.name} of {type(self).__name__} is missing'
                raise ValueError(msg)

            if type(field_type) is tuple:
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

            if field_type is list:
                if not value:
                    progress.advance('export', 1)
                    continue

                if nl_before_first:
                    yield None, '\n'

                for item in value:
                    if nl_before:
                        yield None, '\n'

                    if type(item) is str:  # noqa: E721  # Opti.
                        if field.metadata.get('quoted', True):
                            item = f'"{item}"'
                        yield field, item
                    elif isinstance(item, Token):
                        yield field, item.to_sexpr_elements()
                    else:
                        yield field, item

                    if nl_after:
                        yield None, '\n'

                if nl_after_last:
                    yield None, '\n'

                progress.advance('export', 1)
                continue

            elif field_type is dict:
                if not value:
                    progress.advance('export', 1)
                    continue

                if nl_before_first:
                    yield None, '\n'

                for key, item in value.items():
                    if nl_before:
                        yield None, '\n'

                    if type(item) is list:  # noqa: E721  # Opti.
                        if not item:
                            if type(key) is str:  # noqa: E721  # Opti.
                                key = f'"{key}"'
                            yield field, key
                        else:
                            yield field, [key, *item]
                    else:
                        if type(item) is str:  # noqa: E721  # Opti.
                            if field.metadata.get('quoted', False):
                                item = f'"{item}"'
                            elif not item:
                                item = '""'
                        yield field, [key, item]

                    if nl_after:
                        yield None, '\n'

                if nl_after_last:
                    yield None, '\n'

                progress.advance('export', 1)
                continue

            elif (type(value) is bool) and self._is_literal_field(field, field_type):  # noqa: E721
                if not value:
                    progress.advance('export', 1)
                    continue

                literal = field.metadata['literal']
                if type(literal) is bool:  # noqa: E721  # Opti.
                    literal = field.name

                if nl_before:
                    yield None, '\n'

                yield field, literal

                if nl_after:
                    yield None, '\n'

                progress.advance('export', 1)
                continue

            if nl_before:
                yield None, '\n'

            if field_type is str:
                if field.metadata.get('quoted', True):
                    value = f'"{value}"'
                if field.metadata['is_named']:
                    value = [field.name, value]

                yield field, value

            elif (field_type is float) or (field_type is int):
                if field.metadata['is_named']:
                    value = [field.name, value]

                yield field, value

            elif field_type is uuid.UUID:
                value = str(value)
                if field.metadata.get('quoted', False):
                    value = f'"{value}"'
                if field.metadata['is_named']:
                    value = [field.name, value]

                yield field, value

            elif issubclass(field_type, Enum):
                value = value.value
                if field.metadata.get('quoted', False):
                    value = f'"{value}"'
                if field.metadata['is_named']:
                    value = [field.name, value]

                yield field, value

            elif issubclass(field_type, Token):
                if field.metadata['is_named']:
                    yield field, [field.name, value.to_sexpr_elements()]
                else:
                    yield field, value.to_sexpr_elements()

            if nl_after:
                yield None, '\n'

            progress.advance('export', 1)

        if newlines_filter and newlines['at_end']:
            yield None, '\n'

        Token.CURRENT_CONTEXT.pop()

    #
    # Manipulation methods
    #

    def match(self, **kwargs: Any) -> bool:
        return all(getattr(self, field_name) == value for field_name, value in kwargs.items())


#
# Function usable in fields declarations
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


@overload
def float_key(value: float) -> float:
    ...


@overload
def float_key(value: None) -> None:
    ...


def float_key(value: float | None) -> float | None:
    if value is not None:
        return round(value, 6)
    else:
        return None


def token_field(
    *,
    is_named: bool = False,
    quoted: bool | None = None,
    literal: bool | str = False,
    precision: int = 6,
    strip_0: bool = True,
    skip_space: bool = False,
    indent: bool = False,
    newlines: str | None = None,
    newline_before: bool = False,
    newline_after: bool = False,
    newline_before_first: bool = False,
    newline_after_last: bool = False,
    force_newline_if_none: bool = False,
    metadata: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    if newlines:
        try:
            f_index = newlines.index('()')
        except ValueError as ex:
            msg = "newlines parameter must contain '()' to signify the field position"
            raise ValueError(msg) from ex

        lb_index = None
        rb_index = None
        with suppress(ValueError):
            lb_index = newlines.index('[')

        if lb_index is not None:
            if lb_index >= f_index:
                msg = "'[' in newlines parameter must come before '()'"
                raise ValueError(msg)
            try:
                rb_index = newlines.index(']')
            except ValueError as ex:
                msg = "'[' in newlines parameter must be complemented with a closing ']'"
                raise ValueError(msg) from ex
            if rb_index <= (f_index + 1):
                msg = "']' in newlines parameter must come after '()'"
                raise ValueError(msg)

        i = 0
        try:
            while i <= len(newlines):
                pos = newlines.index('\n', i)
                if (lb_index is not None) and (pos < lb_index):
                    newline_before_first = True
                elif pos < f_index:
                    newline_before = True
                elif (rb_index is not None) and (pos > rb_index):
                    newline_after_last = True
                elif pos > (f_index + 1):
                    newline_after = True
                else:
                    msg = "No '\\n' within '()' in newlines parameter"
                    raise ValueError(msg)

                i += pos + 1

        except ValueError:
            pass

    def _add(value: Any, name: str) -> None:
        if value is not None:
            metadata[name] = value

    if metadata is None:
        metadata = {}
    _add(is_named, 'is_named')
    _add(quoted, 'quoted')
    _add(literal, 'literal')
    _add(precision, 'precision')
    _add(strip_0, 'strip_0')
    _add(skip_space, 'skip_space')
    _add(indent, 'indent')
    _add(newline_before, 'newline_before')
    _add(newline_after, 'newline_after')
    _add(newline_before_first, 'newline_before_first')
    _add(newline_after_last, 'newline_after_last')
    _add(force_newline_if_none, 'force_newline_if_none')

    if not metadata:
        metadata = None

    if 'default' not in kwargs:
        kwargs['default'] = REQUIRED

    return field(metadata=metadata, **kwargs)


def uuid_field(**kwargs: Any) -> Any:
    kwargs.setdefault('converter', to_uuid)
    kwargs.setdefault('eq', False)
    kwargs.setdefault('is_named', True)

    return token_field(**kwargs)


def literal_field(**kwargs: Any) -> Any:
    kwargs.setdefault('default', False)
    kwargs.setdefault('literal', True)

    return token_field(**kwargs)


def named_field(**kwargs: Any) -> Any:
    kwargs.setdefault('is_named', True)

    return token_field(**kwargs)


def ensure_metadata(
    cls: type[Token],
    fields: list[attrs.Attribute[Any]],
) -> list[attrs.Attribute[Any]]:
    result: list[attrs.Attribute[Any]] = []
    for field in fields:
        if field.metadata:
            result.append(field)
        else:
            result.append(
                field.evolve(
                    metadata=dict(
                        is_named=False,
                        literal=False,
                        precision=6,
                        strip_0=True,
                        skip_space=False,
                        indent=False,
                        newline_before=False,
                        newline_after=False,
                        newline_before_first=False,
                        newline_after_last=False,
                        force_newline_if_none=False,
                    ),
                ),
            )

    return result


#
# Token classes declarations
#


@define(field_transformer=ensure_metadata)
class Lib(Token):
    class LibType(Enum):
        KiCad = 'KiCad'
        Legacy = 'Legacy'
        AltiumDesigner = 'Altium Designer'
        Eagle = 'Eagle'
        GEDA_Pcb = 'GEDA/Pcb'

    name: str = named_field()
    type: LibType = named_field(converter=LibType, quoted=True, skip_space=True)  # noqa: A003
    uri: str = named_field(skip_space=True)
    options: str = named_field(skip_space=True)
    descr: str = named_field(skip_space=True)


@define(field_transformer=ensure_metadata)
class General(Token):
    thickness: float | int = named_field(newlines='\n()\n')


@define(field_transformer=ensure_metadata)
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

    paper_size: PaperSize = token_field(converter=PaperSize, quoted=True)
    width: float | int | None = None
    height: float | int | None = None
    portrait: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Page(Paper):  # Older compatible name for paper
    pass


@define(field_transformer=ensure_metadata)
class Comment(Token):
    n: int
    comment: str


@define(field_transformer=ensure_metadata)
class TitleBlock(Token):
    title: str | None = None
    date: str | None = None
    rev: str | None = None
    company: str | None = None
    comment: list[Comment] | None = None


@define(field_transformer=ensure_metadata)
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
    type: LayerType = token_field(converter=LayerType)  # noqa: A003
    user_name: str | None = None


@define(field_transformer=ensure_metadata)
class Layers(Token):
    layers_def: list[_LayerDef] = token_field(newlines='\n[()\n]')
    layers_use: list[str] = token_field(quoted=True)

    @classmethod
    def from_sexpr_data(cls, args: list[Self | str | Number]) -> Self:
        """Overloads to manually instantiate _LayerDef objects."""

        new_args = []
        for arg in args:
            if isinstance(arg, list):
                new_args.append(_LayerDef(*arg))
            else:
                new_args.append(arg)

        return super().from_sexpr_data(new_args)


@define(field_transformer=ensure_metadata)
class _LayerStackup(Token):
    name: str | int
    type: str = named_field()
    color: str | None = named_field(default=None)
    thickness: float | int | None = named_field(default=None)
    material: str | None = named_field(default=None)
    epsilon_r: float | int | None = named_field(default=None)
    loss_tangent: float | int | None = named_field(default=None)

    @classmethod
    def token_name(cls, usage: Literal['parse', 'export']) -> str | None:
        return 'layer'

    @classmethod
    def accept(cls, sexpr: SExpr) -> bool:
        return Token.CURRENT_CONTEXT[-1] == Stackup


@define(field_transformer=ensure_metadata)
class Stackup(Token):
    layers: list[_LayerStackup] = token_field(newlines='\n[()\n]')
    copper_finish: str | None = named_field(default=None, newlines='()\n')
    dielectric_constraints: str | None = named_field(default=None, quoted=False, newlines='()\n')
    edge_connector: str | None = named_field(default=None, quoted=False, newlines='()\n')
    castellated_pads: str | None = named_field(default=None, quoted=False, newlines='()\n')
    edge_plating: str | None = named_field(default=None, quoted=False, newlines='()\n')


@define(field_transformer=ensure_metadata)
class Pcbplotparams(Token):
    params: dict[str, Any] = token_field(newlines='\n[()\n]', strip_0=False)


@define(kw_only=True, field_transformer=ensure_metadata)
class Setup(Token):
    stackup: Stackup | None = token_field(default=None, newlines='\n()')
    other_settings: dict[str, Any] = token_field(newlines='\n[()\n]')
    plot_settings: Pcbplotparams = token_field(newlines='()\n')


# This is for a pad property. It is incompatible with a footprint property...
# @define(field_transformer=ensure_metadata)
# class Property(Token):
#     props = dict[str, Any]


@define(field_transformer=ensure_metadata)
class Property(Token):
    key: str
    value: str


@define(field_transformer=ensure_metadata)
class Net(Token):
    ordinal: int
    net_name: str | None = None


@define(field_transformer=ensure_metadata)
class NetClass(Token):
    name: str
    description: str = token_field(newlines='()\n')
    clearance: float | int = named_field(newlines='()\n')
    trace_width: float | int = named_field(newlines='()\n')
    via_dia: float | int = named_field(newlines='()\n')
    via_drill: float | int = named_field(newlines='()\n')
    uvia_dia: float | int = named_field(newlines='()\n')
    uvia_drill: float | int = named_field(newlines='()\n')
    add_net: str = named_field(newlines='()\n')


@define(field_transformer=ensure_metadata)
class Version(Token):
    CURRENT: ClassVar[Self | None] = None

    version: int

    def __attrs_post_init__(self) -> None:
        # Saves a "global" value of ourself to be able to access the current
        # file version as early as possible (ie. we cannot wait that it is set
        # on the main file token (eg. kicad_pcb) version member as this happens
        # last and we need to access it before to build versionned tokens).
        type(self).CURRENT = self


@define(order=True, field_transformer=ensure_metadata)
class Xy(Token):
    """XY token that we also use as a base class for any token behaving like a point.

    We take the opportunity to define some common operators and methods on it that will
    simplify math operations later on.

    Can also be used as a vector.
    """

    x: float | int = token_field(eq=float_key)
    y: float | int = token_field(eq=float_key)

    def __add__(self, other: Xy | float) -> Self:
        if isinstance(other, Xy):
            return type(self)(x=self.x + other.x, y=self.y + other.y)
        else:
            return type(self)(x=self.x + other, y=self.y + other)

    def __sub__(self, other: Xy | float) -> Self:
        if isinstance(other, Xy):
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

    def dist(self, other: Xy) -> float:
        return (self - other).mag

    def cast_to[T: 'Xy'](self, cls: type[T]) -> T:
        """Casts a point-like token into another point-like token.

        Needed just to have correct token names when serialising.
        """

        if type(self) is not cls:
            return cls(x=self.x, y=self.y)
        else:
            return self

    def __hash__(self) -> int:
        return hash((float_key(self.x), float_key(self.y)))
        # return hash((self.x, self.y))


@define(field_transformer=ensure_metadata)
class Xyz(Xy):
    z: float | int = token_field(eq=float_key)


def angle_normalizer(angle: float | None) -> float | None:
    if angle is None:
        return None
    if not Token.CURRENT_CONTEXT:
        return angle
    if not (-360 < angle < 360):
        angle %= 360
    is_pad_or_text = Token.CURRENT_CONTEXT and (Token.CURRENT_CONTEXT[-1] in (Pad, FpText))
    if is_pad_or_text and (-180 < angle <= 360):  # noqa: SIM114
        return angle
    elif not is_pad_or_text and (-180 < angle <= 180):
        return angle
    else:
        sign = 1 if angle > 0 else -1
        return angle % (360 * -sign)


def angle_key(angle: float | None) -> float | None:
    if angle is None:
        return None
    if not (-360 < angle < 360):
        angle %= 360
    if -180 < angle <= 180:
        return float_key(angle)
    else:
        sign = 1 if angle > 0 else -1
        return float_key(angle % (360 * -sign))


@define(field_transformer=ensure_metadata)
class At(Xy):
    angle: float | int | None = token_field(
        default=None,
        eq=angle_key,
        converter=angle_normalizer,
        on_setattr=attrs.setters.convert,
    )
    unlocked: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Start(Xy):
    pass


@define(field_transformer=ensure_metadata)
class Mid(Xy):
    pass


@define(field_transformer=ensure_metadata)
class Center(Xy):
    pass


@define(field_transformer=ensure_metadata)
class End(Xy):
    pass


@define(field_transformer=ensure_metadata)
class Size(Xy):
    pass


# Interferes with Model.offset who is just a named XYZ
# @define(field_transformer=ensure_metadata)
# class Offset(XY):
#     pass


@define(field_transformer=ensure_metadata)
class Color(Token):
    r: float | int
    g: float | int
    b: float | int
    a: float | int


@define(field_transformer=ensure_metadata)
class Stroke(Token):
    class StrokeType(Enum):
        dash = 'dash'
        dash_dot = 'dash_dot'
        dash_dot_dot = 'dash_dot_dot'
        dot = 'dot'
        default = 'default'
        solid = 'solid'

    width: float | int = named_field()
    type: StrokeType = named_field(converter=StrokeType)
    color: Color | None = None


@define(field_transformer=ensure_metadata)
class GraphicItem(Token):
    """A base token class usable to group all graphic items."""


@define(field_transformer=ensure_metadata)
class Font(Token):
    face: str | None = named_field(default=None)
    size: Size = REQUIRED
    thickness: float | int | None = named_field(default=None)
    bold: bool = literal_field()
    italic: bool = literal_field()
    line_spacing: float | int | None = named_field(default=None)


@define(field_transformer=ensure_metadata)
class Justify(Token):
    # TODO: Redo by supporting Literal[this, that]
    left: bool = literal_field()
    right: bool = literal_field()
    top: bool = literal_field()
    bottom: bool = literal_field()
    mirror: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Effects(Token):
    font: Font
    justify: Justify | None = None
    hide: bool = literal_field()


@define(field_transformer=ensure_metadata)
class GrText(GraphicItem):
    text: str
    at: At
    layer: str = named_field()  # NB: Not supporting knockout...
    tstamp: uuid.UUID = uuid_field(newlines='()\n')
    effects: Effects = token_field(newlines='()\n')


@define(field_transformer=ensure_metadata)
class FpText(GraphicItem):
    class FpTextType(Enum):
        reference = 'reference'
        value = 'value'
        user = 'user'

    type: FpTextType = token_field(converter=FpTextType)  # noqa: A003
    text: str = REQUIRED
    at: At = REQUIRED
    layer: str = named_field()
    hide: bool = literal_field()
    effects: Effects = token_field(newlines='\n()\n', indent=True)
    tstamp: uuid.UUID = uuid_field(newlines='()\n')

    def is_ref(self) -> bool:
        return self.type == FpText.FpTextType.reference

    def is_value(self) -> bool:
        return self.type == FpText.FpTextType.value

    def is_user(self) -> bool:
        return self.type == FpText.FpTextType.user


@define(field_transformer=ensure_metadata)
class FpTextBox(GraphicItem):
    data: dict[str, Any]


@define(field_transformer=ensure_metadata)
class Line:
    """Base definition of a line defined by 2 points.

    Used not only to declare the various flavours and version of line tokens.
    But also to provide some math-related methods.
    """

    start: Xy
    end: Xy

    @property
    def center(self) -> Xy:
        """Returns the center point of the line."""

        return (self.start + self.end) / 2

    def translate(self, vector: Xy) -> Self:
        """Returns a new line being this line translated by the provided vector."""

        return type(self)(
            start=self.start + vector,
            end=self.end + vector,
        )

    def rotate_90deg(self) -> Self:
        """Returns a new line rotated by 90 degrees around 0."""

        return type(self)(
            start=Xy(x=-self.start.y, y=self.start.x),
            end=Xy(x=-self.end.y, y=self.end.x),
        )

    def intersect(self, other: Line) -> Xy:
        """Returns the intersection point between two lines (even if the point is virtually
        not on the lines, ie. not on the line segments limited by the start and end points)."""

        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        x3, y3 = other.start.x, other.start.y
        x4, y4 = other.end.x, other.end.y

        x1y2_y1x2 = (x1 * y2) - (y1 * x2)
        x3y4_y3x4 = (x3 * y4) - (y3 * x4)
        denominator = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        return Xy(
            x=((x1y2_y1x2 * (x3 - x4)) - ((x1 - x2) * x3y4_y3x4)) / denominator,
            y=((x1y2_y1x2 * (y3 - y4)) - ((y1 - y2) * x3y4_y3x4)) / denominator,
        )


@define(field_transformer=ensure_metadata)
class Line_20171130(Line):
    angle: float | int = named_field(eq=float_key)
    layer: str = named_field()
    width: float | int = named_field()

    def to_20221018(self, target_cls: type[Line_20221018]) -> Line_20221018:
        return target_cls(
            start=self.start,
            end=self.end,
            angle=self.angle if self.angle != 90 else None,
            stroke=Stroke(width=self.width, type=Stroke.StrokeType.solid),
            layer=self.layer,
            tstamp=uuid.uuid4(),
        )


@define(field_transformer=ensure_metadata)
class Line_20221018(Line):
    angle: float | int | None = token_field(default=None, eq=float_key)
    stroke: Stroke = token_field(newlines='\n()')
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field()


@define(field_transformer=ensure_metadata)
class FpLine(GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class FpLine_20171130(FpLine, Line_20171130):
    pass


@define(field_transformer=ensure_metadata)
class FpLine_20221018(FpLine, Line_20221018):
    pass


@define(field_transformer=ensure_metadata)
class GrLine(GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class GrLine_20171130(GrLine, Line_20171130):
    pass


@define(field_transformer=ensure_metadata)
class GrLine_20221018(GrLine, Line_20221018):
    pass


@define(field_transformer=ensure_metadata)
class Rect:
    class FillType(Enum):
        none = 'none'
        solid = 'solid'

    start: Start
    end: End
    stroke: Stroke = token_field(newlines='\n()')
    fill: FillType | None = named_field(default=None, converter=FillType)
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field()


@define(field_transformer=ensure_metadata)
class FpRect(Rect, GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class GrRect(Rect, GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class FpCircle(GraphicItem):
    class FillType(Enum):
        none = 'none'
        solid = 'solid'

    center: Center
    end: End
    stroke: Stroke = token_field(newlines='\n()')
    fill: FillType | None = named_field(default=None, converter=FillType)
    locked: bool = literal_field()
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field()


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
    def center(self) -> Xy:
        """Center of the arc circle."""

        raise NotImplementedError

    @property
    def radius(self) -> float:
        """Radius of the arc circle."""

        return self.end.dist(self.center)

    @property
    def end_angle(self) -> float:
        """Returns the angle (in radian) formed between the end point and the virtual zero point."""

        relative_end = (self.end - self.center) / self.radius
        return math.atan2(relative_end.y, relative_end.x)

    def point_at(self, angle: float) -> Xy:
        """Returns the point on the arc circle at the given angle from the virtual zero point."""

        return Xy(
            x=self.center.x + (self.radius * math.cos(angle)),
            y=self.center.y + (self.radius * math.sin(angle)),
        )


@define(field_transformer=ensure_metadata)
class Arc_20171130(Arc):
    start: Start  # It is the center point actually
    end: End
    angle: float | int = named_field(eq=angle_key, converter=angle_normalizer)
    layer: str = named_field()
    width: float | int = named_field()

    @property
    def center(self) -> Xy:
        return self.start.cast_to(Xy)

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


@define(field_transformer=ensure_metadata)
class Arc_20221018(Arc):
    start: Start
    mid: Mid
    end: End
    stroke: Stroke = token_field(newlines='\n()')
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field()

    @property
    def center(self) -> Xy:
        """Center of the arc circle.

        This version of arc does not hold the center point information.
        Instead, we have to recalculate it, using chords defined by the three
        start, middle, and end points.
        """
        sm = Line(start=self.start, end=self.mid)
        sm_chord = sm.translate(-sm.center).rotate_90deg().translate(sm.center)

        me = Line(start=self.mid, end=self.end)
        me_chord = me.translate(-me.center).rotate_90deg().translate(me.center)

        return sm_chord.intersect(me_chord).cast_to(Xy)


@define(field_transformer=ensure_metadata)
class FpArc(GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class FpArc_20171130(FpArc, Arc_20171130):
    pass


@define(field_transformer=ensure_metadata)
class FpArc_20221018(FpArc, Arc_20221018):
    pass


@define(field_transformer=ensure_metadata)
class GrArc(GraphicItem):
    pass


@define(field_transformer=ensure_metadata)
class GrArc_20171130(GrArc, Arc_20171130):
    pass


@define(field_transformer=ensure_metadata)
class GrArc_20221018(GrArc, Arc_20221018):
    pass


@define(field_transformer=ensure_metadata)
class Pts(Token):
    list_: list[Xy] = token_field(newlines='\n[()\n]')

    def newlines_filter(
        self,
        field: attrs.Attribute[Any] | None,
        value: Any | None,
        newlines: dict[str, bool],
    ) -> dict[str, bool]:
        if not field:  # Init
            return newlines
        if Token.CURRENT_CONTEXT[-2] is not Dimension:
            return newlines

        newlines['before_first'] = False
        newlines['after'] = False
        return newlines


@define(field_transformer=ensure_metadata)
class FpPoly(GraphicItem):
    class FillType(Enum):
        none = 'none'
        solid = 'solid'

    points: Pts = token_field(newlines='\n()\n')
    stroke: Stroke = token_field(newlines='\n()')
    fill: FillType | None = named_field(default=None, converter=FillType)
    locked: bool = literal_field()
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field()


@define(field_transformer=ensure_metadata)
class Format(Token):
    prefix: str | None = named_field(default=None)
    suffix: str | None = named_field(default=None)
    units: int = named_field()
    units_format: int = named_field()
    precision: int = named_field()
    override_value: str | None = named_field(default=None)
    suppress_zeros: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Style(Token):
    thickness: float | int = named_field()
    arrow_length: float | int = named_field()
    text_position_mode: int = named_field()
    extension_height: float | int | None = named_field(default=None)
    text_frame: int | None = named_field(default=None)
    extension_offset: float | int | None = named_field(default=None)
    keep_text_aligned: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Dimension(GraphicItem):
    class Type(Enum):
        aligned = 'aligned'
        leader = 'leader'
        center = 'center'
        orthogonal = 'orthogonal'
        radial = 'radial'

    locked: bool = literal_field()
    type: Type = named_field(converter=Type)
    layer: str = named_field()
    tstamp: uuid.UUID = uuid_field(newlines='()\n')
    points: Pts = token_field(newlines='()\n')
    height: float | int | None = named_field(default=None)
    orientation: float | int | None = named_field(default=None)
    leader_length: float | int | None = named_field(default=None)
    text: GrText | None = token_field(default=None, newlines='\n()')
    format: Format | None = token_field(default=None, newlines='\n()')
    style: Style = token_field(newlines='\n()\n')


@define(field_transformer=ensure_metadata)
class Drill(Token):
    oval: bool = literal_field()
    diameter: float | int = REQUIRED
    width: float | int | None = None
    # offset: Offset | None = None  # Interferes with Model.offset...


@define(field_transformer=ensure_metadata)
class Chamfer(Token):
    top_left: bool = literal_field()
    top_right: bool = literal_field()
    bottom_left: bool = literal_field()
    bottom_right: bool = literal_field()


@define(field_transformer=ensure_metadata)
class Pad(Token):
    class Type(Enum):
        thru_hole = 'thru_hole'
        smd = 'smd'
        connect = 'connect'
        np_thru_hole = 'np_thru_hole'

    class Shape(Enum):
        circle = 'circle'
        rect = 'rect'
        oval = 'oval'
        trapezoid = 'trapezoid'
        roundrect = 'roundrect'
        custom = 'custom'

    number: str
    type: Type = token_field(converter=Type)
    shape: Shape = token_field(converter=Shape)
    at: At = REQUIRED
    locked: bool = literal_field()
    size: Size = REQUIRED
    drill: Drill | None = None
    layers: Layers = REQUIRED
    # properties: Property | None = None
    remove_unused_layer: bool = literal_field()
    keep_end_layers: bool = literal_field()
    roundrect_rratio: float | int | None = named_field(default=None)
    chamfer_ratio: float | int | None = named_field(default=None, metadata=dict(opt_group=1))
    chamfer: Chamfer | None = named_field(default=None, metadata=dict(opt_group=1))
    net: Net | None = token_field(default=None, eq=False, metadata=dict(opt_group=2))
    pinfunction: str | None = named_field(default=None, eq=False, metadata=dict(opt_group=2))
    pintype: str | None = named_field(default=None, eq=False, metadata=dict(opt_group=2))
    die_length: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    solder_mask_margin: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    solder_paste_margin: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    solder_paste_margin_ratio: float | int | None = named_field(
        default=None, metadata=dict(opt_group=2)
    )
    clearance: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    zone_connect: int | None = named_field(default=None, metadata=dict(opt_group=2))
    thermal_bridge_width: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    thermal_gap: float | int | None = named_field(default=None, metadata=dict(opt_group=2))
    tstamp: uuid.UUID = uuid_field()
    # TODO: Custom options and primitives

    def newlines_filter(
        self,
        field: attrs.Attribute[Any] | None,
        value: Any | None,
        newlines: dict[str, bool],
    ) -> dict[str, bool]:
        if not field:  # Init
            newlines['opt_group1'] = False
            newlines['opt_group2'] = False
            return newlines

        if value is None:
            return newlines

        opt_group = field.metadata.get('opt_group', None)
        if opt_group is None:
            return newlines

        opt_group_key = f'opt_group{opt_group}'
        if newlines[opt_group_key] is False:
            newlines['before'] = True
            newlines[opt_group_key] = True

        return newlines


@define(field_transformer=ensure_metadata)
class Model(Token):
    file: str
    hide: bool | None = literal_field(default=None)
    offset: Xyz = named_field(newlines='\n()\n')
    scale: Xyz = named_field(newlines='()\n')
    rotate: Xyz = named_field(newlines='()\n')


@define(field_transformer=ensure_metadata)
class Segment(Token):
    start: Start
    end: End
    width: float | int = named_field()
    layer: str = named_field()
    locked: bool | None = literal_field(default=None)
    net: Net = REQUIRED
    tstamp: uuid.UUID = uuid_field()


@define(field_transformer=ensure_metadata)
class Hatch(Token):
    class HatchStyle(Enum):
        none = 'none'
        edge = 'edge'
        full = 'full'

    style: HatchStyle = token_field(converter=HatchStyle)
    pitch: float | int = REQUIRED


@define(field_transformer=ensure_metadata)
class ConnectPads(Token):
    class ConnectionType(Enum):
        thru_hole_only = 'thru_hole_only'
        full = 'full'
        no = 'no'

    connection_type: ConnectionType | None = token_field(
        default=None, converter=lambda value: ConnectPads.ConnectionType(value) if value else None
    )
    clearance: float | int = named_field()


@define(field_transformer=ensure_metadata)
class Keepout(Token):
    class KeepoutType(Enum):
        allowed = 'allowed'
        not_allowed = 'not_allowed'

    tracks: KeepoutType = named_field(converter=KeepoutType)
    vias: KeepoutType = named_field(converter=KeepoutType)
    pads: KeepoutType = named_field(converter=KeepoutType)
    copperpour: KeepoutType = named_field(converter=KeepoutType)
    footprints: KeepoutType = named_field(converter=KeepoutType)


@define(field_transformer=ensure_metadata)
class Polygon(Token):
    points: Pts = token_field(newlines='\n()\n')


@define(field_transformer=ensure_metadata)
class FilledPolygon(Token):
    layer: str = named_field(newlines='\n()\n')
    points: Pts = token_field(newlines='()\n')


@define(field_transformer=ensure_metadata)
class Zone(Token):
    net: Net
    net_name: str = named_field()
    layer: str | None = named_field(default=None)
    layers: Layers | None = None
    tstamp: uuid.UUID = uuid_field()
    name: str | None = named_field(default=None)
    hatch: Hatch = token_field(newlines='()\n')
    priority: int | None = named_field(default=None)
    connect_pads: ConnectPads = token_field(newlines='()\n')
    min_thickness: float | int = named_field()
    filled_areas_thickness: str | None = named_field(default=None, quoted=False, newlines='()\n')
    keepout: Keepout | None = None
    fill: dict[str, Any] | None = named_field(newlines='[()]\n')
    polygon: Polygon = token_field(newlines='()\n')
    filled_polygons: list[FilledPolygon] | None = token_field(default=None, newlines='()\n')


@define(field_transformer=ensure_metadata)
class FpLibTable(Token):
    version: Version = token_field(newlines='\n()\n')
    libs: list[Lib] = token_field(newlines='()\n')


@define(field_transformer=ensure_metadata)
class Footprint(Token):
    """Token for a .kicad_mod file."""

    name: str  # Aka library_link when placed in a PCB

    # In .kicad_mod only
    version: Version | None = None
    generator: str | None = named_field(default=None, quoted=False, newlines='()\n')

    # In .kicad_pcb only
    locked: bool | None = literal_field(default=None)
    placed: bool | None = literal_field(default=None)

    layer: str = named_field(newlines='()\n')

    # In .kicad_pcb only
    tstamp: uuid.UUID | None = uuid_field(default=None, newlines='()\n')
    at: At | None = token_field(default=None, newlines='()\n')

    descr: str | None = named_field(default=None, newlines='()\n')
    tags: str | None = named_field(default=None, newlines='()\n')
    properties: list[Property] | None = token_field(default=None, newlines='()\n')
    path: str | None = named_field(default=None, newlines='()\n')
    # Covers things like attr, property, path, ...
    settings: dict[str, Any] = token_field(newlines='()\n')

    graphic_items: list[GraphicItem] = token_field(newlines='()\n')
    # pads: list[Pad] | None = token_field(default=None, newlines='()\n')
    # models: list[Model] | None = token_field(default=None, newlines='()\n')
    pads: list[Pad] = token_field(newlines='()\n')
    models: list[Model] = token_field(newlines='()\n')
    data: list[Token | list] = token_field(newlines='()\n')

    def find_item[T: Token](self, type_: type[T] = Token, **fields: Any) -> T | None:
        for graphic_item in self.graphic_items:
            if not isinstance(graphic_item, type_):
                continue
            if graphic_item.match(**fields):
                return graphic_item
        return None

    def add_on_pcb(self, pcb: KicadPcb, lib: str, ref: str | None, at: At) -> None:
        footprint = deepcopy(self)
        footprint.name = f'{lib}:{footprint.name}'
        footprint.version = None
        footprint.generator = None
        footprint.tstamp = uuid.uuid4()
        footprint.at = at
        if ref:
            ref_text = footprint.find_item(FpText, type=FpText.FpTextType.reference)
            if ref_text:
                ref_text.text = ref

        for item in chain(footprint.graphic_items, footprint.pads, footprint.models):
            if hasattr(item, 'tstamp'):
                item.tstamp = uuid.uuid4()
            if at.angle and hasattr(item, 'at'):
                if item.at.angle is None:
                    item.at.angle = 0
                item.at.angle += at.angle

        pcb.footprints.append(footprint)

    def update_from(
        self,
        model: Footprint,
        new_angle: float,
        *,
        settings: bool = True,
        texts: bool = True,
    ) -> None:
        ref = None
        if texts:
            ref_text = self.find_item(FpText, type=FpText.FpTextType.reference)
            if ref_text:
                ref = ref_text.text

        if settings:
            self.settings = deepcopy(model.settings)

        old_angle = self.at.angle or 0
        angle_changed = abs(old_angle - new_angle) >= 1e-6

        def update_angle(item: GraphicItem) -> GraphicItem:
            if angle_changed and hasattr(item, 'at'):
                if item.at.angle is None:
                    item.at.angle = 0
                item.at.angle -= old_angle
                item.at.angle += new_angle
                if not item.at.angle:
                    item.at.angle = None
            return item

        def update_items(collection_name: str) -> None:
            old_items: list[Token] = getattr(self, collection_name)
            new_items: list[Token] = []
            setattr(self, collection_name, new_items)

            if not texts and old_items:
                for item in old_items:
                    if isinstance(item, FpText):
                        with FpText.as_context():
                            new_items.append(update_angle(item))

            for item in getattr(model, collection_name):
                if isinstance(item, FpText) and not texts:
                    continue

                new_item = deepcopy(item)
                if hasattr(new_item, 'tstamp'):
                    item.tstamp = uuid.uuid4()
                if (ref is not None) and isinstance(new_item, FpText) and new_item.is_ref():
                    new_item.text = ref

                with type(new_item).as_context():
                    if old_angle and hasattr(new_item, 'at'):
                        if new_item.at.angle is None:
                            new_item.at.angle = 0
                        new_item.at.angle += old_angle

                    if not old_items:
                        new_items.append(update_angle(new_item))
                    elif old_items[-1] == new_item:
                        new_items.append(update_angle(old_items.pop()))
                    else:
                        try:
                            index = old_items.index(new_item)
                        except ValueError:
                            new_items.append(update_angle(new_item))
                        else:
                            new_items.append(update_angle(old_items.pop(index)))

        update_items('graphic_items')
        update_items('pads')
        update_items('models')


@define(kw_only=True, field_transformer=ensure_metadata)
class KicadPcb(Token):
    """Token for a .kicad_pcb file."""

    version: Version
    generator: str = named_field(newlines='()\n', quoted=False)
    general: General = token_field(newlines='\n()\n')
    paper: Paper | Page = token_field(newlines='\n()\n')
    title_block: TitleBlock | None = None
    layers: Layers = token_field(newlines='()\n')
    setup: Setup = token_field(newlines='\n()\n')
    # properties
    nets: list[Net] = token_field(newlines='\n[()\n]')
    net_classes: list[NetClass] | None = None  # Old versions
    footprints: list[Footprint] | None = token_field(newlines='\n()\n')
    graphic_items: list[GraphicItem] = token_field(newlines='\n[()\n]')
    segments: list[Segment] = token_field(newlines='\n[()\n]')
    zones: list[Zone] = token_field(newlines='\n[()\n]')
    data: list[Token | list] = token_field(newlines='[\n()\n]')

    def newlines_filter(
        self,
        field: attrs.Attribute[Any] | None,
        value: Any | None,
        newlines: dict[str, bool],
    ) -> dict[str, bool]:
        if not field:  # Init
            newlines['at_end'] = True
            return newlines

        if not value:
            return newlines

        if field.name in ('segments', 'zones'):
            newlines['at_end'] = False

        return newlines

    @classmethod
    def from_sexpr_data(cls, args: list[Self | str | Number]) -> Self:
        if args[1][0] == 'host':  # Older host variant of generator
            args[1] = ['generator', ' '.join(args[1][1:])]

        return super().from_sexpr_data(args)

    def find_ref[T: Token](self, ref: str, type_: type[T] = Token) -> T | None:
        if issubclass(type_, Footprint) or (type_ is Token):
            for footprint in self.footprints:
                ref_field = footprint.find_item(FpText, type=FpText.FpTextType.reference)
                if ref_field is None:
                    continue
                if ref_field.text == ref:
                    return footprint

        return None


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
            layer='F.Cu',
            settings=dict(attr=['board_only', 'exclude_from_pos_files', 'exclude_from_bom']),
            graphic_items=[
                FpText(
                    type=FpText.FpTextType.reference,
                    text='REF**',
                    at=At(x=0, y=-0.5, unlocked=True),
                    layer='F.SilkS',
                    hide=True,
                    effects=Effects(
                        font=Font(size=Size(x=1, y=1), thickness=0.1),
                    ),
                    tstamp=uuid.uuid4(),
                ),
                FpText(
                    type=FpText.FpTextType.value,
                    text=name,
                    at=At(x=0, y=1, unlocked=True),
                    layer='F.Fab',
                    hide=True,
                    effects=Effects(
                        font=Font(size=Size(x=1, y=1), thickness=0.15),
                    ),
                    tstamp=uuid.uuid4(),
                ),
            ],
            data=[],
        )
        old_items = []
    else:
        footprint = deepcopy(existing_footprint)
        old_items = []
        kept_items = []
        for item in footprint.graphic_items:
            if isinstance(item, FpText) and (
                item.type in (FpText.FpTextType.reference, FpText.FpTextType.value)
            ):
                kept_items.append(item)
            else:
                old_items.append(item)
        footprint.graphic_items = kept_items

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

    # Tries hard to keep original corresponding items to avoid needless tstamp change
    old_items = list(reversed(old_items))
    for item in sorted(pcb.graphic_items, key=sorting_key):
        fp_item = item.to_version(version).to_footprint()

        # Filter out buggy ergogen arcs and lines that ends on the same point than it starts.
        # In case of arcs, due to rounding in newer versions of KiCad, it displays them
        # as full circles.
        # And in cases of lines if can make an Edge.Cut non-manifold (or even weirder, inverted).
        if isinstance(fp_item, (FpLine, FpArc)) and (fp_item.start == fp_item.end.cast_to(Start)):
            continue

        if not old_items:
            footprint.graphic_items.append(fp_item)
        elif old_items[-1] == fp_item:
            footprint.graphic_items.append(old_items.pop())
        else:
            try:
                index = old_items.index(fp_item)
            except ValueError:
                footprint.graphic_items.append(fp_item)
            else:
                footprint.graphic_items.append(old_items.pop(index))

    return footprint


@kicad_cli.command('parse')
def cli_parse(
    filename: Path,
    reexport: Optional[Path] = None,
    do_print: bool = True,
    as_list: bool = False,
    as_text: bool = False,
    profile: bool = False,
) -> None:
    if profile:
        import cProfile

        # All of parsing
        # cProfile.runctx('Token.from_file(filename)', locals(), globals(), 'parsing.stats')

        # Just the SParser
        # cProfile.runctx('SParser.parse(filename)', globals(), locals(), 'parsing.stats')

        # Just the reifier
        # content = SParser.parse(filename)
        # cProfile.runctx('Token.from_sexpr(content)', locals(), globals(), 'parsing.stats')

        # Export
        obj = Token.from_file(filename)
        print(f'Loaded a {type(obj).__name__}')
        cProfile.runctx('obj.to_sexpr_text()', globals(), locals(), 'exporting.stats')

        return

    with ProgressContext():
        obj = Token.from_file(filename)
        print(f'Loaded a {type(obj).__name__}')

        if do_print:
            print('>>>', obj)
        if as_list:
            print('>>>', obj.to_sexpr_list())
        if as_text:
            print('>>>', obj.to_sexpr_text())

        if reexport:
            print('Exporting...')
            obj.to_file(reexport)


@kicad_cli.command('convert-pcb-to-footprint')
def cli_convert_pcb_to_footprint(
    pcb_path: Path,
    footprint_path: Path,
) -> None:
    with ProgressContext():
        name = pcb_path.stem
        pcb = KicadPcb.from_file(pcb_path)

        footprint = None
        if (footprint_path.suffix == '.kicad_mod') and footprint_path.exists():
            footprint = Footprint.from_file(footprint_path)

        footprint = convert_pcb_to_footprint(pcb, name, 'ergogen_keebs', footprint)

        if footprint_path.suffix == '.pretty':
            footprint_path /= f'{name}.kicad_mod'
        footprint_path.parent.mkdir(exist_ok=True)
        footprint.to_file(footprint_path)


@kicad_cli.command('update-fabrication-files')
def cli_update_fabrication_files(
    ergogen_yaml: Path,
    points_yaml: Annotated[Optional[Path], clyo.Option()] = None,  # noqa: UP007
    units_yaml: Annotated[Optional[Path], clyo.Option()] = None,  # noqa: UP007
    project: Annotated[Optional[str], clyo.Option()] = None,  # noqa: UP007
) -> None:
    from ergogen import Keyboard

    with StatusContext() as status, ProgressContext():
        keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)

        if project:
            _update_project(keeb, keeb.fabrication[project])
        else:
            for project_name, project_data in keeb.fabrication.items():
                status.update(f'Updating for {project_name}')
                _update_project(keeb, project_data)

        status.update('Done')


def _update_project(
    keeb: Keyboard,
    project: dict[str, dict[str, dict[str, str]]],
) -> None:
    project_folder = Path(project['folder'])
    if not project_folder.exists():
        msg = f'KiCad project folder "{project_folder!s}" does not exist'
        raise ValueError(msg)
    project_name: str = project['project-name']
    project_file_stem = project_folder / project_name
    pcb_path = project_file_stem.with_suffix('.kicad_pcb')
    pcb: KicadPcb | None = None

    # TODO: Load paths from user config (~/.config/kicad/<version?>/kicad_common.json)
    #       and find a way to get system paths
    paths = dict(KIPRJMOD=str(project_folder))

    fp_lib_table, ergogen_lib = _ergogen_lib_info(
        project_folder, project.get('ergogen-lib-name', 'Ergogen')
    )
    ergogen_lib_path = Path(ergogen_lib.uri.replace('${KIPRJMOD}', str(project_folder)))

    for obj in project['objects']:
        if 'outline' in obj:
            StatusContext().update(f'Updating outline {obj["outline"]}')
            # First, convert the outline as footprint
            source_path = Path(f'ergogen-output/pcbs/{obj["outline"]}.kicad_pcb')
            target_path = ergogen_lib_path / f'{obj["outline"]}.kicad_mod'

            source_pcb = KicadPcb.from_file(source_path)
            target_footprint = Footprint.from_file(target_path) if target_path.exists() else None

            target_footprint = convert_pcb_to_footprint(
                source_pcb,
                obj['outline'],
                generator='ergogen',
                existing_footprint=target_footprint,
            )

            target_path.parent.mkdir(exist_ok=True)
            target_footprint.to_file(target_path)

            # Second, add/update on the PCB
            if pcb is None:
                pcb = KicadPcb.from_file(pcb_path)

            with Footprint.as_context():
                position = At(0, 0)
                if 'offset' in project:
                    position += At(*project['offset'])
                if 'offset' in obj:
                    position += At(*obj['offset'])

            outline_fp = pcb.find_ref(obj['ref'], Footprint) if 'ref' in obj else None
            if outline_fp is None:
                target_footprint.add_on_pcb(
                    pcb, lib=ergogen_lib.name, ref=obj.get('ref', None), at=position
                )
            else:
                outline_fp.update_from(target_footprint, 0)
                outline_fp.at = position

        elif 'keys' in obj:
            StatusContext().update('Updating keys')
            if pcb is None:
                pcb = KicadPcb.from_file(pcb_path)

            for spec in obj['keys']:
                do_keys(keeb, project, fp_lib_table, paths, pcb, spec)

    if pcb is not None:
        StatusContext().update('Writing PCB file')
        pcb.to_file(pcb_path)


def footprint_from_lib(
    fp_lib_table: FpLibTable, paths: dict[str, str], name: str
) -> Footprint | None:
    # TODO: Also lookup in user config (~/.config/kicad/<version?>/fp-lib-table)
    lib_name, footprint_name = name.split(':', maxsplit=1)

    for lib in fp_lib_table.libs:
        if lib.name == lib_name:
            break
    else:
        msg = f'Library {lib_name} not found in fp-lib-table!'
        raise ValueError(msg)

    lib_path = Path(re.sub(r'\$\{([a-zA-Z0-9_]+)\}', r'{\1}', lib.uri).format(**paths))
    footprint_path = lib_path / f'{footprint_name}.kicad_mod'

    return Footprint.from_file(footprint_path) if footprint_path.exists() else None


class AttrDict(dict[str, Any]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = type(self)(value)

    def __getattr__(self, key: str) -> Any:
        try:
            return self[key]
        except KeyError as ex:
            raise AttributeError(key) from ex


def do_keys(
    keeb: Keyboard,
    project: dict[str, dict[str, dict[str, str]]],
    fp_lib_table: FpLibTable,
    paths: dict[str, str],
    pcb: KicadPcb,
    spec: dict[str, Any],
) -> None:
    wheres = spec.get('where', None)
    if wheres:
        if not isinstance(wheres, list):
            wheres = [wheres]
        wheres = [
            re.sub(r'([a-zA-Z0-9_.-]+)', r'{\1}', where.replace('~', '==')) for where in wheres
        ]

    def match_wheres(point: dict[str, Points.ElementData]) -> tuple[bool, AttrDict | None]:
        if not wheres:
            return True, None

        attribs = AttrDict(point['original'])
        for where in wheres:
            try:
                locs = dict(
                    true=True,
                    false=False,
                    horizontal='horizontal',
                    vertical='vertical',
                )
                point_where = where.format(**locs, **attribs)
            except AttributeError:
                return False, attribs
            if not eval(point_where, None, locs):
                return False, attribs

        return True, attribs

    footprint = footprint_from_lib(fp_lib_table, paths, spec['footprint'])
    lib_name, _ = spec['footprint'].split(':', maxsplit=1)

    for point in keeb.points:
        match, attribs = match_wheres(point)
        if not match:
            continue
        if attribs is None:
            attribs = AttrDict(point['original'])
        ref = spec['ref'].format(**attribs)

        StatusContext().update(f'Updating key {point["name"]} ({ref=})')

        with Footprint.as_context():
            position = At(attribs.x, -attribs.y)
            if 'offset' in project:
                position += At(*project['offset'])
            if 'offset' in spec:
                position += At(*spec['offset'])
            angle = attribs.r + spec.get('angle', 0)
            position.angle = angle if angle else None

        pcb_footprint = pcb.find_ref(ref, Footprint)
        if pcb_footprint is None:
            _logger.info(f'Adding {point["name"]} at pos={position} with {ref=}')
            footprint.add_on_pcb(pcb, lib=lib_name, ref=ref, at=position)
        else:
            _logger.info(f'Updating {point["name"]} at pos={position} with {ref=}')
            pcb_footprint.update_from(footprint, angle)
            pcb_footprint.at = position
            pcb_footprint.name = f'{lib_name}:{footprint.name}'


def _ergogen_lib_info(project_folder: Path, name: str = 'Ergogen') -> tuple[FpLibTable, Lib]:
    def make_ergogen_lib() -> Lib:
        return Lib(
            name=name,
            type=Lib.LibType.KiCad,
            uri='${KIPRJMOD}/' + f'{name}.pretty',
            options='',
            descr='',
        )

    fp_lib_table_path = project_folder / 'fp-lib-table'
    if fp_lib_table_path.exists():
        fp_lib_table = FpLibTable.from_file(fp_lib_table_path)
        for lib in fp_lib_table.libs:
            if lib.name == name:
                ergogen_lib = lib
                break
        else:
            ergogen_lib = make_ergogen_lib()
            fp_lib_table.libs.append(ergogen_lib)
            fp_lib_table.to_file(fp_lib_table_path)
    else:
        ergogen_lib = make_ergogen_lib()
        fp_lib_table = FpLibTable(version=Version(version=7), libs=[ergogen_lib])
        fp_lib_table.to_file(fp_lib_table_path)

    return fp_lib_table, ergogen_lib
