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
''''''
from __future__ import annotations

# System imports
import logging
import sys
from configparser import ConfigParser
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

# Third-party imports
try:
    from clyo import ClyoTyper
except ImportError:
    from typer import Typer as ClyoTyper

# Local imports
from ergogen import ergogen_cli
# from kicad import kicad_cli


OURSELF = Path(__file__).resolve()
BASE_PATH = OURSELF.parent
NAME = Path(sys.argv[0]).stem  # Or use OURSELF.stem

_logger = logging.getLogger(NAME)
config = ConfigParser()
cli = ClyoTyper(help='Application testing Clyo features')
cli.add_typer(ergogen_cli, name='ergogen', rich_help_panel='Ergogen')
# cli.add_typer(kicad_cli, name='kicad', rich_help_panel='KiCAD')


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
            NAME, config=config, default_command=prompt,
            default_config_path=Path('config.cfg')
        )

    cli(prog_name=NAME)
