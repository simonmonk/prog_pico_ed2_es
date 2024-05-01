from machine import ADC, Pin
from utime import sleep
from math import sqrt

sensor_luz = ADC(28)
lectura_oscuridad = 200
factor_escala = 2.5

def mide_luz():
    lectura = sensor_luz.read_u16()
    porcentaje = int(sqrt(lectura - lectura_oscuridad) / factor_escala)
    if porcentaje < 0:
        porcentaje = 0
    elif porcentaje > 100:
        porcentaje = 100
    return (porcentaje)

while True:
    nivel_luz = mide_luz()
    print(nivel_luz)
    sleep(0.2)