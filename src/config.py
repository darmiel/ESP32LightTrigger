from menu import MainMenu
from sh1106 import SH1106

_ACTIVE: bool = False
_DELAY: int = 500
_BLOB: int = 1000

MAIN_MENU: MainMenu = None
DISPLAY: SH1106 = None

# 0 _ Delay
# 1 _ Blob
# UPDATE_BUTTONS_MODE: int = 0
UPDATE_BUTTON_MODES: dict = {
    'cur': 0,
    '0': 'Delay',
    '1': 'Blob'
}

LIGHT_SENSOR_STATE: bool = False

def active(new_value: bool = None) -> bool:
    global _ACTIVE

    if new_value != None:
        _ACTIVE = new_value

        if MAIN_MENU != None:
            MAIN_MENU.active = _ACTIVE
            MAIN_MENU.draw()
    
    return _ACTIVE

def delay(new_value: int = None) -> int:
    global _DELAY

    if new_value != None:
        print("Update new val to " + str(new_value))
        _DELAY = new_value

        if MAIN_MENU != None:
            MAIN_MENU.delay = _DELAY
            MAIN_MENU.draw()
    
    return _DELAY

def blob(new_value: int = None) -> int:
    global _BLOB

    if new_value != None:
        _BLOB = new_value

        if MAIN_MENU != None:
            MAIN_MENU.blob = _BLOB
            MAIN_MENU.draw()
    
    return _BLOB