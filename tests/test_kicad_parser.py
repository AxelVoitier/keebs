# Copyright (c) 2024 Contributors as noted in the AUTHORS file
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words kicad
# spell-checker:ignore KIPRJMOD descr uvia uvias sexpr
""""""
from __future__ import annotations

# System imports
import logging
from pathlib import Path
from typing import TYPE_CHECKING

# Third-party imports
import pytest

# Local imports
import kicad

if TYPE_CHECKING:
    from typing import Any

_logger = logging.getLogger(__name__)


def get_base_pcb(
    *,
    version: int = 20221018,
    generator: str = 'pcbnew',
    thickness: float = 1.6,
    paper_size: str = 'A4',
    layers_include_users: bool = True,
    layers_no_user_name: bool = False,
    **kwargs: Any,
) -> dict[str, int | str | kicad.Token]:
    # spell-checker: disable
    data = dict(
        version=kicad.Version(version=version),
        generator=generator,
        general=kicad.General(thickness=thickness),
        paper=kicad.Paper(paper_size=paper_size),
        layers=kicad.Layers(layers_def=[], layers_use=[]),
        setup=kicad.Setup(
            other_settings=dict(pad_to_mask_clearance=0),
            plot_settings=kicad.Pcbplotparams(
                params=dict(
                    layerselection='0x00010fc_ffffffff',
                    plot_on_all_layers_selection='0x0000000_00000000',
                    disableapertmacros='false',
                    usegerberextensions='false',
                    usegerberattributes='true',
                    usegerberadvancedattributes='true',
                    creategerberjobfile='true',
                    dashed_line_dash_ratio=12.0,
                    dashed_line_gap_ratio=3.0,
                    svgprecision=4,
                    plotframeref='false',
                    viasonmask='false',
                    mode=1,
                    useauxorigin='false',
                    hpglpennumber=1,
                    hpglpenspeed=20,
                    hpglpendiameter=15.0,
                    dxfpolygonmode='true',
                    dxfimperialunits='true',
                    dxfusepcbnewfont='true',
                    psnegative='false',
                    psa4output='false',
                    plotreference='true',
                    plotvalue='true',
                    plotinvisibletext='false',
                    sketchpadsonfab='false',
                    subtractmaskfromsilk='false',
                    outputformat=1,
                    mirror='false',
                    drillshape=1,
                    scaleselection=1,
                    outputdirectory='',
                ),
            ),
        ),
    )

    data['layers'].layers_def = [
        kicad._LayerDef(ordinal=0, canonical_name='F.Cu', type='signal'),
        kicad._LayerDef(ordinal=31, canonical_name='B.Cu', type='signal'),
        kicad._LayerDef(ordinal=32, canonical_name='B.Adhes', type='user', user_name='B.Adhesive'),
        kicad._LayerDef(ordinal=33, canonical_name='F.Adhes', type='user', user_name='F.Adhesive'),
        kicad._LayerDef(ordinal=34, canonical_name='B.Paste', type='user'),
        kicad._LayerDef(ordinal=35, canonical_name='F.Paste', type='user'),
        kicad._LayerDef(
            ordinal=36, canonical_name='B.SilkS', type='user', user_name='B.Silkscreen'
        ),
        kicad._LayerDef(
            ordinal=37, canonical_name='F.SilkS', type='user', user_name='F.Silkscreen'
        ),
        kicad._LayerDef(ordinal=38, canonical_name='B.Mask', type='user'),
        kicad._LayerDef(ordinal=39, canonical_name='F.Mask', type='user'),
        kicad._LayerDef(
            ordinal=40, canonical_name='Dwgs.User', type='user', user_name='User.Drawings'
        ),
        kicad._LayerDef(
            ordinal=41, canonical_name='Cmts.User', type='user', user_name='User.Comments'
        ),
        kicad._LayerDef(ordinal=42, canonical_name='Eco1.User', type='user', user_name='User.Eco1'),
        kicad._LayerDef(ordinal=43, canonical_name='Eco2.User', type='user', user_name='User.Eco2'),
        kicad._LayerDef(ordinal=44, canonical_name='Edge.Cuts', type='user'),
        kicad._LayerDef(ordinal=45, canonical_name='Margin', type='user'),
        kicad._LayerDef(ordinal=46, canonical_name='B.CrtYd', type='user', user_name='B.Courtyard'),
        kicad._LayerDef(ordinal=47, canonical_name='F.CrtYd', type='user', user_name='F.Courtyard'),
        kicad._LayerDef(ordinal=48, canonical_name='B.Fab', type='user'),
        kicad._LayerDef(ordinal=49, canonical_name='F.Fab', type='user'),
    ]
    if layers_include_users:
        data['layers'].layers_def.extend(
            [
                kicad._LayerDef(ordinal=50, canonical_name='User.1', type='user'),
                kicad._LayerDef(ordinal=51, canonical_name='User.2', type='user'),
                kicad._LayerDef(ordinal=52, canonical_name='User.3', type='user'),
                kicad._LayerDef(ordinal=53, canonical_name='User.4', type='user'),
                kicad._LayerDef(ordinal=54, canonical_name='User.5', type='user'),
                kicad._LayerDef(ordinal=55, canonical_name='User.6', type='user'),
                kicad._LayerDef(ordinal=56, canonical_name='User.7', type='user'),
                kicad._LayerDef(ordinal=57, canonical_name='User.8', type='user'),
                kicad._LayerDef(ordinal=58, canonical_name='User.9', type='user'),
            ],
        )
    if layers_no_user_name:
        for layer in data['layers'].layers_def:
            layer.user_name = None
    # spell-checker: enable

    data.update(kwargs)

    return data


