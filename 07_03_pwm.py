from machine import Pin, PWM

led = PWM(Pin('LED'))

while True:
    brillo_str = input('brillo (0-65534):')
    brillo = int(brillo_str)
    led.duty_u16(brillo)