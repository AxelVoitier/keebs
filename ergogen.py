# Copyright (c) 2023 Axel Voitier
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words
# spell-checker:ignore
""""""
from __future__ import annotations

# System imports
import logging
import math
import re
from collections import OrderedDict
from math import floor, inf
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Optional, Self

if TYPE_CHECKING:
    from collections.abc import Iterator
    from typing import Any, TypeAlias

# Third-party imports
import hiyapyco

try:
    from clyo import Argument, ClyoTyper, Option
except ImportError:
    from typer import Argument, Option
    from typer import Typer as ClyoTyper
import yaml
from attrs import define
from rich import print

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

    def top_left_offset(self) -> tuple[float, float]:
        min_x = +inf
        max_y = -inf
        for point in self.data.values():
            if not (tags := point['meta']['tags']):
                continue
            if ('1u' not in tags) and ('1-5u' not in tags) and ('2u' not in tags):
                continue
            min_x = min(point['x'], min_x)
            max_y = max(point['y'], max_y)

        return (min_x, max_y)

    def __iter__(self) -> Iterator[dict[str, Points.ElementData]]:
        # offset_x, offset_y = self._keyboard.general_offset
        offset_x, offset_y = self.top_left_offset()

        def sort_key(elem: tuple[str, dict[str, Points.ElementData]]) -> tuple[float, float]:
            k, v = elem
            return (
                floor(round(-(v['y'] - offset_y) / 19.05, 2)),
                floor(round((v['x'] - offset_x) / 19.05, 2)),
            )

        for k, v in sorted(self.data.items(), key=sort_key):
            if not (tags := v['meta']['tags']):
                continue
            if ('1u' not in tags) and ('1-5u' not in tags) and ('2u' not in tags):
                continue

            yield dict(
                x=v['x'] - offset_x,
                y=-(v['y'] - offset_y),
                r=v['r'],
                name=k,
                width=v['meta']['width'],
                height=v['meta']['height'],
                mirrored=v['meta'].get('mirrored', False),
                layers=v['meta'].get('layers', {}),
                qmk=v['meta'].get('qmk', {}),
                original=v,
            )


