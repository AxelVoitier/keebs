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
from math import floor
from operator import itemgetter
from pathlib import Path
from typing import TYPE_CHECKING, Iterable

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
    'Mute': 'KC_AUDIO_MUTE',
    'V+': 'KC_AUDIO_VOL_UP',
    'V-': 'KC_AUDIO_VOL_DOWN',
    'Next': 'KC_MEDIA_NEXT_TRACK',
    'Prev': 'KC_MEDIA_PREV_TRACK',
    'Stop': 'KC_MEDIA_STOP', '■': 'KC_MEDIA_STOP',
    'Play': 'KC_', '▶||': 'KC_MEDIA_PLAY_PAUSE',

    # '': 'KC_',
}

SHORT_ALIASES = dict(
    KC_TRANSPARENT='KC_TRNS',
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
    KC_AUDIO_MUTE='KC_MUTE',
    KC_AUDIO_VOL_UP='KC_VOLU',
    KC_AUDIO_VOL_DOWN='KC_VOLD',
    KC_MEDIA_NEXT_TRACK='KC_MNXT',
    KC_MEDIA_PREV_TRACK='KC_MPRV',
    KC_MEDIA_STOP='KC_MSTP',
    KC_MEDIA_PLAY_PAUSE='KC_MPLY',

    # ='',
)


