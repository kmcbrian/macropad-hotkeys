# MACROPAD Hotkeys example: Minecraft hotbar (inventory)

# Note: Must enable "full keyboad gameplay" for Prev/Next buttons to work.
#       This is found under "settings", then "keyboard and mouse".

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                          # REQUIRED dict, must be named 'app'
    'name' : 'Minecraft', # Application name
    'macros' : [                 # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x206000, 'Esc', [Keycode.ESCAPE]),
        (0x008000, 'Zoom', [{'persistant':6}]),
        (0x007010, 'Debug', [0x3C,'g',0x3C,'b',-0x3C]),
        # 2nd row ----------
        (0x402000, 'F3', [0x3C]),
        (0x800005, 'w', [{'persistant':26}]), # 26 = 'w'
        (0x402000, 'Inv', ['e']),
        # 3rd row ----------
        (0x800005, 'a', [{'persistant':4}]), #4 = 'a' 
        (0x800005, 's', [{'persistant':22}]), #
        (0x800005, 'd', [{'persistant':7}]),
        # 4th row ----------
        (0x501000, 'Shift', [Keycode.LEFT_SHIFT]),
        (0x501010, 'Swap', ['f']),
        (0x501030, 'Jump', [Keycode.SPACEBAR]),
        # Encoder button ---
        (0x000000, '', [])
    ]
} # 4weaaaaaaaaaaaaasssssssssasddddddasdddddddddddddddddd