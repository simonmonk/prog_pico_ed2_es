from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(4, pull=Pin.PULL_UP), 
             scl=Pin(5, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 32, i2c)

h, m, s = (12, 0, 0)

def muestra_hora():
    oled.fill(0)
    tiempo_str = f'{h:02d}:{m:02d}:{s:02d}'
    print(tiempo_str)
    oled.text(tiempo_str, 0, 0, 1)
    oled.show()

def tick(timer):
    global h, m, s
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    muestra_hora()

Timer().init(freq=1, mode=Timer.PERIODIC, callback=tick)