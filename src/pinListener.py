import config

from time import sleep
from machine import Pin
from menu import MessageMenu

def callback_switch_pin(pin: Pin) -> None:
    new_value: int = pin.value()

    # Duplicate -> Ignore
    if config.UPDATE_BUTTON_MODES['cur'] == new_value:
        return

    # New value
    config.UPDATE_BUTTON_MODES['cur'] = new_value

    # Broadcast new mode
    MessageMenu(config.DISPLAY, "Mode: " +
                config.UPDATE_BUTTON_MODES[str(new_value)])

    # After message reset to main menu
    config.MAIN_MENU.draw()


SWITCH_PIN: Pin = Pin(5, Pin.IN, Pin.PULL_DOWN)
SWITCH_PIN.irq(trigger=Pin.IRQ_FALLING, handler=callback_switch_pin)


def callback_button_up(pin: Pin) -> None:
    new_value: int = pin.value()
    if not new_value:
        return
    if config.UPDATE_BUTTON_MODES['cur'] == 0:
        config.delay(config.delay()+10)
    elif config.UPDATE_BUTTON_MODES['cur'] == 1:
        config.blob(config.blob() + 10)
    else:
        print("Not implemented.")


def callback_button_down(pin: Pin) -> None:
    new_value: int = pin.value()
    if not new_value:
        return
    if config.UPDATE_BUTTON_MODES['cur'] == 0:
        config.delay(config.delay()-10)
    elif config.UPDATE_BUTTON_MODES['cur'] == 1:
        config.blob(config.blob() - 10)
    else:
        print("Not implemented.")


VOL_UP_BTN: Pin = Pin(17, Pin.IN, Pin.PULL_DOWN)
VOL_UP_BTN.irq(trigger=Pin.IRQ_FALLING, handler=callback_button_up)

VOL_DWN_BTN: Pin = Pin(16, Pin.IN, Pin.PULL_DOWN)
VOL_DWN_BTN.irq(trigger=Pin.IRQ_FALLING, handler=callback_button_down)

RELAY: Pin = Pin(18, Pin.OUT)

def exec_camera_shutter() -> None:
    config.MAIN_MENU.hover_test(hover=True, dp=config.DISPLAY)

    print("Exec: Waiting for delay...")

    # wait delay
    if config.delay() > 0:
        sleep(config.delay()/1000.0)
            
    print("Exec: Waiting for blob...")
    # trigger relay
    RELAY.on()
    sleep(config.blob()/1000.0)
    RELAY.off()
    print("Exec: Done! Everything (should) have worked.")

    config.MAIN_MENU.hover_test(hover=False, dp=config.DISPLAY)

def callback_light_sensor(pin: Pin) -> None:
   
    new_value: int = not pin.value()
    if config.LIGHT_SENSOR_STATE == new_value:
        return

    config.LIGHT_SENSOR_STATE = new_value
    print("Light-Sensor: " + str(new_value))

    # check if even active
    if not config.active():
        return

    # If there's no more light, execute all this shiet
    if not config.LIGHT_SENSOR_STATE:
        exec_camera_shutter()

LIGHT_SENSOR: Pin = Pin(19, Pin.IN, Pin.PULL_UP)
LIGHT_SENSOR.irq(trigger=Pin.IRQ_FALLING, handler=callback_light_sensor)

def callback_active_jumper (pin: Pin) -> None:
    value: bool = True if pin.value() else False

    if config.active() == value:
        return

    config.active(value)

ACTIVE_PIN: Pin = Pin(4, Pin.IN, Pin.PULL_DOWN)
ACTIVE_PIN.irq(trigger=Pin.IRQ_FALLING, handler=callback_active_jumper)

def callback_test_pin(pin: Pin) -> None:
    print("callback test pin")
    if pin.value():
        exec_camera_shutter()

TEST_PIN: Pin = Pin(0, Pin.IN, Pin.PULL_DOWN)
TEST_PIN.irq(trigger=Pin.IRQ_FALLING, handler=callback_test_pin)