// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#include "lexa.h"


uint16_t copy_paste_timer;


bool process_record_user_keycodes(uint16_t keycode, keyrecord_t *record) {
    switch(keycode) {
        // case KC_CCCV: // One key copy/paste
        //     if (record->event.pressed) {
        //         copy_paste_timer = timer_read();
        //     } else {
        //         if (timer_elapsed(copy_paste_timer) > TAPPING_TERM) { // Hold, copy
        //             tap_code16(LCTL(KC_C));
        //         } else { // Tap, paste
        //             tap_code16(LCTL(KC_V));
        //         }
        //     }
        //     break;
    }

    return true;
}
