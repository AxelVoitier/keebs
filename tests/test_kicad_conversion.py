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
            kicad.Xy(x=-43.825214200000005, y=31.61306180000002),
            kicad.Xy(x=-44.908044600000004, y=29.931551100000018),
            -89.01176935063654,
            kicad.Xy(x=-45.525151, y=32.666731),
            kicad.Xy(x=-45.776176, y=31.17289),
        ),
        (
            kicad.Xy(x=-16.525, y=5.706893210765013),
            kicad.Xy(x=-13.817924099999999, y=9.910670110765015),
            -57.21997143350279,
            kicad.Xy(x=-11.525, y=5.706893),
            kicad.Xy(x=-12.135502, y=8.101117),
        ),
        (
            kicad.Xy(x=-4.029071675259355, y=60.454836573845206),
            kicad.Xy(x=-5.656912575259355, y=55.7272437738452),
            -15.101154660289524,
            kicad.Xy(x=-6.832351, y=56.314592),
            kicad.Xy(x=-6.264011, y=55.982136),
        ),
    ],
)
def test_basic_arc_math(
    # Given
    center: kicad.Xy,
    end: kicad.Xy,
    angle: float,
    # Fixture
    f_start: kicad.Xy,
    f_middle: kicad.Xy,
) -> None:
    radius = end.dist(center)
    angle_rad = math.radians(angle)

    relative_end = (end - center) / radius
    end_angle = math.atan2(relative_end.y, relative_end.x)
    start = kicad.Xy(
        x=center.x + (radius * math.cos(end_angle + angle_rad)),
        y=center.y + (radius * math.sin(end_angle + angle_rad)),
    )
    middle = kicad.Xy(
        x=center.x + (radius * math.cos(end_angle + (angle_rad / 2))),
        y=center.y + (radius * math.sin(end_angle + (angle_rad / 2))),
    )

    print(f'{relative_end=}, {angle_rad=}, {radius=}')
    esp = 1e-5
    eps_xy = kicad.Xy(x=esp, y=esp)
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
        (  # That one led to an obvious apparent bug as it used to turn the arc around
            '(gr_arc_20171130 (start 27.478653999999995 55.97431099999999) (end 119.3366868 -18.570922300000014) (angle -441.7053006987691) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -33.034904 -45.67705) (mid 48.19832 -60.497082) (end 119.336687 -18.570922)
        (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 84c3426e-fa2a-459d-a664-17a439759652))""",
        ),
        (
            '(gr_arc_20171130 (start 25.05 118.50000000000001) (end 25.05 50.88500000000002) (angle -33.76999992911506) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -12.534503 62.293298) (mid 5.411109 53.799906) (end 25.05 50.885)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 004f8fc4-1471-44e6-949c-f8965640a974))""",
        ),
        (
            '(gr_arc_20171130 (start -30.7131866 -41.2398839) (end -33.0312533 -45.670072000000005) (angle -152.37948209584056) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -30.713188 -36.239884) (mid -35.568645 -40.046348) (end -33.031253 -45.670072)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp c4862bec-7070-465f-9b0d-ef168b850954))""",
        ),
        (
            '(gr_arc_20171130 (start 25.05 118.50000000000001) (end -30.614253199999997 19.41512010000001) (angle -8.943661861590428) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -45.341523 29.273569) (mid -38.170344 24.056839) (end -30.614253 19.41512)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp c0340a8d-8e51-4517-8546-66e64de9002d))""",
        ),
        (
            '(gr_arc_20171130 (start -33.06318639999999 15.055908500000015) (end -30.614253199999993 19.415120200000015) (angle -60.67344138800814) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -28.063187 15.055909) (mid -28.747827 17.581313) (end -30.614253 19.41512)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 38c7fc31-0360-4b58-8347-a1470636ca88))""",
        ),
        (
            '(gr_arc_20171130 (start -42.2446676 33.19906090000002) (end -45.3415229 29.27356900000002) (angle -85.49977815602023) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -46.401046 35.978363) (mid -47.183384 32.418622) (end -45.341523 29.273569)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 8c0a1171-8f16-466b-85f5-fe385d65a421))""",
        ),
        (
            '(gr_arc_20171130 (start -36.27179098129984 60.12147817062715) (end -33.49248848129984 64.27785617062715) (angle -89.99999523714158) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -32.115413 57.342175) (mid -31.367524 61.095217) (end -33.492488 64.277856)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 31d4fc85-c529-4907-9af8-c74fa46addde))""",
        ),
        (
            '(gr_arc_20171130 (start -30.713186580758283 68.43423450400175) (end -33.49248908075828 64.27785650400175) (angle -179.99999523714126) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -27.933885 72.590613) (mid -34.869565 71.213537) (end -33.492489 64.277857)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp bc7f00cb-db62-4e79-ab45-be34d807f52f))""",
        ),
        (
            '(gr_arc_20171130 (start 93.14098671573296 45.885) (end 93.14098671573296 50.885) (angle -70.00000118663905) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 97.83945 47.595101) (mid 96.008869 49.98076) (end 93.140987 50.885)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 81437819-a921-4b15-ba8a-d3385dcb25e6))""",
        ),
        (
            '(gr_arc_20171130 (start 115.45426789999999 -15.420236200000012) (end 120.1527311 -13.710135600000012) (angle -59.06024527255928) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start 119.336686 -18.570922) (mid 120.385261 -16.248067) (end 120.152731 -13.710136)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 9d438dae-93ea-4cbf-8dc5-925d0e2df39f))""",
        ),
        (
            '(gr_arc_20171130 (start -30.713186499999996 -33.589883900000004) (end -28.063186499999997 -33.589883900000004) (angle -90) (layer Edge.Cuts) (width 0.15))',
            """(gr_arc_20221018 (start -30.713186 -36.239884) (mid -28.839354 -35.463717) (end -28.063186 -33.589884)
    (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp d5590ab8-f07c-4e6f-9291-c68af492fda5))""",
        ),
        #     (  # Buggy ergogen arc
        #         '(gr_arc_20171130 (start -31.91218779999999 17.104738000000015) (end -30.61425319999999 19.415120200000015) (angle -0.0000012873069294982997) (layer Edge.Cuts) (width 0.15))',
        #         """(gr_arc_20221018 (start -30.614253 19.41512) (mid -33.210123 14.794356) (end -30.614253 19.41512)
        # (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 30d09ff1-a586-463c-a88d-ba909e9c3fb9))""",
        #     ),
        #     (  # Buggy ergogen arc
        #         '(gr_arc_20171130 (start -43.7001896 31.354079700000014) (end -45.3415229 29.273569000000013) (angle -6.812539936618123e-7) (layer Edge.Cuts) (width 0.15))',
        #         """(gr_arc_20221018 (start -45.341523 29.273569) (mid -42.058857 33.434591) (end -45.341523 29.273569)
        # (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp c4790076-ca36-4766-a8d3-75564ebfda3c))""",
        #     ),
        #     (  # Buggy ergogen arc
        #         '(gr_arc_20171130 (start -11.061473199999998 64.49617860000001) (end -12.534503299999997 62.29329820000001) (angle -6.934595404572974e-7) (layer Edge.Cuts) (width 0.15))',
        #         """(gr_arc_20221018 (start -12.534503 62.293298) (mid -9.588443 66.69906) (end -12.534503 62.293298)
        # (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp f85fa6bc-fe20-4eb5-b902-b780807aaa5e))""",
        #     ),
        #     (  # Buggy ergogen arc
        #         '(gr_arc_20171130 (start 95.34926441573296 46.688747299999996) (end 97.83944991573296 47.595100599999995) (angle -7.387059213215252e-7) (layer Edge.Cuts) (width 0.15))',
        #         """(gr_arc_20221018 (start 97.83945 47.595101) (mid 92.859078 45.782393) (end 97.83945 47.595101)
        # (stroke (width 0.15) (type solid)) (layer "Edge.Cuts") (tstamp 600b172f-8dec-4a9b-b23c-54056c509e7b))""",
        #     ),
    ],
)
def test_arc_conversion(arc_20171130_str: str, arc_20221018_str: str) -> None:
    with kicad.KicadPcb.as_context():
        arc_20171130 = kicad.GrArc_20171130.from_text(arc_20171130_str)
        arc_20221018 = kicad.GrArc_20221018.from_text(arc_20221018_str)

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
    assert (arc_20171130.center - converted.center) <= kicad.Xy(x=eps, y=eps)
    eps = 1e-4  # arc_20221018 already has rounded data to start from. So, it gets less precise
    assert (arc_20171130.center - arc_20221018.center) <= kicad.Xy(x=eps, y=eps)
    assert (arc_20221018.center - converted.center) <= kicad.Xy(x=eps, y=eps)


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
