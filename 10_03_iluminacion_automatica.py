from machine import ADC, Pin
from utime import sleep
from math import sqrt

sensor_luz = ADC(28)
pot = ADC(27)

lectura_oscuridad = 200
factor_escala = 2.5

led = Pin('LED', Pin.OUT)

def calcula_porcentaje_luz(lectura_luz):   
    porcentaje = int(sqrt(lectura_luz - lectura_oscuridad) / factor_escala)
    if porcentaje < 0:
        porcentaje = 0
    elif porcentaje > 100:
        porcentaje = 100
    return (porcentaje)

while True:
    lectura_luz = sensor_luz.read_u16()
    porcentaje_luz = calcula_porcentaje_luz(lectura_luz)
    lectura_pot = pot.read_u16()
    porcentaje_pot = int(lectura_pot/65536*100)
    if porcentaje_luz < porcentaje_pot:
        led.on()
    else:
        led.off()
    print(f'Luz: {porcentaje_luz} - Pot: {porcentaje_pot} - {led.value()}')
    sleep(0.2)