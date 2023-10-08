// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#include "lexa.h"


bool process_record_user(uint16_t keycode, keyrecord_t *record) {
#ifdef OLED_ENABLE
    process_record_user_oled(keycode, record);
#endif // OLED_ENABLE

    return process_record_user_keycodes(keycode, record)
#ifdef ENCODER_ENABLE
        && process_record_user_encoders(keycode, record)
#endif
        && true;
}


#ifdef HOLD_ON_OTHER_KEY_PRESS_PER_KEY
bool get_hold_on_other_key_press(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case LT(NUM, KC_TAB):
            // Immediately select the hold action when another key is pressed.
            return true;
        default:
            // Do not select the hold action when another key is pressed.
            return false;
    }
}
#endif


#ifdef AUTO_SHIFT_ENABLE
bool get_custom_auto_shifted_key(uint16_t keycode, keyrecord_t *record) {
    switch(keycode) {
        case KC_DOT:
            return IS_LAYER_ON(0) || IS_LAYER_ON(NUM);
        case KC_COMMA:
        case KC_MINUS:
        case KC_QUOTE:
            return IS_LAYER_ON(0);
        default:
            return false;
    }
}

void autoshift_press_user(uint16_t keycode, bool shifted, keyrecord_t *record) {
    switch(keycode) {
        case KC_DOT:
            if(IS_LAYER_ON(0))
                register_code16((!shifted) ? KC_DOT : KC_COLON);
            else if(IS_LAYER_ON(NUM))
                register_code16((!shifted) ? KC_DOT : KC_COMMA);
            // else
            //     register_code16(KC_DOT);
            break;
        case KC_COMMA:
            register_code16((!shifted) ? KC_COMMA : KC_SEMICOLON);
            break;
        default:
            if (shifted) {
                add_weak_mods(MOD_BIT(KC_LSFT));
            }
            // & 0xFF gets the Tap key for Tap Holds, required when using Retro Shift
            register_code16((IS_RETRO(keycode)) ? keycode & 0xFF : keycode);
    }
}

void autoshift_release_user(uint16_t keycode, bool shifted, keyrecord_t *record) {
    switch(keycode) {
        case KC_DOT:
            if(IS_LAYER_ON(0))
                unregister_code16((!shifted) ? KC_DOT : KC_COLON);
            else if(IS_LAYER_ON(NUM))
                unregister_code16((!shifted) ? KC_DOT : KC_COMMA);
            // else
            //     register_code16(KC_DOT);
            break;
        case KC_COMMA:
            unregister_code16((!shifted) ? KC_COMMA : KC_SEMICOLON);
            break;
        default:
            // & 0xFF gets the Tap key for Tap Holds, required when using Retro Shift
            // The IS_RETRO check isn't really necessary here, always using
            // keycode & 0xFF would be fine.
            unregister_code16((IS_RETRO(keycode)) ? keycode & 0xFF : keycode);
    }
}
#endif


void matrix_scan_user(void) {
#ifdef ENCODER_ENABLE
    matrix_scan_user_encoders();
#endif
}


__attribute__((weak)) bool process_record_user_keycodes(uint16_t keycode, keyrecord_t *record) { return true; }
#ifdef OLED_ENABLE
__attribute__((weak)) bool process_record_user_oled(uint16_t keycode, keyrecord_t *record) { return true; }
#endif
#ifdef ENCODER_ENABLE
__attribute__((weak)) bool process_record_user_encoders(uint16_t keycode, keyrecord_t *record) { return true; }
__attribute__((weak)) void matrix_scan_user_encoders(void) {}
#endif
