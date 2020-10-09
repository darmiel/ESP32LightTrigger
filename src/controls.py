import math
from sh1106 import SH1106

class Control:
    _display: SH1106 = None

    x: int = 0
    y: int = 0

    end_x: int = 0
    end_y: int = 0

    awd = False

    def __init__(self, x: int, y: int, display: SH1106 = None):
        super().__init__()

    def draw(self, dp: SH1106 = _display) -> None:
        print("Draw for component not implemented yet.")


class Switch (Control):

    value: bool = False

    x: int = None
    y: int = None
    color: int = None

    end_x: int = None
    end_y: int = None

    def __init__(self, x: int, y: int, default_value: bool = False, color: int = 1, display: SH1106 = None):
        super().__init__(x, y, display=display)

        self._display = display

        self.value = default_value

        self.x = x
        self.y = y
        self.color = color

        # set end vars
        self.end_x = self.x + 15
        self.end_y = self.y + 8

    def draw(self, dp: SH1106 = None) -> None:
        if dp == None:
            dp = self._display

        dp.rect(self.x, self.y, 15, 8, self.color)  # outer rect
        dp.line(self.x + 7, self.y, self.x + 7,
                self.y + 7, self.color)  # seperator

        # switch off
        if not self.value:
            dp.rect(self.x + 2, self.y + 2, 4, 4, self.color)
        else:
            dp.fill_rect(self.x + 9, self.y + 2, 4, 4, self.color)


class ProgressBar (Control):
    value: int = 0  # from 0 to 100
    style: int = 1  # select from 1 to 2

    x: int = None
    y: int = None
    width: int = None
    height: int = None
    color: int = None

    end_x: int = None
    end_y: int = None

    def __init__(self, x: int, y: int, width: int, height: int, color: int = 1, display: SH1106 = None):
        super().__init__(x, y, display=display)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        # set end vars
        self.end_x = self.x + self.width
        self.end_y = self.y + self.height

    def __draw_rect(self, dp: SH1106 = None) -> None:
        if dp == None:
            dp = self._display
        dp.rect(self.x, self.y, self.width, self.height, self.color)

    def __get_width(self, possible: int):
        value: int = max(0, min(100, self.value))

        res: int = math.ceil((possible / 100.0) * value)
        res = min(possible, res)  # max. possible
        res = max(0, res)  # min. 0

        return res

    def __draw_v1(self, dp: SH1106 = None) -> None:
        if dp == None:
            dp = self._display

        self.__draw_rect(dp=dp)
        dp.fill_rect(self.x + 1, self.y + 1,
                     self.__get_width(self.width - 2), self.height - 2, self.color)

    def __draw_v2(self, dp: SH1106 = None) -> None:
        if dp == None:
            dp = self._display

        self.__draw_rect(dp=dp)
        dp.fill_rect(self.x + 2, self.y + 2,
                     self.__get_width(self.width - 4), self.height - 4, self.color)

    def draw(self, dp: SH1106 = None) -> None:
        if self.style == 1:
            self.__draw_v1(dp=dp)
        elif self.style == 2:
            self.__draw_v2(dp=dp)
        else:
            print("Style {} for progressbar not found".format(self.style))


class Button (Control):
    _display: SH1106 = None

    text: str = None

    hover: bool = False

    x: int = None
    y: int = None

    _text_x = None

    width: int = None
    height: int = None

    end_x: int = None
    end_y: int = None

    def __init__(self, x: int, y: int, text: str, width: int = 0, height: int = 0, px: int = 0, py: int = 0, display: SH1106 = None):
        super().__init__(x, y, display=display)

        self._display = display

        self.text = text

        self.x = x
        self.y = y

        self._text_x = len(text) * 9  # 1 char = 8px x 8px + 1px space

        self.width = width
        self.height = height

        if self.width < (self._text_x + 4):
            self.width = self._text_x + 4

        if self.height < (8 + 4):
            self.height = 8 + 4

        self.width += 2 * px
        self.height += 2 * py

        # set end vars
        self.end_x = self.x + self.width
        self.end_y = self.y + self.height

    def draw(self, dp: SH1106 = None) -> None:
        if dp == None:
            dp = self._display

        dp.rect(self.x, self.y, self.width, self.height, 1)

        if self.hover:
            dp.fill_rect(
                self.x + 2, self.y + 2, self.width - 4, self.height - 4, 1)

        text_x: int = int((2 * self.x + self.width) / 2) - \
            int(self._text_x / 2) + 1
        text_y: int = int((2 * self.y + self.height) / 2) - int(8 / 2) + 1

        dp.text(self.text, text_x, text_y,
                           1 if not self.hover else 0)
