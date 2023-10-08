SPACE_CADET_ENABLE = no
GRAVE_ESC_ENABLE = no

NKRO_ENABLE = yes

EXTRAKEY_ENABLE = yes
UNICODE_ENABLE = yes
KEY_OVERRIDE_ENABLE = yes

DYNAMIC_TAPPING_TERM_ENABLE = yes
AUTO_SHIFT_ENABLE = yes

SRC += $(USER_PATH)/keyrecords/process_records.c \
	   $(USER_PATH)/keyrecords/keycodes.c

ifeq ($(strip $(KEY_OVERRIDE_ENABLE)),yes)
	SRC += $(USER_PATH)/keyrecords/key_overrides.c
endif

ifeq ($(strip $(TAP_DANCE_ENABLE)),yes)
	SRC += $(USER_PATH)/keyrecords/tap_dances.c
endif

ifeq ($(strip $(OLED_ENABLE)),yes)
	SRC += $(USER_PATH)/oled.c
endif

ifeq ($(strip $(ENCODER_ENABLE)),yes)
	SRC += $(USER_PATH)/encoders.c
endif
