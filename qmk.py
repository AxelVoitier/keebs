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
import json

# System imports
import logging
import shlex
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from typing import TypeAlias, Any

# Third-party imports
try:
    from clyo import ClyoTyper, Argument, Option
except ImportError:
    from typer import Typer as ClyoTyper, Argument, Option

# Local imports

_logger = logging.getLogger(__name__)


KEYCODES = {
    '': 'KC_NO',
    'a': 'KC_A', 'A': 'KC_A',
    'b': 'KC_B', 'B': 'KC_B',
    'c': 'KC_C', 'C': 'KC_C',
    'd': 'KC_D', 'D': 'KC_D',
    'e': 'KC_E', 'E': 'KC_E',
    'f': 'KC_F', 'F': 'KC_F',
    'g': 'KC_G', 'G': 'KC_G',
    'h': 'KC_H', 'H': 'KC_H',
    'i': 'KC_I', 'I': 'KC_I',
    'j': 'KC_J', 'J': 'KC_J',
    'k': 'KC_K', 'K': 'KC_K',
    'l': 'KC_L', 'L': 'KC_L',
    'm': 'KC_M', 'M': 'KC_M',
    'n': 'KC_N', 'N': 'KC_N',
    'o': 'KC_O', 'O': 'KC_O',
    'p': 'KC_P', 'P': 'KC_P',
    'q': 'KC_Q', 'Q': 'KC_Q',
    'r': 'KC_R', 'R': 'KC_R',
    's': 'KC_S', 'S': 'KC_S',
    't': 'KC_T', 'T': 'KC_T',
    'u': 'KC_U', 'U': 'KC_U',
    'v': 'KC_V', 'V': 'KC_V',
    'w': 'KC_W', 'W': 'KC_W',
    'x': 'KC_X', 'X': 'KC_X',
    'y': 'KC_Y', 'Y': 'KC_Y',
    'z': 'KC_Z', 'Z': 'KC_Z',
    '0': 'KC_0',
    '1': 'KC_1',
    '2': 'KC_2',
    '3': 'KC_3',
    '4': 'KC_4',
    '5': 'KC_5',
    '6': 'KC_6',
    '7': 'KC_7',
    '8': 'KC_8',
    '9': 'KC_9',
    'Enter': 'KC_ENTER', '⏎': 'KC_ENTER',
    'Esc': 'KC_ESCAPE',
    'Back': 'KC_BACKSPACE', 'BS': 'KC_BACKSPACE', '⌫': 'KC_BACKSPACE',
    'Tab': 'KC_TAB', '⇥': 'KC_TAB',
    ' ': 'KC_SPACE', 'Space': 'KC_SPACE', '␣': 'KC_SPACE',
    '`': 'KC_GRAVE',
    '~': 'KC_TILDE',
    '!': 'KC_EXCLAIM',
    '@': 'KC_AT',
    '#': 'KC_HASH',
    '$': 'KC_DOLLAR',
    '%': 'KC_PERCENT',
    '^': 'KC_CIRCUMFLEX',
    '&': 'KC_AMPERSAND',
    '*': 'KC_ASTERISK',
    '(': 'KC_LEFT_PAREN',
    ')': 'KC_RIGHT_PAREN',
    '-': 'KC_MINUS',
    '_': 'KC_UNDERSCORE',
    '=': 'KC_EQUAL',
    '+': 'KC_PLUS',
    '[': 'KC_LEFT_BRACKET',
    '{': 'KC_LEFT_CURLY_BRACE',
    ']': 'KC_RIGHT_BRACKET',
    '}': 'KC_RIGHT_CURLY_BRACE',
    '\\': 'KC_BACKSLASH',
    '|': 'KC_PIPE',
    ';': 'KC_SEMICOLON',
    ':': 'KC_COLON',
    '\'': 'KC_QUOTE',
    '"': 'KC_DOUBLE_QUOTE',
    ',': 'KC_COMMA',
    '<': 'KC_LEFT_ANGLE_BRACKET',
    '.': 'KC_DOT',
    '>': 'KC_RIGHT_ANGLE_BRACKET',
    '/': 'KC_SLASH',
    '?': 'KC_QUESTION',
    'F1': 'KC_F1',
    'F2': 'KC_F2',
    'F3': 'KC_F3',
    'F4': 'KC_F4',
    'F5': 'KC_F5',
    'F6': 'KC_F6',
    'F7': 'KC_F7',
    'F8': 'KC_F8',
    'F9': 'KC_F9',
    'F10': 'KC_F10',
    'F11': 'KC_F11',
    'F12': 'KC_F12',
    'PrtScn': 'KC_PRINT_SCREEN',
    'ScrLock': 'KC_SCROLL_LOCK',
    'Pause': 'KC_PAUSE',
    'Ins': 'KC_INSERT',
    'Home': 'KC_HOME', '⇱': 'KC_HOME',
    'PageUp': 'KC_PAGE_UP', 'PUp': 'KC_PAGE_UP', '⇞': 'KC_PAGE_UP',
    'Delete': 'KC_DELETE', 'Del': 'KC_DELETE', '⌦': 'KC_DELETE',
    'End': 'KC_END', '⇲': 'KC_END',
    'PageDown': 'KC_PAGE_DOWN', 'PDown': 'KC_PAGE_DOWN', '⇟': 'KC_PAGE_DOWN',
    'Right': 'KC_RIGHT', '▶': 'KC_RIGHT',
    'Left': 'KC_LEFT', '◀': 'KC_LEFT',
    'Down': 'KC_DOWN', '▼': 'KC_DOWN',
    'Up': 'KC_UP', '▲': 'KC_UP',
    'LCtrl': 'KC_LEFT_CTRL', 'Ctrl': 'KC_LEFT_CTRL', '⎈': 'KC_LEFT_CTRL',
    'LShift': 'KC_LEFT_SHIFT', 'Shift': 'KC_LEFT_SHIFT', '⇧': 'KC_LEFT_SHIFT',
    'LAlt': 'KC_LEFT_ALT', 'Alt': 'KC_LEFT_ALT', '⎇': 'KC_LEFT_ALT',
    'LGui': 'KC_LEFT_GUI', 'Gui': 'KC_LEFT_GUI', '❖': 'KC_LEFT_GUI', '⊞': 'KC_LEFT_GUI', '⌘': 'KC_LEFT_GUI',
    'RCtrl': 'KC_RIGHT_CTRL',
    'RShift': 'KC_RIGHT_SHIFT',
    'RAlt': 'KC_RIGHT_ALT',
    'RGui': 'KC_RIGHT_GUI',

    # '': 'KC_',
}

