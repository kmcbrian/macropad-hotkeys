# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Number Pad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004040, '7', ['7']), (0x002060, '8', ['8']), (0x000080, '9', ['9']),
        # 2nd row ----------
        (0x207000, '4', ['4']), (0x008000, '5', ['5']), (0x006020, '6', ['6']),
        # 3rd row ----------
        (0x701000, '1', ['1']), (0x603000, '2', ['2']), (0x405000, '3', ['3']),
        # 4th row ----------
        (0x300030, '.', ['.']), (0x800000, '0', ['0']), (0x300030, 'Tab', [Keycode.TAB]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
