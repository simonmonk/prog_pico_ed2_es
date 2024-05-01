from machine import ADC, Pin
from utime import sleep

pin_analogico = ADC(28)

def voltios_desde_lectura(lectura):
    min_lectura = 256
    max_lectura = 65534
    rango_lectura = max_lectura - min_lectura
    voltios_por_lectura = 3.3 / rango_lectura
    voltios = (lectura - min_lectura) * voltios_por_lectura
    return voltios

while True:
    lectura = pin_analogico.read_u16()
    print(lectura,voltios_desde_lectura(lectura))
    sleep(0.5)