SHORT_ALIASES = dict(
    KC_ENTER='KC_ENT',
    KC_ESCAPE='KC_ESC',
    KC_BACKSPACE='KC_BSPC',
    KC_SPACE='KC_SPC',
    KC_MINUS='KC_MINS',
    KC_EQUAL='KC_EQL',
    KC_LEFT_BRACKET='KC_LBRC',
    KC_RIGHT_BRACKET='KC_RBRC',
    KC_BACKSLASH='KC_BSLS',
    KC_SEMICOLON='KC_SCLN',
    KC_QUOTE='KC_QUOT',
    KC_GRAVE='KC_GRV',
    KC_COMMA='KC_COMM',
    KC_SLASH='KC_SLSH',
    KC_PRINT_SCREEN='KC_PSCR',
    KC_SCROLL_LOCK='KC_SCRL',
    KC_PAUSE='KC_PAUS',
    KC_INSERT='KC_INS',
    KC_PAGE_UP='KC_PGUP',
    KC_DELETE='KC_DEL',
    KC_PAGE_DOWN='KC_PGDN',
    KC_RIGHT='KC_RGHT',

    KC_TILDE='KC_TILD',
    KC_EXCLAIM='KC_EXLM',
    KC_DOLLAR='KC_DLR',
    KC_PERCENT='KC_PERC',
    KC_CIRCUMFLEX='KC_CIRC',
    KC_AMPERSAND='KC_AMPR',
    KC_ASTERISK='KC_ASTR',
    KC_LEFT_PAREN='KC_LPRN',
    KC_RIGHT_PAREN='KC_RPRN',
    KC_UNDERSCORE='KC_UNDS',
    KC_LEFT_CURLY_BRACE='KC_LCBR',
    KC_RIGHT_CURLY_BRACE='KC_RCBR',
    KC_COLON='KC_COLN',
    KC_DOUBLE_QUOTE='KC_DQUO',
    KC_LEFT_ANGLE_BRACKET='KC_LT',
    KC_RIGHT_ANGLE_BRACKET='KC_GT',
    KC_QUESTION='KC_QUES',
    KC_LEFT_CTRL='KC_LCTL',
    KC_LEFT_SHIFT='KC_LSFT',
    KC_LEFT_ALT='KC_LALT',
    KC_LEFT_GUI='KC_LGUI',
    KC_RIGHT_CTRL='KC_RCTL',
    KC_RIGHT_SHIFT='KC_RSFT',
    KC_RIGHT_ALT='KC_RALT',
    KC_RIGHT_GUI='KC_RGUI',

    # ='',
)

