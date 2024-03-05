from machine import Pin
from utime import sleep
from random import randint

led = Pin('LED', Pin.OUT)

def lanza_dado(num_dados=1):
    total = 0
    for x in range(num_dados):
        total += randint(1, 6)
    return total

def parpadeo(veces, espera):
    for x in range(veces):
        led.on()
        sleep(espera)
        led.off()
        sleep(espera)
        
while True:
    input()
    tirada_dado = lanza_dado(num_dados=2)
    print(tirada_dado)
    parpadeo(tirada_dado, 0.2)

