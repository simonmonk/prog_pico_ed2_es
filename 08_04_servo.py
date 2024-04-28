from machine import Pin, PWM
from utime import sleep

boton_up = Pin(14, Pin.IN, Pin.PULL_UP)
boton_down = Pin(15, Pin.IN, Pin.PULL_UP)

servo = PWM(Pin(16))
servo.freq(50) # pulso cada 20ms

def set_angulo(angulo, min_pulso_us=500, max_pulso_us=2500):
    us_por_grado = (max_pulso_us - min_pulso_us) / 180
    pulso_us = us_por_grado * angulo + min_pulso_us
    # duty 0 to 1023. A 50Hz, cada punto_duty es
    # 20000/65535 = 0.305 microsegundos/punto_duty
    duty = int(pulso_us / 0.305)
    print(angulo)
    servo.duty_u16(duty)

angulo = 90
set_angulo(90)
min_angulo = 0
max_angulo = 180

while True:
    if boton_up.value() == 0 and angulo < max_angulo:
        angulo += 1
        set_angulo(angulo)
        #print(angulo)
        sleep(0.01)
    elif boton_down.value() == 0 and angulo > min_angulo:
        angulo -= 1
        set_angulo(angulo)
        #print(angulo)
        sleep(0.01)