qmk_cli = ClyoTyper(help='QMK-related commands')


class QMK_CLI:

    def config_get(self, name: str) -> str:
        result = subprocess.run(shlex.split(f'qmk config {name}'), capture_output=True)
        output = result.stdout.decode().strip()
        _, value = output.split('=', maxsplit=1)
        return value

    @property
    def qmk_home(self) -> Path:
        return Path(self.config_get('user.qmk_home'))

    @property
    def keyboard(self) -> str:
        return self.config_get('user.keyboard')

    @property
    def keyboard_path(self) -> Path:
        return self.qmk_home / 'keyboards' / self.keyboard

    @property
    def root_keyboard_path(self) -> Path:
        return self.qmk_home / 'keyboards' /  Path(self.keyboard).parts[0]

    @property
    def keymap(self) -> str:
        return self.config_get('user.keymap')

    @property
    def keymap_path(self) -> Path:
        return self.root_keyboard_path / 'keymaps' / self.keymap


class KeyboardInfo:

    if TYPE_CHECKING:
        ElementType: TypeAlias = str | int | float | list['ElementType'] | dict[str, 'ElementType']

    def __init__(self, filepath: Path) -> None:
        self._filepath = filepath
        self._data: dict[str, KeyboardInfo.ElementType] | None = None
        self.layout_meta: dict[str, KeyboardInfo.ElementType] = {}

    def set_infos(self, from_ergogen: dict[str, KeyboardInfo.ElementType]) -> None:
        def traverse(
            sub_from: dict[str, KeyboardInfo.ElementType],
            sub_to: dict[str, KeyboardInfo.ElementType],
        ) -> None:
            for k, v in sub_from.items():
                if k.startswith('_'):
                    continue

                if isinstance(v, dict):
                    if k not in sub_to:
                        sub_to[k] = {}
                    traverse(v, sub_to[k])
                else:
                    sub_to[k] = v

        traverse(from_ergogen, self.data)

    @property
    def data(self) -> dict[str, KeyboardInfo.ElementType]:
        if (data := self._data) is None:
            if self._filepath.exists():
                data = self._data = json.loads(self._filepath.read_text())
            else:
                data = self._data = {}

        return data

    def write(self) -> None:
        data = self.data
        with self._filepath.open(mode='w') as f:
            json.dump(data, f, indent=4)

    @property
    def offset(self) -> tuple[float, float]:
        value = self.layout_meta.get('shift', (0, 0))
        return (
            value[0] / 19.05,
            value[1] / 19.05,
        )

    @property
    def layout(self) -> list[dict[str, str | int]]:
        data = self.data
        if (layouts := data.get('layouts', None)) is None:
            layouts = data['layouts'] = {}

        layout_name = self.layout_meta['name']
        if (layout := layouts.get(layout_name, None)) is None:
            layout = layouts[layout_name] = dict(layout=[])

        return layout['layout']

    def get_side_info(self, mirrored: bool) -> dict[str, str | bool]:
        for side_name, side in self.layout_meta['sides'].items():
            side = {} if side is None else dict(side)
            side['name'] = side_name
            side.setdefault('abbrev', side_name[0].upper())
            side.setdefault('is_mirror', False)
            side.setdefault('is_main', False)
            if side['is_mirror'] is mirrored:
                break
        else:
            raise ValueError(f'Key {name} is of no side!? {mirrored=}, sides={self.layout_meta["sides"]}')

        return side

    def add_key(
        self,
        x: float,
        y: float,
        r: float,
        width: float,
        height: float,
        qmk: dict[str, KeyboardInfo.ElementType],
        mirrored: bool,
        name: str,
        **kwargs: Any
    ) -> None:
        side = self.get_side_info(mirrored)

        if (matrix_pins := self.data.get('matrix_pins', None)) is None:
            matrix_pins = self.data['matrix_pins'] = dict()
        if (rows := matrix_pins.get('rows', None)) is None:
            rows = matrix_pins['rows'] = []
        if (cols := matrix_pins.get('cols', None)) is None:
            cols = matrix_pins['cols'] = []

        try:
            row_i = rows.index(qmk['row'])
        except KeyError:
            print(f'Skipping {name} as it lacks row  info')
            return
        except ValueError:
            row_i = len(rows)
            rows.append(qmk['row'])

        try:
            col_i = cols.index(qmk['col'])
        except KeyError:
            print(f'Skipping {name} as it lacks col info')
            return
        except ValueError:
            col_i = len(cols)
            cols.append(qmk['col'])

        label = self.layout_meta['labels'].format(
            side=side['name'],
            side_abbrev=side['abbrev'],
            row=qmk['row'],
            row_i=row_i,
            col=qmk['col'],
            col_i=col_i,
        )

        offset_x, offset_y = self.offset
        row_i += len(rows) if not side['is_main'] else 0
        params = dict(
            label=label,
            matrix=[row_i, col_i],
            x=(x / 19.05) + offset_x - 0.5,
            y=(-y / 19.05) + offset_y - 0.5,
            r=-r,
        )
        params['rx'] = params['x'] + 0.5
        params['ry'] = params['y'] + 0.5
        if (width / 19.05) != 1:
            params['w'] = width / 19.05
            params['x'] -= params['w'] / 4
        if (height / 19.05) != 1:
            params['h'] = height / 19.05
            params['y'] -= params['h'] / 4

        self.layout.append(params)


