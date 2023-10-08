// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#include "lexa.h"


const key_override_t base_comma_shift_to_semicolon_key_override = ko_make_with_layers(
    MOD_MASK_SHIFT, KC_COMMA, KC_SEMICOLON, 1 << COLEMAK_DH);
const key_override_t base_dot_shift_to_colon_key_override = ko_make_with_layers(
    MOD_MASK_SHIFT, KC_DOT, KC_COLON, 1 << COLEMAK_DH);
const key_override_t num_dot_shift_to_comma_key_override = ko_make_with_layers(
    MOD_MASK_SHIFT, KC_DOT, KC_COMMA, 1 << NUM);


const key_override_t **key_overrides = (const key_override_t *[]){
    &base_comma_shift_to_semicolon_key_override,
    &base_dot_shift_to_colon_key_override,
    &num_dot_shift_to_comma_key_override,
    NULL
};
