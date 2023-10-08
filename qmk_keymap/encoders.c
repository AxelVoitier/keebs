// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#include "lexa.h"


uint32_t last_pulse = 0;
uint32_t last_diff = 0;
uint8_t scroll = 0;

bool is_gui_tab_active = false;
uint16_t gui_tab_timer = 0;


bool process_record_user_encoders(uint16_t keycode, keyrecord_t *record) {
    switch(keycode) {
        case KC_LEFT:
        case KC_UP:
        case KC_DOWN:
        case KC_RGHT:
            if(is_gui_tab_active)
                gui_tab_timer = timer_read();

            return true;

        default:
            return true;
    }
}

void matrix_scan_user_encoders(void) {
    if(is_gui_tab_active) {
        if(timer_elapsed(gui_tab_timer) > 1250) {
            unregister_code(KC_LGUI);
            is_gui_tab_active = false;
        }
    }
}

bool encoder_update_user(uint8_t index, bool clockwise) {
    uint8_t i;
    uint32_t pulse = timer_read32();
    last_diff = TIMER_DIFF_32(pulse, last_pulse);
    last_pulse = pulse;
    scroll = 100 / last_diff;
    if(scroll < 1)
        scroll = 1;

    if(layer_state_is(MEDIA)) {
        if(index == 0) {  // Volume
            if(clockwise)
                tap_code(KC_VOLU);
            else
                tap_code(KC_VOLD);
        }else if(index == 1) {  // Track
            if(clockwise)
                tap_code(KC_MNXT);
            else
                tap_code(KC_MPRV);
        }
    }else if(layer_state_is(NAV)) {
        // if(index == 0) {  // Words
        //     if(clockwise)
        //         tap_code16(C(KC_LEFT));
        //     else
        //         tap_code16(C(KC_RGHT));
        // }else if(index == 1) {  // Tabs
        //     if(clockwise)
        //         tap_code16(C(KC_TAB));
        //     else
        //         tap_code16(S(C(KC_TAB)));
        // }
        if(index == 0) {  // Words
            if(clockwise)
                tap_code16(KC_UP);
            else
                tap_code16(KC_DOWN);
        }else if(index == 1) {  // Words
            if(clockwise)
                tap_code16(C(KC_RGHT));
            else
                tap_code16(C(KC_LEFT));
        }
    }else if(layer_state_is(SHORT)) {
        if(index == 0) {  // Search results
            if(clockwise)
                tap_code16(S(KC_F3));
            else
                tap_code(KC_F3);
        }else if(index == 1) {  // Windows
            if(clockwise) {
                if(!is_gui_tab_active) {
                    is_gui_tab_active = true;
                    register_code(KC_LGUI);
                }
                gui_tab_timer = timer_read();
                tap_code16(KC_TAB);
            }else{
                if(!is_gui_tab_active) {
                    is_gui_tab_active = true;
                    register_code(KC_LGUI);
                }
                gui_tab_timer = timer_read();
                tap_code16(S(KC_TAB));
            }
        }
    }else{
        if(index == 0) {  // Vertical scrolling
            if(clockwise) {
                for(i=0 ; i < scroll ; i++)
                    tap_code(KC_MS_WH_UP);
            }else {
                for(i=0 ; i < scroll ; i++)
                    tap_code(KC_MS_WH_DOWN);
            }
        }else if(index == 1) {  // Horizontal scrolling
            if(clockwise)
                tap_code(KC_MS_WH_RIGHT);
            else
                tap_code(KC_MS_WH_LEFT);
        }
    }
    return false;
}
