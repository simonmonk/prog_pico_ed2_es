from machine import ADC, Pin
from utime import sleep

analogico = ADC(28)

def voltios_desde_lectura(lectura):
    min_lectura = 256
    max_lectura = 65534
    rango_lectura = max_lectura - min_lectura
    voltios_por_lectura = 3.3 / rango_lectura
    voltios = (lectura - min_lectura) * voltios_por_lectura
    return voltios

while True:
    lectura = analogico.read_u16()
    voltios = voltios_desde_lectura(lectura)
    print(f'{lectura} {voltios:.2f}')
    sleep(0.5)
