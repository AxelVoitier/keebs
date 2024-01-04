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
        layers=kicad.Layers(layers=[]),
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

    data['layers'].layers = [
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
        data['layers'].layers.extend(
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
        for layer in data['layers'].layers:
            layer.user_name = None
    # spell-checker: enable

    data.update(kwargs)

    return data


@pytest.mark.parametrize(
    ('fixture_path', 'fixture_obj'),
    [
        (
            'fixtures/kicad/fp-lib-table-simple',
            kicad.FpLibTable(
                version=kicad.Version(version=7),
                lib=kicad.Lib(
                    name='Generated',
                    type=kicad.Lib.LibType.KiCad,
                    uri='${KIPRJMOD}/Generated.pretty',
                    options='',
                    descr='',
                ),
            ),
        ),
        (
            'fixtures/kicad/empty.kicad_pcb',
            kicad.KicadPcb(
                **get_base_pcb(  # type: ignore[reportGeneralTypeIssues]
                    nets=[kicad.Net(ordinal=0, net_name='')],
                    graphic_items=[],
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
                    graphic_items=[],
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
                    graphic_items=[],
                    data=[],
                ),
            ),
        ),
        (
            'fixtures/kicad/ergogen-outline-generated.kicad_pcb',
            kicad.KicadPcb(
                **get_base_pcb(  # type: ignore[reportGeneralTypeIssues]
                    version=20171130,
                    generator='pcbnew 5.1.6',
                    paper=kicad.Page('A3'),
                    title_block=kicad.TitleBlock(
                        title='Handy-pcb-outline',
                        rev='v1.0.0',
                        company='Unknown',
                    ),
                    layers_include_users=False,
                    layers_no_user_name=True,
                    setup=kicad.Setup(
                        # spell-checker: disable
                        plot_settings=kicad.Pcbplotparams(
                            params={
                                'layerselection': '0x010fc_ffffffff',
                                'usegerberextensions': 'false',
                                'usegerberattributes': 'true',
                                'usegerberadvancedattributes': 'true',
                                'creategerberjobfile': 'true',
                                'excludeedgelayer': 'true',
                                'linewidth': 0.1,
                                'plotframeref': 'false',
                                'viasonmask': 'false',
                                'mode': 1,
                                'useauxorigin': 'false',
                                'hpglpennumber': 1,
                                'hpglpenspeed': 20,
                                'hpglpendiameter': 15.0,
                                'psnegative': 'false',
                                'psa4output': 'false',
                                'plotreference': 'true',
                                'plotvalue': 'true',
                                'plotinvisibletext': 'false',
                                'padsonsilk': 'false',
                                'subtractmaskfromsilk': 'false',
                                'outputformat': 1,
                                'mirror': 'false',
                                'drillshape': 1,
                                'scaleselection': 1,
                                'outputdirectory': '',
                            },
                        ),
                        # spell-checker: enable
                        other_settings={
                            'last_trace_width': 0.25,
                            'trace_clearance': 0.2,
                            'zone_clearance': 0.508,
                            'zone_45_only': 'no',
                            'trace_min': 0.2,
                            'via_size': 0.8,
                            'via_drill': 0.4,
                            'via_min_size': 0.4,
                            'via_min_drill': 0.3,
                            'uvia_size': 0.3,
                            'uvia_drill': 0.1,
                            'uvias_allowed': 'no',
                            'uvia_min_size': 0.2,
                            'uvia_min_drill': 0.1,
                            'edge_width': 0.05,
                            'segment_width': 0.2,
                            'pcb_text_width': 0.3,
                            'pcb_text_size': [1.5, 1.5],
                            'mod_edge_width': 0.12,
                            'mod_text_size': [1, 1],
                            'mod_text_width': 0.15,
                            'pad_size': [1.524, 1.524],
                            'pad_drill': 0.762,
                            'pad_to_mask_clearance': 0.05,
                            'aux_axis_origin': [0, 0],
                            'visible_elements': 'FFFFFF7F',
                        },
                    ),
                    nets=[kicad.Net(ordinal=0, net_name='')],
                    net_classes=[
                        kicad.NetClass(
                            name='Default',
                            description='This is the default net class.',
                            clearance=0.2,
                            trace_width=0.25,
                            via_dia=0.8,
                            via_drill=0.4,
                            uvia_dia=0.3,
                            uvia_drill=0.1,
                            add_net='',
                        ),
                    ],
                    graphic_items=[
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=-11.525, y=5.706893210765013),
                            end=kicad.End(x=-11.525, y=-47.625),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=-9.525, y=-47.625),
                            end=kicad.End(x=-9.9601324, y=-49.5770911),
                            angle=-77.43387547993375,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=-9.9601324, y=-49.5770911),
                            end=kicad.End(x=33.3269054, y=-59.226022),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=33.7620378, y=-57.273930899999996),
                            end=kicad.End(x=33.9363493, y=-59.2663203),
                            angle=-17.56612459349526,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=33.9363493, y=-59.266320300000004),
                            end=kicad.End(x=52.9138582, y=-57.606003400000006),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=52.739546700000005, y=-55.613614000000005),
                            end=kicad.End(x=53.7875925, y=-57.317022400000006),
                            angle=-26.602487822601248,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=53.787592499999995, y=-57.3170224),
                            end=kicad.End(x=97.90556000000001, y=-30.172826599999997),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=96.8575142, y=-28.4694182),
                            end=kicad.End(x=98.2258025, y=-29.9281119),
                            angle=-11.565847112680771,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=98.2258025, y=-29.9281119),
                            end=kicad.End(x=117.39058209999999, y=-11.9511073),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=116.0222938, y=-10.492413599999999),
                            end=kicad.End(x=117.901679, y=-9.8083733),
                            angle=-66.83166584992264,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=117.901679, y=-9.8083733),
                            end=kicad.End(x=96.7263569, y=48.370346),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=94.8469717, y=47.6863057),
                            end=kicad.End(x=94.8529204, y=49.686296899999995),
                            angle=-69.8295820447666,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=94.8529204, y=49.6862969),
                            end=kicad.End(x=11.993419129403046, y=49.93275186499069),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=10.380450181085843, y=50.20513691536339),
                            end=kicad.End(x=-5.656912623277353, y=55.7272437248119),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=-6.8323502531178795, y=56.31459145885365),
                            end=kicad.End(x=-22.038204, y=66.61017610000002),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=-23.1595154, y=64.9540781),
                            end=kicad.End(x=-24.8594516, y=66.0077464),
                            angle=-92.30935691513776,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=-24.8594516, y=66.00774640000002),
                            end=kicad.End(x=-45.5251504, y=32.66673010000002),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=-43.825214200000005, y=31.61306180000002),
                            end=kicad.End(x=-44.908044600000004, y=29.931551100000018),
                            angle=-89.01176935063654,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrLine_20171130(
                            start=kicad.Start(x=-44.908044600000004, y=29.931551000000017),
                            end=kicad.End(x=-13.817924074832812, y=9.910670094558283),
                            angle=90,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=12.008291129103835, y=54.932729764396704),
                            end=kicad.End(x=11.993419129103835, y=49.93275186439671),
                            angle=-18.829581198225384,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=-4.029071675259355, y=60.454836573845206),
                            end=kicad.End(x=-5.656912575259355, y=55.7272437738452),
                            angle=-15.101154660289524,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                        kicad.GrArc_20171130(
                            start=kicad.Start(x=-16.525, y=5.706893210765013),
                            end=kicad.End(x=-13.817924099999999, y=9.910670110765015),
                            angle=-57.21997143350279,
                            layer=kicad.Layer(canonical_name='Edge.Cuts'),
                            width=0.15,
                        ),
                    ],
                    data=[],
                ),
            ),
        ),
    ],
)
def test_reading(fixture_path: str | Path, fixture_obj: kicad.Token) -> None:
    fixture_path = Path(__file__).resolve().parent / Path(fixture_path)
    obj = kicad.Token.from_sexpr(kicad.SParser.parse(fixture_path))
    assert obj == fixture_obj

    if obj.version.version >= 20221018:
        assert obj.to_sexpr_list() == kicad.SParser.parse(fixture_path, unquote=False)
        assert obj.to_sexpr_text() == fixture_path.read_text()
