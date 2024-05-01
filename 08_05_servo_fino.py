from machine import Pin, PWM
from utime import sleep

boton_up = Pin(14, Pin.IN, Pin.PULL_UP)
boton_down = Pin(15, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(16))
servo.freq(50) # pulso cada 20ms
min_pulso_us = 500
max_pulso_us = 2500
factor_angulo_pulso = 180/(max_pulso_us-min_pulso_us)
def set_pulso(pulso_us):
    angulo = (pulso_us - min_pulso_us) * factor_angulo_pulso
    print(f'{pulso_us} - {angulo:.1f}',end='\r')
    # duty 0 to 1023. A 50Hz, cada punto_duty es
    # 20000/65535 = 0.305 microsegundos/punto_duty
    duty = int(pulso_us / 0.305)
    servo.duty_u16(duty)

pulso_actual = (max_pulso_us + min_pulso_us)//2
set_pulso(pulso_actual)

resolucion = 1

while True:
    if boton_up.value() == 0 and pulso_actual < max_pulso_us:
        pulso_actual += resolucion
        set_pulso(pulso_actual)
        #print(angulo)
        sleep(0.01)
    elif boton_down.value() == 0 and pulso_actual > min_pulso_us:
        pulso_actual -= resolucion
        set_pulso(pulso_actual)
        #print(angulo)
        sleep(0.01)
