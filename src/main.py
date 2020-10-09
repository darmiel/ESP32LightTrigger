from machine import Pin, SoftI2C
from sh1106 import SH1106, SH1106_I2C

from menu import MainMenu

from time import sleep
from time import time

import config

#
# Create Display
#
i2c: SoftI2C = SoftI2C(scl = Pin(22), sda = Pin(21), freq=400000)
config.DISPLAY = SH1106_I2C (128, 64, i2c, addr = 0x3c)
config.DISPLAY.sleep(False)

#
# Create Menu
#
config.MAIN_MENU = MainMenu(config.DISPLAY)

# Impoprt pin listeners
import pinListener