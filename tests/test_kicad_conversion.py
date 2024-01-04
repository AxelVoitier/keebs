# Copyright (c) 2024 Contributors as noted in the AUTHORS file
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# spell-checker:enableCompoundWords
# spell-checker:words kicad
# spell-checker:ignore tstamp sexpr ndigits
""""""
from __future__ import annotations

# System imports
import logging
import math
import uuid

# Third-party imports
import pytest

# Local imports
import kicad

_logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ('center', 'end', 'angle', 'f_start', 'f_middle'),
    [
        (
            kicad.XY(x=-43.825214200000005, y=31.61306180000002),
            kicad.XY(x=-44.908044600000004, y=29.931551100000018),
            -89.01176935063654,
            kicad.XY(x=-45.525151, y=32.666731),
            kicad.XY(x=-45.776176, y=31.17289),
        ),
        (
            kicad.XY(x=-16.525, y=5.706893210765013),
            kicad.XY(x=-13.817924099999999, y=9.910670110765015),
            -57.21997143350279,
            kicad.XY(x=-11.525, y=5.706893),
            kicad.XY(x=-12.135502, y=8.101117),
        ),
        (
            kicad.XY(x=-4.029071675259355, y=60.454836573845206),
            kicad.XY(x=-5.656912575259355, y=55.7272437738452),
            -15.101154660289524,
            kicad.XY(x=-6.832351, y=56.314592),
            kicad.XY(x=-6.264011, y=55.982136),
        ),
    ],
)
def test_basic_arc_math(
    # Given
    center: kicad.XY,
    end: kicad.XY,
    angle: float,
    # Fixture
    f_start: kicad.XY,
    f_middle: kicad.XY,
) -> None:
    radius = end.dist(center)
    angle_rad = math.radians(angle)

    relative_end = (end - center) / radius
    end_angle = math.atan2(relative_end.y, relative_end.x)
    start = kicad.XY(
        x=center.x + (radius * math.cos(end_angle + angle_rad)),
        y=center.y + (radius * math.sin(end_angle + angle_rad)),
    )
    middle = kicad.XY(
        x=center.x + (radius * math.cos(end_angle + (angle_rad / 2))),
        y=center.y + (radius * math.sin(end_angle + (angle_rad / 2))),
    )

    print(f'{relative_end=}, {angle_rad=}, {radius=}')
    esp = 1e-5
    eps_xy = kicad.XY(x=esp, y=esp)
    assert abs(start - f_start) <= eps_xy
    assert abs(middle - f_middle) <= eps_xy


@pytest.mark.parametrize(
    'arc_20171130_str, arc_20221018_str',
    [
        (
            '(gr_arc_20171130 (start -43.825214200000005 31.61306180000002) (end -44.908044600000004 29.931551100000018) (angle -89.01176935063654) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -45.525151 32.666731) (mid -45.776176 31.17289) (end -44.908045 29.931551)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 8b50544e-3966-4d2c-8b69-a33250254ff7))""",
        ),
        (
            '(gr_arc_20171130 (start -9.525 -47.625) (end -9.9601324 -49.5770911) (angle -77.43387547993375) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -11.525 -47.625) (mid -11.085491 -48.875947) (end -9.960132 -49.577091)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 1d5c86cc-17d0-4fdf-828b-aaab836fc0a2))""",
        ),
        (
            '(gr_arc_20171130 (start 33.7620378 -57.273930899999996) (end 33.9363493 -59.2663203) (angle -17.56612459349526) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 33.326905 -59.226022) (mid 33.63008 -59.269573) (end 33.936349 -59.26632)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 1acdca78-cc02-4277-8909-bf16fa67f606))""",
        ),
        (
            '(gr_arc_20171130 (start 52.739546700000005 -55.613614000000005) (end 53.7875925 -57.317022400000006) (angle -26.602487822601248) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 52.913859 -57.606003) (mid 53.367573 -57.512451) (end 53.787593 -57.317022)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp bcec0c40-b24c-4a61-b3f9-7547d49d8446))""",
        ),
        (
            '(gr_arc_20171130 (start 96.8575142 -28.4694182) (end 98.2258025 -29.9281119) (angle -11.565847112680771) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 97.90556 -30.172827) (mid 98.071862 -30.058557) (end 98.225803 -29.928112)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 98079754-37d8-4044-a89d-014b7433c526))""",
        ),
        (
            '(gr_arc_20171130 (start 116.0222938 -10.492413599999999) (end 117.901679 -9.8083733) (angle -66.83166584992264) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 117.390583 -11.951107) (mid 117.967718 -10.956447) (end 117.901679 -9.808373)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp a4558ff8-468a-453a-ab63-2407a8d7f88c))""",
        ),
        (
            '(gr_arc_20171130 (start 94.8469717 47.6863057) (end 94.8529204 49.686296899999995) (angle -69.8295820447666) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 96.726357 48.370347) (mid 95.996559 49.322903) (end 94.85292 49.686297)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 9ecffd1c-2be0-44d8-9098-8fdcaf913da0))""",
        ),
        (
            '(gr_arc_20171130 (start -23.1595154 64.9540781) (end -24.8594516 66.0077464) (angle -92.30935691513776) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -22.038204 66.610177) (mid -23.577167 66.909984) (end -24.859452 66.007746)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp fa457bd7-b874-422c-ad56-128466e98a68))""",
        ),
        (
            '(gr_arc_20171130 (start 12.008291129103835 54.932729764396704) (end 11.993419129103835 49.93275186439671) (angle -18.829581198225384) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 10.38045 50.205137) (mid 11.17572 50.002535) (end 11.993419 49.932752)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp e56eae85-d41d-4983-9443-99f47ede568e))""",
        ),
        (
            '(gr_arc_20171130 (start -4.029071675259355 60.454836573845206) (end -5.656912575259355 55.7272437738452) (angle -15.101154660289524) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -6.832351 56.314592) (mid -6.264011 55.982136) (end -5.656913 55.727244)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp fcbaf9cd-0553-4ecb-8094-a909051f997d))""",
        ),
        (
            '(gr_arc_20171130 (start -16.525 5.706893210765013) (end -13.817924099999999 9.910670110765015) (angle -57.21997143350279) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -11.525 5.706893) (mid -12.135502 8.101117) (end -13.817924 9.91067)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp d39bcc29-b8c7-4a22-8fa9-e5cb1c8d022c))""",
        ),
    ],
)
def test_arc_conversion(arc_20171130_str: str, arc_20221018_str: str) -> None:
    arc_20171130: kicad.GrArc_20171130 = kicad.Token.from_sexpr(
        kicad.SParser.parse(arc_20171130_str)
    )
    arc_20221018: kicad.GrArc_20221018 = kicad.Token.from_sexpr(
        kicad.SParser.parse(arc_20221018_str)
    )

    print(arc_20171130)
    print(arc_20221018)
    converted = arc_20171130.to_version(20221018)
    print(converted)
    assert isinstance(converted, kicad.GrArc_20221018)

    eps = 1e-5
    assert isinstance(converted.start, kicad.Start)
    assert abs(converted.start - arc_20221018.start) <= kicad.Start(x=eps, y=eps)
    assert isinstance(converted.mid, kicad.Mid)
    assert abs(converted.mid - arc_20221018.mid) <= kicad.Mid(x=eps, y=eps)
    assert isinstance(converted.end, kicad.End)
    assert abs(converted.end - arc_20221018.end) <= kicad.End(x=eps, y=eps)
    assert converted.stroke == arc_20221018.stroke
    assert converted.layer == arc_20221018.layer
    assert isinstance(converted.tstamp, uuid.UUID)

    # Reverse convertion
    assert (arc_20171130.center - converted.center) <= kicad.XY(x=eps, y=eps)
    eps = 1e-4  # arc_20221018 already has rounded data to start from. So, it gets less precise
    assert (arc_20171130.center - arc_20221018.center) <= kicad.XY(x=eps, y=eps)
    assert (arc_20221018.center - converted.center) <= kicad.XY(x=eps, y=eps)


