from machine import Pin
from utime import sleep
import _thread

button_L = Pin(17,Pin.IN,Pin.PULL_DOWN)
button_R = Pin(14,Pin.IN,Pin.PULL_DOWN)
buildin_led = Pin(25,Pin.OUT)
external_led = Pin(15,Pin.OUT)

def led_blink():
    while True:
        buildin_led.toggle()
        sleep(0.5)
_thread.start_new_thread(led_blink,())

def button_clicked(pin):
    if pin.value() == 1:
        sleep(0.1)
        while pin.value() == 1:
            pass
        return True
    else:
        return False
    
while True:
    if button_clicked(button_R):
        external_led.value(1)
        print("R click")
    if button_clicked(button_L):
        external_led.value(0)
        print("L click")