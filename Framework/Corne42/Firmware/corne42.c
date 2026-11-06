// Derived from Axel Voitier HandyWork; channels follow the Corne42 schematic.
#include "quantum.h"

#ifdef LED_MATRIX_ENABLE
const is31fl3733_led_t PROGMEM g_is31fl3733_leds[IS31FL3733_LED_COUNT] = {
    {0, SW5_CS11}, // SW_R1C1
    {0, SW5_CS9}, // SW_R1C2
    {0, SW5_CS12}, // SW_R1C3
    {0, SW5_CS13}, // SW_R1C4
    {0, SW5_CS2}, // SW_R1C5
    {0, SW5_CS3}, // SW_R1C6
    {0, SW5_CS4}, // SW_R1C8
    {0, SW5_CS5}, // SW_R1C9
    {0, SW5_CS7}, // SW_R1C10
    {0, SW5_CS6}, // SW_R1C11
    {0, SW5_CS8}, // SW_R1C12
    {0, SW5_CS10}, // SW_R1C13
    {0, SW4_CS11}, // SW_R2C1
    {0, SW4_CS9}, // SW_R2C2
    {0, SW4_CS12}, // SW_R2C3
    {0, SW4_CS13}, // SW_R2C4
    {0, SW4_CS2}, // SW_R2C5
    {0, SW4_CS3}, // SW_R2C6
    {0, SW4_CS4}, // SW_R2C8
    {0, SW4_CS5}, // SW_R2C9
    {0, SW4_CS7}, // SW_R2C10
    {0, SW4_CS6}, // SW_R2C11
    {0, SW4_CS8}, // SW_R2C12
    {0, SW4_CS10}, // SW_R2C13
    {0, SW3_CS11}, // SW_R3C1
    {0, SW3_CS9}, // SW_R3C2
    {0, SW3_CS12}, // SW_R3C3
    {0, SW3_CS13}, // SW_R3C4
    {0, SW3_CS2}, // SW_R3C5
    {0, SW3_CS3}, // SW_R3C6
    {0, SW3_CS4}, // SW_R3C8
    {0, SW3_CS5}, // SW_R3C9
    {0, SW3_CS7}, // SW_R3C10
    {0, SW3_CS6}, // SW_R3C11
    {0, SW3_CS8}, // SW_R3C12
    {0, SW3_CS10}, // SW_R3C13
    {0, SW1_CS13}, // SW_R5C4
    {0, SW1_CS2}, // SW_R5C5
    {0, SW1_CS3}, // SW_R5C6
    {0, SW1_CS4}, // SW_R5C8
    {0, SW1_CS5}, // SW_R5C9
    {0, SW1_CS7}, // SW_R5C10
};
#endif

#include "power.inc"
