from machine import Pin
from utime import sleep
from random import randint

led = Pin('LED', Pin.OUT)

def lanza_dado():
    return randint(1, 6)
    
def parpadeo(veces, espera):
    for x in range(veces):
        led.on()
        sleep(espera)
        led.off()
        sleep(espera)
        
while True:
    input()
    tirada_dado = lanza_dado()
    print(tirada_dado)
    parpadeo(tirada_dado, 0.2)