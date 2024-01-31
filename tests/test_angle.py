# Copyright (c) 2024 Contributors as noted in the AUTHORS file
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words kicad
# spell-checker:ignore
""""""
from __future__ import annotations

# System imports
# Third-party imports
import pytest

# Local imports
from kicad import angle_key


@pytest.mark.parametrize(
    ('a', 'fixture'),
    [
        (None, None),
        # Center range
        (0, 0),
        (90, 90),
        (180, 180),
        (-90, -90),
        (-179, -179),
        (-179.999999, -179.999999),
        # Upward
        (180.000001, -179.999999),
        (181, -179),
        (270, -90),
        (360, 0),
        (360 + 90, 90),
        (360 + 180, 180),
        (360 + 180.000001, -179.999999),
        (360 + 181, -179),
        (360 + 270, -90),
        (360 + 360, 0),
        # Downward
        (-180, 180),
        (-270, 90),
        (-360, 0),
        (-360 - 90, -90),
        (-360 - 179, -179),
        (-360 - 179.999999, -179.999999),
        (-360 - 180, 180),
        (-360 - 270, 90),
        (-360 - 360, 0),
    ],
)
def test_angle_key(a: float | None, fixture: float | None) -> None:
    result = angle_key(a)
    assert result == fixture, f'_angle_key({a}) => {result} != {fixture}'
