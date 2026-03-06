# Kicad footprint library for Framework keyboard things

## One Key Module

> [!WARNING]
> Validation in progress
>
> - [x] Against CAD
> - [x] With real caliper measurements
> - [x] Paper test
> - [x] 3D print test
> - [ ] Soldered on real PCB

Three variants are available:
- [One Key Module.kicad_mod](One%20Key%20Module.kicad_mod): The base footprint for a PCB
- [One Key Module for Top Plate.kicad_mod](One%20Key%20Module%20for%20Top%20Plate.kicad_mod): Just the keycap aperture suitable for a top plate
- [One Key Module for 3D Print.kicad_mod](One%20Key%20Module%20for%203D%20Print.kicad_mod): Variation of the base footprint with wider slot holes to compensate for typical X/Y hole shrinkage from 3D printers.

Top view
[![image](OKM%2001.png)](OKM%2001.png)

Bottom view
[![image](OKM%2002.png)](OKM%2002.png)

Bottom view without 3D model
[![image](OKM%2003.png)](OKM%2003.png)

Bottom in footprint editor (flipped, with FAB layer on to see the pin mapping)
[![image](OKM%2004.png)](OKM%2004.png)

Dimensions used
[![image](OKM%2005.png)](OKM%2005.png)
[![image](OKM%2006.png)](OKM%2006.png)

Paper test
[![image](OKM%2007.jpg)](OKM%2007.jpg)

## A1 Input Module Board

Two variants are available:
- [A1 Board PCB.kicad_mod](A1%20Board%20PCB.kicad_mod): A footprint for the full board. Includes:
    - The Edge.Cut contour
    - Pads for the pogo pins connector in the leftmost position
    - Rectangular hole for the other pogo pins connectors
    - Non-plated mechanical through holes for the positioning pins
    - Silkscreen filled rectangles corresponding to the placement of either the central bottom magnet, or the pieces of iron to glue on around the pogo pin connectors
    - User.1 layer corresponds to the inner zone where keycaps are allowed (ie. up to the full ~3.7 mm height)
    - User.2 layer corresponds to the recessed zones where electronics is allowed
        - NB: These are the minimal zones, assuming the keyboard can go in any of the three allowed positions on the deck
    - User.4 layer has a simple grid of 5x13 keys intended to be used as guidelines for pre-routing tracks before placing actual keys (eg. as used in a [template PCB](../Kicad%20templates/PCB)).

- [A1 Board PCB Top Plate.kicad_mod](A1%20Board%20PCB%20Top%20Plate.kicad_mod): A footprint for a top plate
    - Pads for the connector are removed
    - Other connector positions are closed
    - The positioning ridges at the back are removed.

Intended stack-up: Use the PCB one with a 0.8 mm thickness. And mount the top plate (eg. using a thin double-sided adhesive), for instance a 0.8 mm or 1 mm thick aluminium board, on top of the PCB.
You are also intended to glue a 10x3x1 mm bar magnet at the bottom in the middle. As well as glue six 4x8x0.3 mm pieces of galvanized iron sheets around where the pogo pin connectors will be.

[![image](A1%20Board%2001.png)](A1%20Board%2001.png)

[![image](A1%20Board%2002.png)](A1%20Board%2002.png)

## License

All original documents related to hardware designs are licensed under the [CERN Open Hardware Licence Version 2 or later - Permissive](LICENSE-CERN-OHL-P-2.0.txt).