def load_py_fixture(path: Path, name: str) -> kicad.Token:
    locs = dict(get_base_pcb=get_base_pcb)
    exec(path.read_text(), {}, locs)  # noqa: S102
    return locs[name]


tests_dir = Path(__file__).resolve().parent


@pytest.mark.parametrize(
    ('fixture_path', 'fixture_obj'),
    [
        (
            'fixtures/kicad/fp-lib-table-simple',
            kicad.FpLibTable(
                version=kicad.Version(version=7),
                libs=[
                    kicad.Lib(
                        name='Generated',
                        type=kicad.Lib.LibType.KiCad,
                        uri='${KIPRJMOD}/Generated.pretty',
                        options='',
                        descr='',
                    )
                ],
            ),
        ),
        (
            'fixtures/kicad/empty.kicad_pcb',
            kicad.KicadPcb(
                **get_base_pcb(  # type: ignore[reportGeneralTypeIssues]
                    nets=[kicad.Net(ordinal=0, net_name='')],
                    footprints=[],
                    graphic_items=[],
                    segments=[],
                    zones=[],
                    data=[],
                ),
            ),
        ),
        (
            'fixtures/kicad/empty-paper-portrait.kicad_pcb',
            kicad.KicadPcb(
                **get_base_pcb(  # type: ignore[reportGeneralTypeIssues]
                    paper=kicad.Paper(paper_size='A4', portrait=True),
                    nets=[kicad.Net(ordinal=0, net_name='')],
                    footprints=[],
                    graphic_items=[],
                    segments=[],
                    zones=[],
                    data=[],
                ),
            ),
        ),
        (
            'fixtures/kicad/empty-paper-user.kicad_pcb',
            kicad.KicadPcb(
                **get_base_pcb(  # type: ignore[reportGeneralTypeIssues]
                    paper=kicad.Paper(paper_size='User', width=431.8, height=279.4),
                    nets=[kicad.Net(ordinal=0, net_name='')],
                    footprints=[],
                    graphic_items=[],
                    segments=[],
                    zones=[],
                    data=[],
                ),
            ),
        ),
        (
            'fixtures/kicad/ergogen-outline-generated.kicad_pcb',
            load_py_fixture(tests_dir / 'fixtures/kicad/ergogen-outline-generated.py', 'pcb'),
        ),
        (
            'fixtures/kicad/empty.kicad_mod',
            kicad.Footprint(
                name='Handy-pcb-outline',
                version=kicad.Version(version=20221018),
                generator='pcbnew',
                layer='F.Cu',
                properties=[],
                settings={},
                graphic_items=[
                    kicad.FpText(
                        type=kicad.FpText.FpTextType.reference,
                        text='REF**',
                        at=kicad.At(x=0, y=-0.5, unlocked=True),
                        layer='F.SilkS',
                        hide=True,
                        effects=kicad.Effects(
                            font=kicad.Font(size=kicad.Size(x=1, y=1), thickness=0.1),
                        ),
                        tstamp='138e5e0e-e546-4625-9053-eae9e71e2188',
                    ),
                    kicad.FpText(
                        type=kicad.FpText.FpTextType.value,
                        text='Handy-pcb-outline',
                        at=kicad.At(x=0, y=1, unlocked=True),
                        layer='F.Fab',
                        hide=True,
                        effects=kicad.Effects(
                            font=kicad.Font(size=kicad.Size(x=1, y=1), thickness=0.15),
                        ),
                        tstamp='ffaac02c-30ab-4fbd-8b90-f33ac13bdccb',
                    ),
                ],
                pads=[],
                models=[],
                data=[],
            ),
        ),
        (
            'fixtures/kicad/ergogen-outline-converted.kicad_mod',
            load_py_fixture(tests_dir / 'fixtures/kicad/ergogen-outline-converted.py', 'footprint'),
        ),
        (
            'fixtures/kicad/ergogen-outline-as-footprint.kicad_pcb',
            load_py_fixture(tests_dir / 'fixtures/kicad/ergogen-outline-as-footprint.py', 'pcb'),
        ),
        (
            'fixtures/kicad/medium-footprint.kicad_mod',
            load_py_fixture(tests_dir / 'fixtures/kicad/medium-footprint.py', 'medium_footprint'),
        ),
    ],
)
def test_reading(fixture_path: str | Path, fixture_obj: kicad.Token) -> None:
    fixture_path = tests_dir / fixture_path

    # Sanity checks
    if (fixture_obj.version.version >= 20221018) or (fixture_obj.version.version == 7):
        assert fixture_obj.to_sexpr_list() == kicad.SParser.parse(fixture_path, unquote=False)

    obj = kicad.Token.from_file(fixture_path)
    assert obj == fixture_obj

    # Export tests
    if (obj.version.version >= 20221018) or (obj.version.version == 7):
        assert obj.to_sexpr_list() == kicad.SParser.parse(fixture_path, unquote=False)
        assert obj.to_sexpr_text() == fixture_path.read_text()


def test_comparison() -> None:
    # Checks float precision and tstamp change do not affect eq comparisons
    a = kicad.FpLine_20221018(
        start=kicad.Start(x=-44.908044600000004, y=29.931551000000017),
        end=kicad.End(x=-13.817924074832812, y=9.910670094558283),
        stroke=kicad.Stroke(width=0.15, type=kicad.Stroke.StrokeType.solid, color=None),
        layer='Edge.Cuts',
        tstamp='19c40b8f-917f-428d-bd15-159f66a0b605',
    )
    b = kicad.FpLine_20221018(
        start=kicad.Start(x=-44.908045, y=29.931551),
        end=kicad.End(x=-13.817924, y=9.91067),
        stroke=kicad.Stroke(width=0.15, type=kicad.Stroke.StrokeType.solid, color=None),
        layer='Edge.Cuts',
        tstamp='1712fe2c-1e66-4748-9877-807af8af5544',
    )
    assert a == b
    la = [a]
    lb = [b]
    assert la.index(b) == 0
    assert lb.index(a) == 0
