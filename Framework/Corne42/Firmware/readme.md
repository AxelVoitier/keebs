# HandyWork Corne42 prototype

Personal derivative of Axel Voitier HandyWork. 42 OKMs, RP2040, IS31FL3733.
Generated from the Corne42 schematic, not a copy of the 46-key LED order.

PROTOTYPE: hardware validation pending. See firmware/build/artifact-verification.json for build status.
GPIO0 SLEEP# and USB suspend gate the LED driver; RP2040 whole-board low-power
consumption is still unverified and not guaranteed by this gating code.
Starter US QWERTY with number/navigation and symbol layers; this is not Vincent's personal Corne keymap. OS keyboard layout controls character interpretation.
Hold upper-left key while connecting USB for bootmagic. Hardware boot/reset
buttons remain the recovery path. No device has been flashed.

Physical display coordinates use the approved20.3mm horizontal pitch.
Electrical matrix indices remain identical to the original42-key study.
