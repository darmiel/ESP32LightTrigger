from controls import Switch, ProgressBar, Button

from machine import Pin, I2C
from sh1106 import SH1106, SH1106_I2C

import json

i2c: I2C = I2C(scl = Pin(22), sda = Pin(21), freq=400000)
display: SH1106 = SH1106_I2C (128, 64, i2c, addr = 0x3c)

display.sleep(False)

# black background
display.fill(0)

active_button: Button = Button(display, 5, 5, "Akt", px = 1, py = 1)
active_button.hover = True
active_button.draw()

print(active_button.__dict__)

inactive_button: Button = Button(display, active_button.end_x + 5, 5, "Akt", px = 1, py = 1)
inactive_button.hover = False
inactive_button.draw()

print(inactive_button.__dict__)

display.show()