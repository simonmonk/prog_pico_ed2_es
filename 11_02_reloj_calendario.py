from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
from time import localtime

i2c = I2C(0, sda=Pin(4, pull=Pin.PULL_UP), 
             scl=Pin(5, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 32, i2c)

dias_semana = ('lunes','martes','mierco.','jueves','viernes','sábado','domingo')

CHAR_SIZE = 8 

def muestra_tiempo_sistema(timer):
    oled.fill(0)
    año, mes, dia, hora, minuto, segundo, dia_semana, dia_año = localtime()
    
    fecha_str = f'{dia:02d}/{mes:02d}/{año}'
    tiempo_str = f'{hora:02d}:{minuto:02d}:{segundo:02d}'
    dia_str = f'{dias_semana[dia_semana]} {dia_año}/365'
    print(tiempo_str, fecha_str,dia_str, end ='\r')
    oled.text(tiempo_str, 3 * CHAR_SIZE, 0, 1)
    oled.text(fecha_str, 2 * CHAR_SIZE, CHAR_SIZE, 1)
    oled.text(dia_str, 1 * CHAR_SIZE, CHAR_SIZE * 2, 1)    
    oled.show()

Timer().init(freq=1, mode=Timer.PERIODIC, callback=muestra_tiempo_sistema)