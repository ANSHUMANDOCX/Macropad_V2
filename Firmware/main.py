print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8)
keyboard.row_pins = (board.D5, board.D4, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
layer = Layers()

keyboard.modules.append(encoder_handler)
keyboard.modules.append(MediaKeys())
keyboard.modules.append(layer)

TRANS = KC.TRANS
RAISE = KC.LT(1,KC.ESC)
RAISE1 = KC.LT(2,KC.F)
#RAISE = KC.DF(1)
#DOWN = KC.DF(0)

encoder_handler.pins = ((board.D2, board.D1, board.D0),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),)
]

keyboard.keymap = [
    [#Layer 0
        RAISE, KC.BACKSPACE, KC.PSCR,
        RAISE1, KC.ENTER, KC.LGUI(KC.TAB),
        KC.LEFT, KC.SPACE, KC.RIGHT
    ],
    [#Layer 1
        TRANS,KC.LCTRL(KC.Y),KC.LALT(KC.F4),
        KC.LCTRL(KC.C),KC.LCTRL(KC.V),KC.LCTRL(KC.Z),
        KC.MPRV,KC.MPLY,KC.MNXT,
    ],
    [
        KC.X,KC.LALT,KC.TAB,
        TRANS,KC.W,KC.UP,
        KC.A,KC.X,KC.DOWN
    ]
]

if __name__ == '__main__':
    keyboard.go()