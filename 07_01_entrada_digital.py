from machine import Pin
from utime import sleep

interruptor = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    print(interruptor.value())
    sleep(0.1)