def strip_last(line: str, old: str, new: str = '') -> str:
    return line[::-1].replace(old, new, 1)[::-1]


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
                elif v is None:
                    if k in sub_to:
                        del sub_to[k]
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

    def guess_layout_name(self) -> str | None:
        if 'name' in self.layout_meta:
            return self.layout_meta['name']
        layouts = self.data.get('layouts', {})
        if layouts:
            return next(iter(layouts.keys()))
        return None

    def get_side_info(self, mirrored: bool, name: str) -> dict[str, str | bool]:
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
        if qmk.get('ignore', False):
            return

        side = self.get_side_info(mirrored, name)

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
            # Self-adding row pin
            row_i = len(rows)
            rows.append(qmk['row'])

        try:
            col_i = cols.index(qmk['col'])
        except KeyError:
            print(f'Skipping {name} as it lacks col info')
            return
        except ValueError:
            # Self-adding column pin
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
            x=(x / 19.05) + offset_x,
            y=(y / 19.05) + offset_y,
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

    def max_len(self, data: Iterable[str | Any], item: Any | None = None) -> int:
        if item is not None:
            return max(map(len, map(itemgetter(item), data)))
        else:
            return max(map(len, data))

    def generate_layout_structure(self) -> list[list[str]]:
        max_len = self.max_len(self.layout, 'label')

        struct = []
        current_x = 0
        for key in self.layout:
            # The core of autolayout.
            # - Adding half of height and width is to get the center of the key.
            #   -> This is in the "hope" that keys are at least somewhat aligned on a grid
            #      and .5 would be their middle, such that round/floor/ceil operations have
            #      a good chance to give us their grid position.
            # - Round at 2 digits. This handles cases of float errors (eg. .999999) that trip
            #   floor/ceil operations afterwards. It also handles some cases of rotated keys.
            # - Floor to get integers aligned with top-left corner.
            # /!\ NOT battle tested.
            height = key.get('h', 1)
            width = key.get('w', 1)
            x_i = floor(round(key['x'] + (width / 2), 2))
            y_i = floor(round(key['y'] + (height / 2), 2))

            # This part grows the structure progressively as needed
            diff_y = y_i - len(struct) + 1
            diff_x = x_i - current_x + 1
            if diff_y > 0:
                for _ in range(diff_y):
                    struct.append([' ' * max_len] * current_x)
            if diff_x > 0:
                for row in struct:
                    row += [' ' * max_len] * diff_x
                current_x += diff_x

            if struct[y_i][x_i] != (' ' * max_len):
                print(f'Warning, overwriting key in ({x_i}, {y_i}). Was {struct[y_i][x_i]}, is now {key["label"]}')
            struct[y_i][x_i] = key['label']
            key['x_i'] = x_i
            key['y_i'] = y_i

        return struct

    def layout_h(self) -> list[str]:
        struct = self.generate_layout_structure()
        layout_name = self.layout_meta['name']
        max_len = self.max_len(self.layout, 'label')

        lines = []
        lines.append('#pragma once')
        lines.append('')
        lines.append(f'#define {layout_name}_keebs (\\')
        indent = 2
        for row in struct:
            current_line = ' ' * indent
            for cell in row:
                if not cell.strip():
                    current_line += (' ' * (max_len + 2))
                else:
                    current_line += f'{cell + ",":<{max_len + 1}} '
            current_line += '\\'
            lines.append(current_line)
        lines[-1] = strip_last(lines[-1], ',', ' ')
        lines.append(') { \\')

        rows = self.data['matrix_pins']['rows']
        cols = self.data['matrix_pins']['cols']
        is_split = self.data.get('split', {}).get('enabled', False)
        n_rows = len(rows) if not is_split else len(rows) * 2
        matrix = []
        for _ in range(n_rows):
            matrix.append(['KC_NO'] * len(cols))

        for key in self.layout:
            row, col = key['matrix']
            matrix[row][col] = key['label']

        max_len = max(len('KC_NO'), max_len)
        current_line = '/*' + (' ' * (indent - 2)) + '  '
        current_line += ' '.join([f'{col:<{max_len + 1}}' for col in cols])
        current_line += '*/ \\'
        lines.append(current_line)

        for i, row in enumerate(matrix):
            if is_split and (i == len(rows)):
                lines.append(f'/*{"SPLIT":-^{len(lines[-1]) - 6}}*/ \\')

            current_line = ' ' * indent
            current_line += '{ '
            current_line += ' '.join([f'{col + ",":<{max_len + 1}}' for col in row])
            current_line = strip_last(current_line, ',')
            current_line += f' }},  /* {rows[i % len(rows)]} */ \\'
            lines.append(current_line)
        lines[-1] = strip_last(lines[-1], ',', ' ')

        lines.append('}')
        lines.append('')
        return lines


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
            else:
                data = self._data = {}

        return data

    def write(self) -> None:
        data = self.data
        if not self._filepath.parent.exists() and self._filepath.parent.parent.exists():
            self._filepath.parent.mkdir()
        with self._filepath.open(mode='w') as f:
            json.dump(data, f, indent=4)

    @property
    def layers(self) -> list[list[str]]:
        data = self.data
        if not (layers := data.get('layers', None)):
            layers = data['layers'] = []
            for _ in self.layers_meta:
                layers.append([])

        return layers

    def add_key(
        self,
        layers: dict[str, Keymap.ElementType],
        qmk: dict[str, Keymap.ElementType],
        mirrored: bool,
        name: str,
        **kwargs: Any
    ) -> None:
        if qmk.get('ignore', False):
            return

        layer_indices = {layer_name: i for i, layer_name in enumerate(self.layers_meta.keys())}

        for layer_index, layer_name in enumerate(self.layers_meta.keys()):
            layer = self.layers[layer_index]

            if layer_name not in layers:
                if (layer_index > 0) and layers.get('transparent', False):
                    value = dict(keycode='KC_TRANSPARENT')
                else:
                    value = ''
            else:
                value = layers[layer_name]

            modifier = 'no-mod'
            if isinstance(value, dict):
                if modifier in value:
                    if isinstance(value[modifier], dict):
                        keycode = value[modifier].get(
                            'keycode', self.get_keycode(value[modifier].get('legend', None)))
                    else:
                        keycode = self.get_keycode(value[modifier])
                else:
                    keycode = value.get('keycode', self.get_keycode(value.get('legend', None)))
            else:
                keycode = self.get_keycode(value)

            if keycode is None:
                print(f'Skipping {value} on {name} key, layer {layer_name} for now')
                keycode = 'KC_NO'

            layer.append(keycode)

        if 'on_hold' in layers:
            if isinstance(layers['on_hold'], dict):
                target_layer = layers['on_hold']['legend']
            else:
                target_layer = layers['on_hold']
            target_layer_index = layer_indices[target_layer]

            key_index = len(layer) - 1
            original_keycode = self.layers[0][key_index]
            self.layers[0][key_index] = f'LT({target_layer_index}, {original_keycode})'
            # The key being held should map to nothing in the target layer. Otherwise, troubles...
            self.layers[target_layer_index][key_index] = 'KC_NO'
            # In every other layers, if the key is set to be transparent,
            # we put the original keycode instead
            if layers.get('transparent', False):
                for layer_index, layer in enumerate(self.layers):
                    if layer_index in (0, target_layer_index):
                        continue
                    layer[key_index] = original_keycode

    def get_keycode(self, legend: str | None) -> str:
        if legend is None:
            return None
        try:
            return KEYCODES[str(legend)]
        except KeyError:
            if len(legend) == 1:
                return f'UC(0x{ord(legend):X})'
            else:
                return None

    def keymap_c(self) -> list[str]:
        struct = self._info.generate_layout_structure()
        layout_name = self.data['layout'] + '_keebs'
        layout = self._info.layout

        lines = []
        lines.append('#include QMK_KEYBOARD_H')
        lines.append('')

        indent = ' ' * 4
        lines.append('enum layer_names {')
        for layer_name in self.layers_meta:
            lines.append(f'{indent}{layer_name.upper()},')
        lines[-1] = strip_last(lines[-1], ',', ' ')
        lines.append('};')
        lines.append('')

        lines.append('const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {')
        for layer_index, layer_name in enumerate(self.layers_meta):
            layer = self.layers[layer_index]
            keycodes = {key['label']: layer[i] for i, key in enumerate(layout)}

            col_max_len = [0] * len(struct[0])
            struct_keycodes: list[list[str]] = []
            for row in struct:
                row_keycodes: list[str] = []
                for i, cell in enumerate(row):
                    if not cell.strip():
                        row_keycodes.append('')
                    else:
                        keycode = keycodes[cell]
                        if keycode.startswith('KC_'):
                            keycode = SHORT_ALIASES.get(keycode, keycode)
                        else:
                            for orig, short in SHORT_ALIASES.items():
                                keycode = keycode.replace(orig, short)
                            if keycode.startswith('LT('):
                                comma_i = keycode.index(',')
                                for layer_i, layer_n in enumerate(self.layers_meta):
                                    keycode = keycode[:comma_i].replace(str(layer_i), layer_n.upper()) + keycode[comma_i:]

                        row_keycodes.append(keycode)
                        col_max_len[i] = max(len(keycode), col_max_len[i])

                struct_keycodes.append(row_keycodes)

            lines.append(f'{indent}[{layer_name.upper()}] = {layout_name}(')

            for row in struct_keycodes:
                current_line = indent * 2
                for i, cell in enumerate(row):
                    if not cell.strip():
                        current_line += (' ' * (col_max_len[i] + 2))
                    else:
                        current_line += f'{cell + ",":<{col_max_len[i] + 1}} '
                lines.append(current_line)

            lines[-1] = strip_last(lines[-1], ',')
            lines.append(f'{indent}),')
        lines[-1] = strip_last(lines[-1], ',')
        lines.append('};')

        lines.append('')
        return lines


