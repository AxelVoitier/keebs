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
from typing import TYPE_CHECKING, Iterable, Iterator

if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import TypeAlias, Any

# Third-party imports

# Local imports

_logger = logging.getLogger(__name__)


class Keyboard:

    if TYPE_CHECKING:
        ElementType: TypeAlias = str | int | float | list['ElementType'] | dict[str, 'ElementType']
        LayerInfoType: TypeAlias = int | str | dict[str, 'LayerInfoType']

    def __init__(self, filepath: Path) -> None:
        self._filepath = filepath
        self._data: list[Keyboard.ElementType] | None = None
        self._current_y = 0
        self._offset: tuple[float, float] = (0, 0)
        self._layers: dict[str, Keyboard.LayerInfoType] = {}

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
        layers: dict[str, Keyboard.LayerInfoType],
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

        def get_layer_info(
            layer: str,
            modifier: str,
            key_value: Keyboard.LayerInfoType,
            defaults: dict[str, int | str] | None = None,
        ) -> dict[str, int | str]:
            def filter_keys(d: dict[str, Any], not_value: bool = False) -> dict[str, Any]:
                if not_value:
                    valid_keys = ('index', 'size', 'color')
                else:
                    valid_keys = ('value', 'index', 'size', 'color')

                return {k: v for k, v in d.items() if k in valid_keys}

            if defaults is None:
                info = dict(value='', index=9, size='', color='')
            else:
                info = dict(defaults)

            not_value = (modifier != 'no-mod')

            info.update(filter_keys(self.layers, not_value))
            info.update(filter_keys(self.layers.get(modifier, {})))

            if layer in self.layers:
                info.update(filter_keys(self.layers[layer], not_value))
                info.update(filter_keys(self.layers[layer].get(modifier, {})))

            if isinstance(key_value, dict):
                info.update(filter_keys(key_value, not_value))
                if modifier in key_value:
                    if isinstance(key_value[modifier], dict):
                        info.update(filter_keys(key_value[modifier]))
                    else:
                        info['value'] = key_value[modifier]
            elif not not_value:
                info['value'] = key_value

            return info

        legends = [''] * 12
        sizes = [0] * 12
        colors = [''] * 12
        for layer, value in layers.items():
            if layer == 'on_hold':
                value = value if isinstance(value, dict) else dict(value=value)
                layer = value['value']
                value.setdefault('index', 4)
            for modifier in ('no-mod', 'shift'):
                layer_info = get_layer_info(layer, modifier, value)
                if layer_info['value'] == '':
                    continue
                index = layer_info['index']
                legends[index] += str(layer_info['value'])
                sizes[index] = layer_info['size']
                colors[index] = layer_info['color']

        params['fa'] = sizes
        params['t'] = '\n'.join(colors).rstrip('\n')

        self.data.append([
            params,
            '\n'.join([str(v) for v in legends]).rstrip('\n'),
        ])
