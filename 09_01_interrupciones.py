from machine import Pin
from utime import sleep

boton = Pin(14, Pin.IN, Pin.PULL_UP)

def gestiona_boton_down(ignore):
    print('BOTÓN PULSADO')
    sleep(0.2)


boton.irq(gestiona_boton_down, Pin.IRQ_FALLING)

i = 0

while True:
    i += 1
    print(i)
    sleep(0.2)