from machine import Pin, PWM

led = PWM(Pin('LED'),1000)

while True:
    brillo_str = input('brillo (0-100):')
    brillo = int(int(brillo_str) * 65534 / 100)
    led.duty_u16(brillo)