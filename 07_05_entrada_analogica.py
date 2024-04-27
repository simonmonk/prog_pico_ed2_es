from machine import ADC, Pin
from utime import sleep

analogico = ADC(28)

while True:
    lectura = analogico.read_u16()
    print(lectura)
    sleep(0.5)