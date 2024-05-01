from machine import Pin, ADC
from utime import sleep

temp_sensor = ADC(4)

puntos_por_voltio = 3.3 / 65535

def leer_temp_c():
    lectura = temp_sensor.read_u16() * puntos_por_voltio
    temp_c = 27 - (lectura - 0.706)/0.001721
    return temp_c

while True:
    temp_c = leer_temp_c()
    print(f'{temp_c:.1f}')
    sleep(0.5)