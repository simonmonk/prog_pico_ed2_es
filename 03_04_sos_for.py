from machine import Pin
from utime import sleep
led = Pin('LED', Pin.OUT)
while True:
    # Este bucle hace 3 puntos (S)
    for x in range(3):
        led.on()
        sleep(0.2)
        led.off()
        sleep(0.2)
    sleep(0.4) # Esperamos entre S y O
    # Este bucle hace 3 rayas (O)
    for x in range(3):
        led.on()
        sleep(0.6)
        led.off()
        sleep(0.6)aw       as