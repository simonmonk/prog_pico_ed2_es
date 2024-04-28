from machine import Pin, PWM
from utime import sleep

rojo_ch = PWM(Pin(16), 1000)
verde_ch = PWM(Pin(17), 1000)
azul_ch = PWM(Pin(15), 1000)
boton = Pin(12, Pin.IN, Pin.PULL_UP)
colores = [[255, 0, 0], [127, 127, 0],
    [0, 255, 0], [0, 127, 127],
    [0, 0, 255], [127, 0, 127]]

def set_color(rgb):
    rojo_ch.duty_u16(rgb[0] * 256)
    verde_ch.duty_u16(rgb[1] * 256)
    azul_ch.duty_u16(rgb[2] * 256)

indice = 0
set_color(colores[indice])

while True:
    if boton.value() == 0:
        indice +=1
        if indice >= len(colores):
            indice = 0
        sleep(0.2)
    set_color(colores[indice])
