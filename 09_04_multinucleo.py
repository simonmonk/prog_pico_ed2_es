from machine import Pin
from utime import sleep
import _thread

interruptor = Pin(10, Pin.IN, Pin.PULL_UP)

def nucleo0():
    x = 0
    while True:
        x += 1
        print(x)
        sleep(1)

def nucleo1():
    while True:
        if interruptor.value() == 0:
           print('botón pulsado')
           sleep(0.1)
           
_thread.start_new_thread(nucleo1, ( ))
nucleo0()