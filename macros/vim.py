# MACROPAD Hotkeys
from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Vim', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Save', [Keycode.ESCAPE, ':w', Keycode.ENTER]),
        (0x004000, 'Quit', [Keycode.ESCAPE, ':q', Keycode.ENTER]),
        (0x400040, 'Pair []', [Keycode.ESCAPE, '%']),
        # 2nd row ----------
        (0x004040, 'SOF', [Keycode.ESCAPE, 'gg']),
        (0x004040, 'EOF', [Keycode.ESCAPE, 'G']),
        (0x400000, 'Pg up', [Keycode.ESCAPE, Keycode.CONTROL, 'u']),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'SOL', [Keycode.ESCAPE, '0']),
        (0x000040, 'EOL', [Keycode.ESCAPE, '$']),
        (0x400000, 'Pg down', [Keycode.ESCAPE, Keycode.CONTROL, 'd']),
        # 4th row ----------
        (0x202000, '5 L', [Keycode.ESCAPE, '5h']), # adafruit.com in a new tab
        (0x202000, '5 R', [Keycode.ESCAPE, '5l']),     # dev mode
        (0x101010, 'quickref', [Keycode.ESCAPE, ':help quickref', Keycode.ENTER]),     # digikey in a new tab
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
