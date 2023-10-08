// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#include "lexa.h"


typedef struct {
    uint16_t layer_state;
    // led_t led_state;
    uint8_t mod_state;
    uint8_t os_mod_state;
} oled_states_t;

static oled_states_t oled_states = {
    .layer_state = 0xFFFF,
    .mod_state = 0,
    .os_mod_state = 0
};

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_270;
}

bool oled_task_user(void) {
    bool diff = false;
    if(layer_state != oled_states.layer_state) {
        diff = true;
        oled_states.layer_state = layer_state;
    }
    if(get_mods() != oled_states.mod_state) {
        diff = true;
        oled_states.mod_state = get_mods();
    }
    if(get_oneshot_mods() != oled_states.os_mod_state) {
        diff = true;
        oled_states.os_mod_state = get_oneshot_mods();
    }
    if(!diff)
        return false;

    oled_clear();

    switch (get_highest_layer(layer_state)) {
        // case COLEMAK_DH:
        //     oled_write_P(PSTR("COLEMAK DH\n"), false);
        //     break;
        case SYM1:
            oled_write_P(PSTR("SYM1\n"), false);
            break;
        case SYM2:
            oled_write_P(PSTR("SYM2\n"), false);
            break;
        case NUM:
            oled_write_P(PSTR("NUM\n"), false);
            break;
        case MATH:
            oled_write_P(PSTR("MATH\n"), false);
            break;
        case NAV:
            oled_write_P(PSTR("NAV\n"), false);
            break;
        case MEDIA:
            oled_write_P(PSTR("MEDIA\n"), false);
            break;
        case FUN:
            oled_write_P(PSTR("FUN\n"), false);
            break;

        // default:
        //     if(IS_LAYER_ON_STATE(default_layer_state, COLEMAK))
        //         oled_write_P(PSTR("COLEMAK\n"), false);
    }

    // // Host Keyboard LED Status
    // led_t led_state = host_keyboard_led_state();
    // if(led_state.num_lock)
    //     oled_write_P(PSTR("NUM\n"), false);
    // if(led_state.caps_lock)
    //     oled_write_P(PSTR("CAP\n"), false);
    // if(led_state.scroll_lock)
    //     oled_write_P(PSTR("SCR\n"), false);

    uint8_t mod_state = oled_states.mod_state;
    uint8_t os_mod_state = oled_states.os_mod_state;

    if(mod_state & MOD_MASK_SHIFT)
        oled_write_P(PSTR("SHIFT\n"), false);
    else if(os_mod_state & MOD_MASK_SHIFT)
        oled_write_P(PSTR("SHIFT*\n"), false);
    else
        oled_write_P(PSTR("\n"), false);

    if(mod_state & MOD_MASK_CTRL)
        oled_write_P(PSTR("CTRL\n"), false);
    else if(os_mod_state & MOD_MASK_CTRL)
        oled_write_P(PSTR("CTRL*\n"), false);
    else
        oled_write_P(PSTR("\n"), false);

    if(mod_state & MOD_MASK_ALT)
        oled_write_P(PSTR("ALT\n"), false);
    else if(os_mod_state & MOD_MASK_ALT)
        oled_write_P(PSTR("ALT*\n"), false);
    else
        oled_write_P(PSTR("\n"), false);

    if(mod_state & MOD_MASK_GUI)
        oled_write_P(PSTR("GUI\n"), false);
    else if(os_mod_state & MOD_MASK_GUI)
        oled_write_P(PSTR("GUI*\n"), false);
    else
        oled_write_P(PSTR("\n"), false);

    // char buf[10] = {0};
    // oled_write(get_numeric_str(buf, 10, last_diff, ' '), false);
    // oled_write_P(PSTR("\n"), false);
    // oled_write(get_numeric_str(buf, 10, scroll, ' '), false);
    return false;
}
