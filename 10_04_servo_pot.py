from machine import ADC,Pin, PWM
from utime import sleep

servo = PWM(Pin(16))
servo.freq(50) # pulso cada 20ms
min_pulso_us = 500
max_pulso_us = 2500
factor_angulo_pulso = 180/(max_pulso_us-min_pulso_us)

pot = ADC(28)

def set_pulso(pulso_us):
    angulo = (pulso_us - min_pulso_us) * factor_angulo_pulso

    duty = int(pulso_us / 0.305)
    servo.duty_u16(duty)
    return  angulo

while True:
    valor_pot = pot.read_u16()
    pulso_servo = (max_pulso_us - min_pulso_us) * valor_pot/65535 + min_pulso_us
    angulo = set_pulso(pulso_servo)
    print(f'{valor_pot} - {pulso_servo} - {angulo:.1f}',end='\r')
    sleep(0.02)