# Commented blocks below:
# Testing for full file conversion is actually not trivial.
# - tstamp UUID differs. While you can neutralise them in the object forms,
#   it's harder to do in the text form (notably the one we read from fixture file).
# - float are of different precisions. Worst, while you can match some of them
#   with a base precision of 6, others still seem to carry larger errors. Tests
#   above show errors can go as high as having to push precision comparison
#   down to 4. While in essence PCB fabrication is not more precise than ~0.01 mm
#   (ie. precision of 2 here), you face issues that not only pytest cannot do
#   approx comparison on nested datastructure, or on lists mixing non-numeric data.
#   If we implement our own recursive float checker, we still loose the
#   "structural" and other type and equality checks than pytest does for the
#   rest of the data (+ all the nice differences printout). But that float
#   differences issue is also quite untestable in pure text form...
# So, at some point, the amount of effort that needs to go into testing full file
# conversion is a bit too high, when compared to testing the bits that matters
# independently, which the other tests do (numerical test of the conversion
# itself just above, reading, parsing and exporting tests in other test files).
# Only test we are missing here is how the graphic items get reordered
# during a convertion.


# FIX_UUID = uuid.uuid4()


# def neutralise_uuids(obj: kicad.Token | list | dict) -> None:
#     if isinstance(obj, list):
#         for item in obj:
#             neutralise_uuids(item)
#     elif isinstance(obj, dict):
#         for item in obj.values():
#             neutralise_uuids(item)
#     elif isinstance(obj, kicad.Token):
#         for field in attrs.fields(type(obj)):
#             value = getattr(obj, field.name)
#             if isinstance(value, uuid.UUID):
#                 setattr(obj, field.name, FIX_UUID)
#             elif isinstance(value, (kicad.Token, list, dict)):
#                 neutralise_uuids(value)


# @pytest.mark.parametrize(
#     'source, name, footprint_fixture',
#     [
#         (
#             'fixtures/kicad/ergogen-outline-generated.kicad_pcb',
#             'Handy-pcb-outline',
#             'fixtures/kicad/ergogen-outline-converted.kicad_mod',
#         ),
#     ],
# )
# def test_pcb_to_footprint(source: str, name: str, footprint_fixture: str) -> None:
#     base_path = Path(__file__).resolve().parent
#     pcb = kicad.Token.from_sexpr(kicad.SParser.parse(base_path / source))
#     fixture = kicad.Token.from_sexpr(kicad.SParser.parse(base_path / footprint_fixture))

#     footprint = kicad.convert_pcb_to_footprint(pcb, name)
#     neutralise_uuids(fixture)
#     neutralise_uuids(footprint)

#     assert footprint == fixture

#     # # pytest.approx does not support nested data structures...
#     def list_rounder(list_: list, ndigits: int) -> None:
#         for i, item in enumerate(list_):
#             if isinstance(item, list):
#                 list_rounder(item, ndigits)
#             elif isinstance(item, float):
#                 list_[i] = round(item, ndigits)

#         return list_

#     assert list_rounder(footprint.to_sexpr_list(), 6) == fixture.to_sexpr_list()
#     assert footprint.to_sexpr_text() == (base_path / footprint_fixture).read_text()
