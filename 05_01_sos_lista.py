from machine import Pin
from utime import sleep

led = Pin('LED', Pin.OUT)
esperas = [0.2, 0.2, 0.2, 0.6, 0.6, 0.6]

while True:
    for espera in esperas:
        led.on()
        sleep(delay)
        led.off()
        sleep(delay)