class Units:
    if TYPE_CHECKING:
        ElementData: TypeAlias = int | float

    RE_MULT = re.compile(
        r'((?:[0-9]*\.[0-9]+)|(?:[0-9]+\.[0-9]*)|(?:[0-9]+)|(?:\(.*?\)))([a-zA-Z_][a-zA-Z0-9_]*)'
    )

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

    def __init__(
        self, filepath: Path, points_filepath: Path | None, units_filepath: Path | None
    ) -> None:
        self.filepath = filepath
        self.points_filepath = points_filepath
        self.units_filepath = units_filepath
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

    def _expand_units(
        self, data: dict[str, Keyboard.ElementData]
    ) -> dict[str, Keyboard.ElementData]:
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
            if (points_filepath := self.points_filepath) is None:
                points_filepath = self.filepath.with_name('points.yaml')
            points = self._points = Points(points_filepath, self)

        return points

    @property
    def units(self) -> Units:
        if (units := self._units) is None:
            if (units_filepath := self.units_filepath) is None:
                units_filepath = self.filepath.with_name('units.yaml')
            units = self._units = Units(units_filepath)

        return units

    @property
    def general_offset(self) -> tuple[float, float]:
        for zone in self.data['points']['zones'].values():
            return zone.get('anchor', {}).get('shift', [0, 0])

    @property
    def layers(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data['layers']

    @property
    def kle(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data.get('kle', {})

    @property
    def qmk(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data.get('qmk', {})

    @property
    def outlines(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data.get('outlines', {})

    @property
    def fabrication(self) -> dict[str, dict[str, dict[str, str]]]:
        return self.data.get('fabrication', {})


@define
class Point:
    x: float
    y: float
    r: float = 0

    @classmethod
    def from_points_yaml(cls, source: dict[str, float]) -> Self:
        return cls(x=source['x'], y=source['y'], r=source['r'])

    def __add__(self, other: Point | float) -> Self:
        if isinstance(other, Point):
            return type(self)(x=self.x + other.x, y=self.y + other.y, r=self.r + other.r)
        else:
            return type(self)(x=self.x + other, y=self.y + other, r=self.r)

    def __sub__(self, other: Point | float) -> Self:
        if isinstance(other, Point):
            return type(self)(x=self.x - other.x, y=self.y - other.y, r=self.r - other.r)
        else:
            return type(self)(x=self.x - other, y=self.y - other, r=self.r)

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

    def dist(self, other: Point) -> float:
        return (self - other).mag

    def shift(self, other: Point) -> Point:
        rx_rad = math.radians(self.r)
        ry_rad = math.radians(self.r + 90)

        # x = x * cos(r) + y * cos(r + 90)
        # y = x * sin(r) + y * sin(r + 90)

        return type(self)(
            x=self.x + (other.x * math.cos(rx_rad) + other.y * math.cos(ry_rad)),
            y=self.y + (other.x * math.sin(rx_rad) + other.y * math.sin(ry_rad)),
            r=self.r + other.r,
        )


@define
class Line:
    start: Point
    end: Point

    def intersect(self, other: Line) -> Point:
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        x3, y3 = other.start.x, other.start.y
        x4, y4 = other.end.x, other.end.y

        x1y2_y1x2 = (x1 * y2) - (y1 * x2)
        x3y4_y3x4 = (x3 * y4) - (y3 * x4)
        denominator = ((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4))
        return Point(
            x=((x1y2_y1x2 * (x3 - x4)) - ((x1 - x2) * x3y4_y3x4)) / denominator,
            y=((x1y2_y1x2 * (y3 - y4)) - ((y1 - y2) * x3y4_y3x4)) / denominator,
        )

    @property
    def dx(self) -> float:
        return self.end.x - self.start.x

    @property
    def dy(self) -> float:
        return self.end.y - self.start.y

    @property
    def slope(self) -> float:
        return self.dy / self.dx

    @property
    def intercept(self) -> float:
        return self.start.y - (self.start.x * self.slope)

    def y_at_x(self, x: float) -> float:
        return (self.slope * x) + self.intercept


@define
class Circle:
    center: Point
    radius: float


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
    points_yaml: Annotated[Optional[Path], Option()] = None,
    units_yaml: Annotated[Optional[Path], Option()] = None,
) -> None:
    from kle import Keyboard as KLEKeyboard

    keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)
    points = keeb.points

    if output is None:
        output = ergogen_yaml.with_suffix('.json')
    kle = KLEKeyboard(output)

    kle.name = keeb.kle.get('name', None)
    kle.layers = keeb.kle['layers']
    for key in points:
        kle.add_key(**key)

    kle.write()


@ergogen_cli.command()
def preprocess(
    ergogen_yaml: Path,
    points_yaml: Path,
    units_yaml: Path,
    preproccesed_yaml: Path,
) -> None:
    keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)

    with preproccesed_yaml.open() as f:
        preprocessed = yaml.load(f, Loader=Loader)
    if 'units' not in preprocessed:
        preprocessed['units'] = {}
    units = preprocessed['units']

    for zone_name, zone in keeb.data.get('points', {}).get('zones', {}).items():
        if preprocess := zone.get('key', {}).get('preprocess', {}):
            print()
            print('---------------------------------')
            print(f'Preprocessing {zone_name}')
            method = preprocess['method']
            if method == 'intersect':  # noqa: SIM102
                if 'lines' in preprocess:
                    _preprocess_intersect_lines(keeb, preprocess, zone_name, units)
                elif ('line' in preprocess) and ('circle' in preprocess):
                    _preprocess_intersect_line_circle(keeb, preprocess, zone_name, units)
            elif method == 'circle-on-line-tangent-to-other-circle':
                _preprocess_circle_line_circle_tangent(keeb, preprocess, zone_name, units)

    with preproccesed_yaml.open(mode='w') as f:
        hiyapyco.dump(preprocessed, stream=f, indent=2)


if TYPE_CHECKING:
    PointDef: TypeAlias = 'dict[str, Any] | list[PointDef]'


def _preprocess_get_point(
    keeb: Keyboard,
    point_def: PointDef,
    ref: Point | None = None,
) -> Point:
    if ref is None:
        ref = Point(0, 0, 0)

    if isinstance(point_def, dict):
        # print(point_def)
        if 'ref' in point_def:
            point = Point.from_points_yaml(keeb.points.data[point_def['ref']])
        elif 'affect' not in point_def:
            point = ref
        else:
            point = Point(0, 0, 0)
        # print('ref point:', point)

        if 'orient' in point_def:
            point.r += point_def['orient']

        if 'shift' in point_def:
            shift_point = Point(x=point_def['shift'][0], y=point_def['shift'][1])
            # print('shift point:', shift_point)
            point = point.shift(shift_point)
            # print('shiftted point:', point)

        if 'rotate' in point_def:
            point.r += point_def['rotate']

        if 'affect' in point_def:
            affects = point_def['affect']
            if not isinstance(affects, list):
                affects = [affects]
            for member in affects:
                setattr(ref, member, getattr(point, member))
            point = ref

        # print(f'{point=}')
        # print()
        return point

    else:
        for sub_point_def in point_def:
            ref = _preprocess_get_point(keeb, sub_point_def, ref)

        return ref


def _preprocess_get_line(
    keeb: Keyboard,
    line_def: list[dict[str, Any]] | dict[str, dict[str, Any]],
) -> Line:
    if isinstance(line_def, list) and (len(line_def) == 2):
        return Line(
            start=_preprocess_get_point(keeb, line_def[0]),
            end=_preprocess_get_point(keeb, line_def[1]),
        )
    elif isinstance(line_def, dict) and ('start' in line_def) and ('end' in line_def):
        return Line(
            start=_preprocess_get_point(keeb, line_def['start']),
            end=_preprocess_get_point(keeb, line_def['end']),
        )
    else:
        msg = f'Unsupported definition for a line: {line_def}'
        raise ValueError(msg)


def _preprocess_get_circle(
    keeb: Keyboard,
    circle_def: dict[str, Any],
) -> Circle:
    return Circle(
        center=_preprocess_get_point(keeb, circle_def['center']),
        radius=circle_def['radius'],
    )


def _preprocess_intersect_lines(
    keeb: Keyboard,
    preprocess: dict[str, Any],
    zone_name: str,
    units: dict[str, float],
) -> None:
    lines = preprocess['lines']
    assert len(lines) == 2

    line_a = _preprocess_get_line(keeb, lines[0])
    line_b = _preprocess_get_line(keeb, lines[1])

    result = line_a.intersect(line_b)
    units[f'preprocessed_x_{zone_name}'] = result.x
    units[f'preprocessed_y_{zone_name}'] = result.y
    units[f'preprocessed_r_{zone_name}'] = result.r


def _preprocess_intersect_line_circle(
    keeb: Keyboard,
    preprocess: dict[str, Any],
    zone_name: str,
    units: dict[str, float],
) -> None:
    line = _preprocess_get_line(keeb, preprocess['line'])
    circle = _preprocess_get_circle(keeb, preprocess['circle'])
    det_sign = 1 if preprocess['determinant-sign'] == 'plus' else -1

    # Circle equation:
    # (x - Cx)^2 + (y - Cy)^2 = Cr^2
    Cx = circle.center.x
    Cy = circle.center.y
    Cr = circle.radius

    # Line equation:
    # y = La * x + Lb
    # TODO: Handle vertical lines
    La = line.slope
    Lb = line.intercept

    # Merging both to get a polynome:
    # (x - Cx)^2 + (La * x + Lb - Cy)^2 = Cr^2
    # x^2 - (2 * x * Cx) + Cx^2 + (La * x + Lb)^2 - (2 * Cy * (La * x + Lb)) + Cy^2 = Cr^2
    # x^2 - (2 * x * Cx) + Cx^2 + (La * x)^2 + (2 * La * Lb * x) + Lb^2 - (2 * Cy * La * x) - (2 * Cy * Lb) + Cy^2 = Cr^2
    # ((1 + La^2) * x^2) + (((-2 * Cx) + (2 * La * Lb) - (2 * Cy * La)) * x) + (Cx^2 + Lb^2 - (2 * Cy * Lb) + Cy^2 - Cr^2) = 0

    # a = 1 + La^2
    # b = (-2 * Cx) + (2 * La * Lb) - (2 * Cy * La)
    # c = Cx^2 + Lb^2 - (2 * Cy * Lb) + Cy^2 - Cr^2
    a = 1 + La**2
    b = (-2 * Cx) + (2 * La * Lb) - (2 * Cy * La)
    c = Cx**2 + Lb**2 - (2 * Cy * Lb) + Cy**2 - Cr**2

    det = (b * b) - (4 * a * c)

    if det >= 0:
        # We have either one or two solutions. In the later case, det_sign tell
        # us which one to choose (and if det == 0, sqrt(det) is 0, and so we don't care)
        root = ((det_sign * math.sqrt(det)) - b) / (2 * a)
    else:
        msg = f'Cannot complete preprocces for {zone_name}. Math error: determinant is negative'
        raise ValueError(msg)

    x = root
    units[f'preprocessed_x_{zone_name}'] = x
    units[f'preprocessed_y_{zone_name}'] = line.y_at_x(x)
    units[f'preprocessed_r_{zone_name}'] = 0


def _preprocess_circle_line_circle_tangent(
    keeb: Keyboard,
    preprocess: dict[str, Any],
    zone_name: str,
    units: dict[str, float],
) -> None:
    circle = _preprocess_get_circle(keeb, preprocess['circle'])
    target_circle_center_line = _preprocess_get_line(keeb, preprocess['line'])
    target_circle_radius = preprocess['radius']
    internal_sign = 1 if preprocess['internal'] else -1
    det_sign = 1 if preprocess['determinant-sign'] == 'plus' else -1

    # We want to find the (x, y) position of a target circle, such that
    # it is tangent to another circle, with the constrains that
    # its center rides on a given line.

    # The 2 points of the line give us the following equation:
    # yL = La * xL + Lb
    # In usual cases, we search to solve for xL in this problem.
    # However, if the line is vertical we switch to solving for yL (and xL is just a known variable)
    try:
        La = target_circle_center_line.slope
    except ZeroDivisionError:
        is_vertical_line = True
        xL = target_circle_center_line.start.x
        La = Lb = 0
    else:
        is_vertical_line = False
        Lb = target_circle_center_line.intercept
        xL = 0

    # The target circle has equation:
    # (xT - Tx)^2 + (yT - Ty)^2 = Tr^2, we know:
    Tr = target_circle_radius

    # The other circle has equation:
    # (xC - Cx)^2 + (yC - Cy)^2 = Cr^2, we know
    Cx = circle.center.x
    Cy = circle.center.y
    Cr = circle.radius

    # We only need to do two things to get to a polynomial that we can solve.
    # 1- As the two circles are tangent, they can be merged like this:
    # (Cx - Tx)^2 + (Cy - Ty)^2 = (Cr ± Tr)^2
    # The ± sets whether the solution put the target circle inside or outside the other one.

    # 2- Since the target circle center rides on a given line, in the usual case we can replace
    # Tx and Ty with the line equation (expressing yL in terms of xL). #1 becomes:
    # (Cx - xL)^2 + (Cy - (La * xL + Lb))^2 = (Cr ± Tr)^2
    # And in case of a vertical line, we get:
    # (Cx - xL)^2 + (Cy - yL)^2 = (Cr ± Tr)^2

    # We can then expand that, then regroup terms such that we get a polynomial:
    if not is_vertical_line:
        # In the usual case:
        # a * xL^2 + b * xL + c = 0
        # With:
        # a = 1 + La^2
        # b = -2 * (Cx + (Cy - Lb) * La)
        # c = Cx^2 - Cr^2 - Tr^2 + (Cy - Lb)^2 ± (2 * Cr * Tr)
        a = 1 + La**2
        b = -2 * (Cx + ((Cy - Lb) * La))
        c = Cx**2 + ((Cy - Lb) * (Cy - Lb)) - Cr**2 - Tr**2 + (internal_sign * 2 * Cr * Tr)
    else:
        # And in the case of a vertical line:
        # a * yL^2 + b * yL + c = 0
        # With:
        # a = 1
        # b = -2 * Cy
        # c = Cx^2 + Cy^2 + xL^2 - Cr^2 - Tr^2 - (2 * Cx * xL) ± (2 * Cr * Tr)
        a = 1
        b = -2 * Cy
        c = Cx**2 + Cy**2 + xL**2 - Cr**2 - Tr**2 - (2 * Cx * xL) + (internal_sign * 2 * Cr * Tr)

    # Solving for xL or yL, we first get a determinant: b^2 - 4ac
    det = (b * b) - (4 * a * c)

    if det >= 0:
        # We have either one or two solutions. In the later case, det_sign tell
        # us which one to choose (and if det == 0, sqrt(det) is 0, and so we don't care)
        root = ((det_sign * math.sqrt(det)) - b) / (2 * a)
    else:
        msg = f'Cannot complete preprocces for {zone_name}. Math error: determinant is negative'
        raise ValueError(msg)

    if not is_vertical_line:
        xL = root
        units[f'preprocessed_x_{zone_name}'] = xL
        units[f'preprocessed_y_{zone_name}'] = target_circle_center_line.y_at_x(xL)
        units[f'preprocessed_r_{zone_name}'] = 0
    else:
        yL = root
        units[f'preprocessed_x_{zone_name}'] = xL
        units[f'preprocessed_y_{zone_name}'] = yL
        units[f'preprocessed_r_{zone_name}'] = 0


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
