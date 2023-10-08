// Copyright 2023 Axel Voitier (@Axel Voitier)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#include QMK_KEYBOARD_H

enum userspace_layers {
    COLEMAK_DH=0,
    SYM1,
    SYM2,
    NUM,
    MATH,
    NAV,
    FUN,
    MEDIA,
};


#include "keyrecords/keycodes.h"
#include "keyrecords/process_records.h"

#ifdef TAP_DANCE_ENABLE
    #include "keyrecords/tap_dances.h"
#endif

#if defined(OLED_ENABLE)
    // #include "oled.h"
#endif