class Keymap:

    if TYPE_CHECKING:
        ElementType: TypeAlias = str | list['ElementType'] | dict[str, 'ElementType']

    def __init__(self, filepath: Path, info: KeyboardInfo) -> None:
        self._filepath = filepath
        self._info = info
        self._data: dict[str, Keymap.ElementType] | None = None
        self.layers_meta: dict[str, Keymap.ElementType] = {}

    @property
    def data(self) -> dict[str, Keymap.ElementType]:
        if (data := self._data) is None:
            if self._filepath.exists():
                data = self._data = json.loads(self._filepath.read_text())
                if 'layers' in data:
                    del data['layers']
            else:
                data = self._data = {}

        return data

    def write(self) -> None:
        data = self.data
        with self._filepath.open(mode='w') as f:
            json.dump(data, f, indent=4)

    @property
    def layers(self) -> list[list[str]]:
        data = self.data
        if (layers := data.get('layers', None)) is None:
            layers = data['layers'] = []
            rows = self._info.data['matrix_pins']['rows']
            cols = self._info.data['matrix_pins']['cols']
            length = len(rows) * len(cols) * 2
            for _ in self.layers_meta:
                layers.append(['KC_NO'] * length)

        return layers

    def get_key_index(self, row: str, col: str, is_main: bool) -> int:
        rows = self._info.data['matrix_pins']['rows']
        cols = self._info.data['matrix_pins']['cols']
        row_i = rows.index(row)
        row_i += len(rows) if not is_main else 0
        col_i = cols.index(col)

        return (len(cols) * row_i) + col_i

    def add_key(
        self,
        layers: dict[str, Keymap.ElementType],
        qmk: dict[str, Keymap.ElementType],
        mirrored: bool,
        name: str,
        **kwargs: Any
    ) -> None:
        side = self._info.get_side_info(mirrored)
        layer_indices = {layer_name: i for i, layer_name in enumerate(self.layers_meta.keys())}

        for layer_name, value in layers.items():
            if layer_name not in layer_indices:
                continue

            layer_index = layer_indices[layer_name]
            layer = self.layers[layer_index]
            key_index = self.get_key_index(qmk['row'], qmk['col'], side['is_main'])

            if isinstance(value, dict):
                if 'no-mod' in value:
                    if isinstance(value['no-mod'], dict):
                        key_value = value['no-mod']['value']
                    else:
                        key_value = value['no-mod']
                else:
                    key_value = value['value']
            else:
                key_value = value

            try:
                layer[key_index] = KEYCODES[key_value]
            except KeyError:
                print(f'Skipping {key_value} for now')
