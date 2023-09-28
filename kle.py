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
import json
import logging
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import TypeAlias, Any

# Third-party imports

# Local imports

_logger = logging.getLogger(__name__)


class Keyboard:

    if TYPE_CHECKING:
        ElementType: TypeAlias = str | int | float | list['ElementType'] | dict[str, 'ElementType']

    def __init__(self, filepath: Path) -> None:
        self._filepath = filepath
        self._data: list[Keyboard.ElementType] | None = None
        self._current_y = 0
        self._offset: tuple[float, float] = (0, 0)
        self._layers: dict[str, dict[str, int | str]] = {}

    @property
    def data(self) -> list[Keyboard.ElementType]:
        if (data := self._data) is None:
            data = self._data = [dict(name=self._filepath.stem)]

        return data

    @property
    def offset(self) -> tuple[float, float]:
        return self._offset

    @offset.setter
    def offset(self, value: Sequence[float]) -> None:
        self._offset = (
            value[0] / 19.05,
            value[1] / 19.05,
        )

    @property
    def layers(self) -> dict[str, dict[str, int | str]]:
        return self._layers

    @layers.setter
    def layers(self, value: dict[str, dict[str, int | str]]) -> None:
        self._layers = value

    def write(self) -> None:
        data = self.data
        with self._filepath.open(mode='w') as f:
            json.dump(data, f, indent=4)

    def dump(self) -> None:
        print(json.dumps(self.data, indent=4))

    def add_key(
        self,
        x: float,
        y: float,
        r: float,
        name: str,
        width: float,
        height: float,
        layers: dict[str, str],
        **kwargs: Any
    ) -> None:
        # y = (-y / 19.05) - self._current_y
        # self.data.append([
        #     dict(
        #         x=x / 19.05,
        #         y=y,
        #     ),
        #     name.replace('matrix_', ''),
        # ])
        # self._current_y += y + 1
        offset_x, offset_y = self.offset
        params = dict(
            rx=(x / 19.05) + offset_x + 0.5,
            ry=(-y / 19.05) + offset_y + 0.5,
            x=-0.5,
            y=-0.5,
            r=-r,
        )
        if (width / 19.05) != 1:
            params['w'] = width / 19.05
            params['x'] = -params['w'] / 2
        if (height / 19.05) != 1:
            params['h'] = height / 19.05
            params['y'] = -params['h'] / 2

        def layer_meta(
            layer: str,
            meta: str,
            value: int | str | dict[str, int | str],
            default: int | str | None = None
        ) -> int | str:
            if isinstance(value, dict):
                if meta in value:
                    return value[meta]
            if default is not None:
                return self.layers[layer].get(meta, default)
            else:
                return self.layers[layer][meta]

        legends = [''] * 12
        sizes = [0] * 12
        colors = [''] * 12
        for layer, value in layers.items():
            if layer == 'on_hold':
                index = 4 if not isinstance(value, dict) else value.get('index', 4)
                legends[index] = value if not isinstance(value, dict) else value.get('value', 'X')
                colors[index] = layer_meta(value, 'color', value, '')
            else:
                index = layer_meta(layer, 'index', value, 9)
                legends[index] = layer_meta(layer, 'value', value, value)
                sizes[index] = layer_meta(layer, 'size', value)
                colors[index] = layer_meta(layer, 'color', value, '')

        params['fa'] = sizes
        params['t'] = '\n'.join(colors).rstrip('\n')

        self.data.append([
            params,
            '\n'.join([str(v) for v in legends]).rstrip('\n'),
        ])
