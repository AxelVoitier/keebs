# Copyright (c) 2023 Axel Voitier
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words
# spell-checker:ignore
''''''
from __future__ import annotations

# System imports
import logging
import re
from collections import OrderedDict
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Optional

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import TypeAlias, Any

# Third-party imports
import hiyapyco
try:
    from clyo import ClyoTyper, Argument, Option
except ImportError:
    from typer import Typer as ClyoTyper, Argument, Option
from rich import print
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

# Local imports

_logger = logging.getLogger(__name__)


class Points:

    if TYPE_CHECKING:
        ElementData: TypeAlias = Any

    def __init__(self, filepath: Path, keyboard: Keyboard) -> None:
        self.filepath = filepath
        self._data: dict[str, Points.ElementData] | None = None
        self._keyboard = keyboard

    @property
    def data(self) -> dict[str, Points.ElementData]:
        if (data := self._data) is None:
            with self.filepath.open() as f:
                data = self._data = yaml.load(f, Loader=Loader)

        return data

    def __iter__(self) -> Iterator[dict[str, int | float]]:
        offset_x, offset_y = self._keyboard.general_offset
        for k, v in self.data.items():
            if not (tags := v['meta']['tags']):
                continue
            if ('1u' not in tags) and ('1-5u' not in tags) and ('2u' not in tags):
                continue

            yield dict(
                x=v['x'] - offset_x, y=v['y'] - offset_y, r=v['r'], name=k,
                width=v['meta']['width'], height=v['meta']['height'],
                layers=v['meta'].get('layers', {})
            )


class Units:

    if TYPE_CHECKING:
        ElementData: TypeAlias = int | float

    RE_MULT = re.compile(
        r'((?:[0-9]*\.[0-9]+)|(?:[0-9]+\.[0-9]*)|(?:[0-9]+)|(?:\(.*?\)))([a-zA-Z_][a-zA-Z0-9_]*)')

    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        self._data: dict[str, Units.ElementData] | None = None

    @property
    def data(self) -> dict[str, Units.ElementData]:
        if (data := self._data) is None:
            with self.filepath.open() as f:
                data = self._data = yaml.load(f, Loader=Loader)

        return data

    def eval(self, value: str) -> str | float | int:
        try:
            return eval(self.RE_MULT.sub(r'(\1*\2)', value), None, self.data)
        except Exception:
            return value


