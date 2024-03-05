from machine import Pin
from utime import sleep

led = Pin('LED', Pin.OUT)

def parpadeo(veces, espera):
    for x in range(veces):
        led.on()
        sleep(espera)
        led.off()
        sleep(espera)
    return veces * espera * 2

while True:
    print(parpadeo(3, 0.2))
    sleep(0.4)
    print(parpadeo(3, 0.6))