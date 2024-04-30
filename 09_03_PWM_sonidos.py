from machine import Pin, PWM
from time import sleep


buzzer_pin = PWM(Pin(15))

tono = 55 # La bajo
for escala in range(1,11):
    buzzer_pin.freq(tono) 
    print(f'escala: {escala}  frecuencia: {tono}')
    buzzer_pin.duty_u16(32768) # 50%
    sleep(1)
    tono = tono * 2

buzzer_pin.deinit()
    