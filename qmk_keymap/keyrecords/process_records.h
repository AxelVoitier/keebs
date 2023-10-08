// Copyright 2021 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once
#include "lexa.h"


bool process_record_user_keycodes(uint16_t keycode, keyrecord_t *record);
#ifdef OLED_ENABLE
bool process_record_user_oled(uint16_t keycode, keyrecord_t *record);
#endif
#ifdef ENCODER_ENABLE
bool process_record_user_encoders(uint16_t keycode, keyrecord_t *record);
void matrix_scan_user_encoders(void);
#endif
