#!/usr/bin/env python3
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
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Optional

if TYPE_CHECKING:
    pass

# Third-party imports
try:
    from clyo import Argument, ClyoTyper, Option
except ImportError:
    from typer import Argument, Option
    from typer import Typer as ClyoTyper

# Local imports
from ergogen import ergogen_cli
from kicad import kicad_cli
from qmk import qmk_cli

OURSELF = Path(__file__).resolve()
BASE_PATH = OURSELF.parent
NAME = Path(sys.argv[0]).stem  # Or use OURSELF.stem

_logger = logging.getLogger(NAME)
config = ConfigParser()
cli = ClyoTyper(help='Application testing Clyo features')
cli.add_typer(ergogen_cli, name='ergogen', rich_help_panel='Ergogen')
cli.add_typer(kicad_cli, name='kicad', rich_help_panel='KiCAD')
cli.add_typer(qmk_cli, name='qmk', rich_help_panel='QMK')


@cli.command()
def gen_qmk_info_json(
    ergogen_yaml: Path,
    points_yaml: Annotated[Optional[Path], Option()] = None,
    units_yaml: Annotated[Optional[Path], Option()] = None,
) -> None:
    from ergogen import Keyboard
    from qmk import QMK_CLI
    from qmk import KeyboardInfo as QMKKeyboardInfo

    keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)
    qmk_cli = QMK_CLI()
    qmk_info = QMKKeyboardInfo(qmk_cli.keyboard_path / 'info.json')
    qmk_info.set_infos(keeb.qmk.get('keyboard', {}))
    qmk_info.layout_meta = keeb.qmk['_layout']
    qmk_info.layout.clear()

    for key in keeb.points.keys:
        qmk_info.add_key(**key)

    print('writing')
    qmk_info.write()


@cli.command()
def gen_qmk_keymap_json(
    ergogen_yaml: Path,
    points_yaml: Annotated[Optional[Path], Option()] = None,
    units_yaml: Annotated[Optional[Path], Option()] = None,
    output: Path = Option(..., '--output', '-o'),
) -> None:
    from ergogen import Keyboard
    from qmk import QMK_CLI
    from qmk import KeyboardInfo as QMKKeyboardInfo
    from qmk import Keymap as QMKKeymap

    keeb = Keyboard(ergogen_yaml, points_yaml, units_yaml)
    qmk_cli = QMK_CLI()
    qmk_info = QMKKeyboardInfo(qmk_cli.keyboard_path / 'info.json')
    qmk_info.set_infos(keeb.qmk.get('keyboard', {}))
    qmk_info.layout_meta = keeb.qmk['_layout']
    qmk_info.layout.clear()

    if output.suffix != '.json':
        output /= f"{qmk_info.data['keyboard_name'].replace('/', '-')}.json"
    keymap = QMKKeymap(output, qmk_info)
    keymap.data['keyboard'] = qmk_cli.keyboard
    keymap.data['layout'] = qmk_info.layout_meta['name']
    keymap.data['keymap'] = qmk_cli.keymap
    keymap.set_config(keeb.qmk.get('keymap', None))
    keymap.layers.clear()
    keymap.layers_meta = keeb.data['layers']

    for key in keeb.points.keys:
        qmk_info.add_key(**key)
        keymap.add_key(**key)

    keymap.write()


@cli.command(hidden=True)
def prompt() -> None:
    from clyo import CommandTree

    command_tree = CommandTree(cli)

    session = command_tree.make_prompt_session()
    try:
        while True:
            command_tree.repl(session)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    if hasattr(cli, 'set_main_callback'):
        cli.set_main_callback(
            NAME,
            config=config,
            default_command=prompt,
            default_config_path=Path('config.cfg'),
            default_logging_level='WARNING',
            rich_tracebacks=False,
        )

    cli(prog_name=NAME)
