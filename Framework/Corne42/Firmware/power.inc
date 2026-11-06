// SPDX-License-Identifier: GPL-2.0-or-later
// GPIO0 is the Framework SLEEP# input; USB suspend is an independent sleep cause.
// Hardware gating does not establish RP2040 whole-board low-power compliance.
static volatile bool corne42_usb_suspended = false;

static void corne42_apply_sleep_state(void) {
#ifdef LED_MATRIX_ENABLE
    const bool sleeping = corne42_usb_suspended || !gpio_read_pin(GP0);
    led_matrix_set_suspend_state(sleeping);
    gpio_write_pin(IS31FL3733_SDB_PIN, !sleeping);
#endif
}

void keyboard_post_init_kb(void) {
    gpio_set_pin_input(GP0);
#ifdef LED_MATRIX_ENABLE
    gpio_set_pin_output(IS31FL3733_SDB_PIN);
#endif
    corne42_apply_sleep_state();
    keyboard_post_init_user();
}

void housekeeping_task_kb(void) {
    corne42_apply_sleep_state();
    // QMK invokes housekeeping_task_user separately after this hook.
}

void suspend_power_down_kb(void) {
    corne42_usb_suspended = true;
    corne42_apply_sleep_state();
    suspend_power_down_user();
}

void suspend_wakeup_init_kb(void) {
    corne42_usb_suspended = false;
    corne42_apply_sleep_state();
    suspend_wakeup_init_user();
}