qmk_cli = ClyoTyper(help='QMK-related commands')


@qmk_cli.command()
def gen_layout_structure(

) -> None:
    qmk_cli = QMK_CLI()
    qmk_info = KeyboardInfo(qmk_cli.root_keyboard_path / 'info.json')
    qmk_info.layout_meta = dict(
        name=qmk_info.guess_layout_name(),
    )

    struct = qmk_info.generate_layout_structure()
    for row in struct:
        print('-', row)


@qmk_cli.command()
def gen_layout_h(

) -> None:
    qmk_cli = QMK_CLI()
    qmk_info = KeyboardInfo(qmk_cli.root_keyboard_path / 'info.json')
    qmk_info.layout_meta = dict(
        name=qmk_info.guess_layout_name(),
    )
    layout_h_lines = qmk_info.layout_h()

    layout_h_path = qmk_cli.keyboard_path / 'layout.h'
    layout_h_path.write_text('\n'.join(layout_h_lines))


@qmk_cli.command()
def gen_keymap_c(
    ergogen_yaml: Path,

) -> None:
    from ergogen import Keyboard

    keeb = Keyboard(ergogen_yaml, None, None)
    qmk_cli = QMK_CLI()
    qmk_info = KeyboardInfo(qmk_cli.root_keyboard_path / 'info.json')
    qmk_info.layout_meta = dict(
        name=qmk_info.guess_layout_name(),
    )
    keymap = Keymap(qmk_cli.keymap_path / 'keymap.json', qmk_info)
    keymap.data['keyboard'] = qmk_cli.keyboard
    keymap.data['layout'] = qmk_info.layout_meta['name']
    keymap.layers_meta = keeb.data['layers']

    keymap_c_lines = keymap.keymap_c()
    keymap_c_path = qmk_cli.keymap_path / 'keymap.c'
    print(keymap_c_path)
    keymap_c_path.write_text('\n'.join(keymap_c_lines))
