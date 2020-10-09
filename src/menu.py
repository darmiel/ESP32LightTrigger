from sh1106 import SH1106
from controls import Control, Button, ProgressBar
from time import sleep

import math
import config

class Menu:
    _display: SH1106 = None
    controls: list = []

    def __init__(self, display: SH1106):
        super().__init__()

        self._display = display

    def add(self, control: Control):
        self.controls.append(control)

    # Overwrite this in your menu. 
    # Will be calld before drawing the controls
    def on_draw(self, dp: SH1106):
        pass

    def draw_controls(self, dp: SH1106):
   

        for control in self.controls:
            control.draw(self._display)

    def draw(self, dp: SH1106 = None):
        if dp == None:
            dp = self._display

        self.on_draw(dp)
        self.draw_controls(dp)

#                                               #
# ============================================= #
#                                               #

class MainMenu (Menu):
    delay: int = 10000
    blob: int = 500

    def draw_logo(self, display: SH1106, x: int, y: int) -> None:
        display.pixel(x + 1, y + 0, 1)
        display.pixel(x + 3, y + 0, 1)
        display.pixel(x + 4, y + 0, 1)
        display.pixel(x + 1, y + 1, 1)
        display.pixel(x + 4, y + 1, 1)
        display.pixel(x + 6, y + 1, 1)
        display.pixel(x + 7, y + 1, 1)
        display.pixel(x + 12, y + 1, 1)
        display.pixel(x + 14, y + 1, 1)
        display.pixel(x + 15, y + 1, 1)
        display.pixel(x + 0, y + 2, 1)
        display.pixel(x + 1, y + 2, 1)
        display.pixel(x + 3, y + 2, 1)
        display.pixel(x + 6, y + 2, 1)
        display.pixel(x + 8, y + 2, 1)
        display.pixel(x + 12, y + 2, 1)
        display.pixel(x + 14, y + 2, 1)
        display.pixel(x + 15, y + 2, 1)
        display.pixel(x + 0, y + 3, 1)
        display.pixel(x + 1, y + 3, 1)
        display.pixel(x + 3, y + 3, 1)
        display.pixel(x + 4, y + 3, 1)
        display.pixel(x + 6, y + 3, 1)
        display.pixel(x + 7, y + 3, 1)
        display.pixel(x + 8, y + 3, 1)
        display.pixel(x + 10, y + 3, 1)
        display.pixel(x + 12, y + 3, 1)
        display.pixel(x + 14, y + 3, 1)
        display.pixel(x + 15, y + 3, 1)

    def draw_arrow(self, display: SH1106, x: int, y: int) -> None:
        display.pixel(x + 3, y + 0, 1)
        display.pixel(x + 2, y + 1, 1)
        display.pixel(x + 4, y + 1, 1)
        display.pixel(x + 1, y + 2, 1)
        display.pixel(x + 5, y + 2, 1)
        display.pixel(x + 0, y + 3, 1)
        display.pixel(x + 6, y + 3, 1)
        display.pixel(x + 0, y + 4, 1)
        display.pixel(x + 1, y + 4, 1)
        display.pixel(x + 2, y + 4, 1)
        display.pixel(x + 3, y + 4, 1)
        display.pixel(x + 4, y + 4, 1)
        display.pixel(x + 5, y + 4, 1)
        display.pixel(x + 6, y + 4, 1)
        display.pixel(x + 1, y + 5, 1)
        display.pixel(x + 2, y + 5, 1)
        display.pixel(x + 3, y + 5, 1)
        display.pixel(x + 4, y + 5, 1)
        display.pixel(x + 5, y + 5, 1)
        display.pixel(x + 2, y + 6, 1)
        display.pixel(x + 3, y + 6, 1)
        display.pixel(x + 4, y + 6, 1)
        display.pixel(x + 3, y + 7, 1)

    def draw_camera(self, display: SH1106, x: int, y: int) -> None:
        display.pixel(x + 2, y + 0, 1)
        display.pixel(x + 3, y + 0, 1)
        display.pixel(x + 0, y + 1, 1)
        display.pixel(x + 1, y + 1, 1)
        display.pixel(x + 2, y + 1, 1)
        display.pixel(x + 3, y + 1, 1)
        display.pixel(x + 4, y + 1, 1)
        display.pixel(x + 5, y + 1, 1)
        display.pixel(x + 6, y + 1, 1)
        display.pixel(x + 7, y + 1, 1)
        display.pixel(x + 8, y + 1, 1)
        display.pixel(x + 9, y + 1, 1)
        display.pixel(x + 10, y + 1, 1)
        display.pixel(x + 11, y + 1, 1)
        display.pixel(x + 12, y + 1, 1)
        display.pixel(x + 13, y + 1, 1)
        display.pixel(x + 14, y + 1, 1)
        display.pixel(x + 15, y + 1, 1)
        display.pixel(x + 0, y + 2, 1)
        display.pixel(x + 15, y + 2, 1)
        display.pixel(x + 0, y + 3, 1)
        display.pixel(x + 6, y + 3, 1)
        display.pixel(x + 7, y + 3, 1)
        display.pixel(x + 8, y + 3, 1)
        display.pixel(x + 12, y + 3, 1)
        display.pixel(x + 15, y + 3, 1)
        display.pixel(x + 0, y + 4, 1)
        display.pixel(x + 5, y + 4, 1)
        display.pixel(x + 9, y + 4, 1)
        display.pixel(x + 15, y + 4, 1)
        display.pixel(x + 0, y + 5, 1)
        display.pixel(x + 4, y + 5, 1)
        display.pixel(x + 10, y + 5, 1)
        display.pixel(x + 15, y + 5, 1)
        display.pixel(x + 0, y + 6, 1)
        display.pixel(x + 4, y + 6, 1)
        display.pixel(x + 10, y + 6, 1)
        display.pixel(x + 15, y + 6, 1)
        display.pixel(x + 0, y + 7, 1)
        display.pixel(x + 4, y + 7, 1)
        display.pixel(x + 10, y + 7, 1)
        display.pixel(x + 15, y + 7, 1)
        display.pixel(x + 0, y + 8, 1)
        display.pixel(x + 5, y + 8, 1)
        display.pixel(x + 9, y + 8, 1)
        display.pixel(x + 15, y + 8, 1)
        display.pixel(x + 0, y + 9, 1)
        display.pixel(x + 6, y + 9, 1)
        display.pixel(x + 7, y + 9, 1)
        display.pixel(x + 8, y + 9, 1)
        display.pixel(x + 15, y + 9, 1)
        display.pixel(x + 0, y + 10, 1)
        display.pixel(x + 15, y + 10, 1)
        display.pixel(x + 0, y + 11, 1)
        display.pixel(x + 1, y + 11, 1)
        display.pixel(x + 2, y + 11, 1)
        display.pixel(x + 3, y + 11, 1)
        display.pixel(x + 4, y + 11, 1)
        display.pixel(x + 5, y + 11, 1)
        display.pixel(x + 6, y + 11, 1)
        display.pixel(x + 7, y + 11, 1)
        display.pixel(x + 8, y + 11, 1)
        display.pixel(x + 9, y + 11, 1)
        display.pixel(x + 10, y + 11, 1)
        display.pixel(x + 11, y + 11, 1)
        display.pixel(x + 12, y + 11, 1)
        display.pixel(x + 13, y + 11, 1)
        display.pixel(x + 14, y + 11, 1)
        display.pixel(x + 15, y + 11, 1)

    def __init__(self, display: SH1106):
        super().__init__(display)

        self.draw(display)

    def on_draw(self, display: SH1106) -> None:
        # clear
        display.fill(0)

        # Logo
        self.draw_logo(display, 56, 59)
        display.line(3, 60, 52, 60, 1)
        display.line(75, 60, 124, 60, 1)

        # Delay
        display.text("Delay", 8, 8, 1)
        self.draw_arrow(display, 51, 8)
        delay_len: int = int((math.log10(self.delay) if self.delay > 0 else 0) + 1)
        display.fill_rect(62, 8, delay_len * 8 + 2, 10, 1)
        display.text(str(self.delay), 63, 9, 0)
        display.text("ms", 63 + delay_len * 8 + 2, 9, 1)

        # Blob
        display.text("Blob", 8, 20, 1)
        self.draw_arrow(display, 51, 20)
        blob_len: int = int((math.log10(self.blob) if self.blob > 0 else 0) + 1)
        display.fill_rect(62, 20, blob_len * 8 + 2, 10, 1)
        display.text(str(self.blob), 63, 21, 0)
        display.text("ms", 63 + blob_len * 8 + 2, 21, 1)

        # Test
        test_btn: Button = Button(8, 39, "TEST", width=38, height=13)
        test_btn.hover = False
        test_btn.draw(display)

        # Active
        active_btn: Button = Button(82, 39, "ACT", width=38, height=13)
        active_btn.hover = config.active()
        active_btn.draw(display)

        # Camera
        self.draw_camera(display, 56, 39)

        display.show()

class MessageMenu (Menu):
    value: int = 100
    text: str = None

    def __init__(self, display: SH1106, message: str = "No Message Set."):
        super().__init__(display)
        self.text = message
        self.draw(display)

    # 26
    def draw(self, dp: SH1106 = None):
        if (self.value <= 0):
            return

        print("Draw!")

        if dp == None:
            dp = self._display

        dp.fill(0)
        dp.rect(5, 5, 128 - 5 - 5, 64 - 5 - 5, 1)

        pb: ProgressBar = ProgressBar(7, 52, 113, 5)
        pb.value = self.value
        pb.draw(dp)

        # Text
        txt_len = len(self.text) * 8
        dp.text(self.text, int(128 / 2) - int(txt_len / 2), 26, 1)

        dp.show()

        self.value -= 10
        sleep(.1)

        self.draw(dp)
