#pragma once

#define TAPPING_TERM 200
#define PERMISSIVE_HOLD
// #define HOLD_ON_OTHER_KEY_PRESS
#define HOLD_ON_OTHER_KEY_PRESS_PER_KEY

#ifdef AUTO_SHIFT_ENABLE
    // #define AUTO_SHIFT_TIMEOUT 150
    #define AUTO_SHIFT_MODIFIERS
    #define NO_AUTO_SHIFT_SYMBOLS
    #define NO_AUTO_SHIFT_NUMERIC
    #define AUTO_SHIFT_REPEAT
#endif // AUTO_SHIFT_ENABLE

#define LAYER_STATE_8BIT

#ifdef UNICODE_COMMON_ENABLE
    #define UNICODE_SELECTED_MODES UNICODE_MODE_LINUX
#endif // UNICODE_COMMON_ENABLE

#ifdef SPLIT_KEYBOARD
    #ifdef OLED_ENABLE
        #define SPLIT_LAYER_STATE_ENABLE
        #define SPLIT_MODS_ENABLE

        #ifdef OLED_ON_SLAVE
            #define SPLIT_OLED_ENABLE

            #if defined(LED_NUM_LOCK_PIN) || defined(LED_CAPS_LOCK_PIN) || defined(LED_SCROLL_LOCK_PIN) || defined(LED_COMPOSE_PIN) || defined(LED_KANA_PIN)
                #define SPLIT_LED_STATE_ENABLE
            #endif // LED_NUM_LOCK_PIN || LED_CAPS_LOCK_PIN || LED_SCROLL_LOCK_PIN || LED_COMPOSE_PIN || LED_KANA_PIN

            #ifdef WPM_ENABLE
                #define SPLIT_WPM_ENABLE
            #endif // WPM_ENABLE
        #endif // OLED_ON_SLAVE
    #endif // OLED_ENABLE

    #if defined(POINTING_DEVICE_ENABLE) && defined(POINTING_DEVICE_ON_SLAVE)
        #define SPLIT_POINTING_ENABLE
    #endif // POINTING_DEVICE_ENABLE && POINTING_DEVICE_ON_SLAVE

    #if defined(HAPTIC_ENABLE) && defined(HAPTIC_ON_SLAVE)
        #define SPLIT_HAPTIC_ENABLE
    #endif // HAPTIC_ENABLE && HAPTIC_ON_SLAVE
#endif // SPLIT_KEYBOARD


#ifdef OLED_ENABLE
    #define OLED_TIMEOUT 15000
#endif // OLED_ENABLE


#ifdef POINTING_DEVICE_ENABLE
#endif // POINTING_DEVICE_ENABLE


#ifdef NKRO_ENABLE
    #define FORCE_NKRO
#endif // NKRO_ENABLE