class Keyboard:

    if TYPE_CHECKING:
        ElementData: TypeAlias = str | float | int | list['ElementData'] | dict[str, 'ElementData']

    def __init__(self, filepath: Path) -> None:
        self.filepath = filepath
        self._data: dict[str, Keyboard.ElementData] | None = None
        self._points: Points | None = None
        self._units: Units | None = None

    @property
    def data(self) -> dict[str, Keyboard.ElementData]:
        if (data := self._data) is None:
            with self.filepath.open() as f:
                data = self._data = self._preprocess(yaml.load(f, Loader=Loader))

        return data

    def _preprocess(self, data: dict[str, Keyboard.ElementData]) -> dict[str, Keyboard.ElementData]:
        data = self._unnest(data)
        # TODO: Inheritance
        # TODO: Parametrization
        # TODO: Skipping
        data = self._expand_units(data)

        return data

    @classmethod
    def _unnest(cls, data: dict[str, Keyboard.ElementData]) -> dict[str, Keyboard.ElementData]:
        # print(f'> unnest: {data=} (type={type(data)})')
        if not isinstance(data, dict):
            return data

        def handle_dict_and_list(value: Keyboard.ElementData) -> Keyboard.ElementData:
            if isinstance(value, dict):
                return cls._unnest(value)
            elif isinstance(value, list):
                return [handle_dict_and_list(item) for item in value]
            else:
                return value

        def recursive_update(
            dict1: dict[str, Keyboard.ElementData],
            dict2: dict[str, Keyboard.ElementData],
        ) -> dict[str, Keyboard.ElementData]:
            for k, v in dict2.items():
                if isinstance(v, dict):
                    dict1[k] = recursive_update(dict1.get(k, OrderedDict()), v)
                else:
                    dict1[k] = v
            return dict1

        new_data: dict[str, Keyboard.ElementData] = OrderedDict()
        for k, v in data.items():
            subkeys = k.split('.', 1)
            key = subkeys.pop(0)
            if subkeys:
                v = cls._unnest(OrderedDict({subkeys.pop(): v}))
            else:
                v = handle_dict_and_list(v)
            if key in new_data:
                # print(f'{key=} in {new_data=}, updating with {v=}')
                recursive_update(new_data[key], v)
                # print(f'Now {new_data=}')
            else:
                new_data[key] = v

        # print(f'< unnest: {new_data}')

        return new_data

    def _expand_units(self, data: dict[str, Keyboard.ElementData]) -> dict[str, Keyboard.ElementData]:
        def handle_dict_and_list(value: Keyboard.ElementData) -> Keyboard.ElementData:
            if isinstance(value, str):
                return self.units.eval(value)
            elif isinstance(value, dict):
                return self._expand_units(value)
            elif isinstance(value, list):
                return [handle_dict_and_list(item) for item in value]
            else:
                return value

        new_data: dict[str, Keyboard.ElementData] = {}
        for k, v in data.items():
            v = handle_dict_and_list(v)
            new_data[k] = v

        return new_data

    @property
    def points(self) -> Points:
        if (points := self._points) is None:
            points = self._points = Points(self.filepath.with_name('points.yaml'), self)

        return points

    @property
    def units(self) -> Units:
        if (units := self._units) is None:
            units = self._units = Units(self.filepath.with_name('units.yaml'))

        return units

    @property
    def general_offset(self) -> tuple[float, float]:
        for zone in self.data['points']['zones'].values():
            return zone['anchor']['shift']

    @property
    def layers(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data['layers']

    @property
    def kle(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data['kle']


ergogen_cli = ClyoTyper(help='Ergogen-related commands')


@ergogen_cli.command()
def merge_configs(
    yaml_files: list[str],
    output: Path = Option(..., '--output', '-o'),
) -> None:
    import jinja2

    class PreproccessedHiYaPyCo(hiyapyco.HiYaPyCo):

        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.__already_unnested = False
            super().__init__(*args, **kwargs)

        def _deepmerge(self, a, b):
            if not self.__already_unnested:
                self.__already_unnested = True
                try:
                    a = Keyboard._unnest(a)
                    b = Keyboard._unnest(b)
                    return super()._deepmerge(a, b)
                finally:
                    self.__already_unnested = False
            else:
                return super()._deepmerge(a, b)

    hiyapyco.jinja2env = jinja2.Environment(undefined=jinja2.StrictUndefined)
    merged = PreproccessedHiYaPyCo(
        yaml_files,
        method=hiyapyco.METHOD_MERGE,
        interpolate=True,
        failonmissingfiles=True,
    ).data()

    with output.open(mode='w') as f:
        hiyapyco.dump(merged, stream=f, indent=2)


@ergogen_cli.command()
def gen_kle(
    ergogen_yaml: Path,
    output: Annotated[Optional[Path], Argument()] = None,
) -> None:
    from kle import Keyboard as KLEKeyboard
    keeb = Keyboard(ergogen_yaml)
    points = keeb.points

    if output is None:
        output = ergogen_yaml.with_suffix('.json')
    kle = KLEKeyboard(output)

    kle.name = keeb.kle.get('name', None)
    kle.offset = keeb.kle['shift']
    kle.layers = keeb.kle['layers']
    for key in points:
        kle.add_key(**key)

    kle.write()


@ergogen_cli.command('_print')
def _print(
    ergogen_yaml: Path,
) -> None:
    keeb = Keyboard(ergogen_yaml)
    print(keeb.data)


@ergogen_cli.command('_general-offset')
def _general_offset(
    ergogen_yaml: Path,
) -> None:
    keeb = Keyboard(ergogen_yaml)
    print(keeb.general_offset)
