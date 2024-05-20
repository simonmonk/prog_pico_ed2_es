from machine import Pin, I2C
import mm_wlan
import urequests
import json
from utime import sleep
from ssd1306 import SSD1306_I2C

ssid = 'network'
password = 'password'

clave = 'ea751fc7712f2705=e8a448213b712'
localizacion = 'lat=53.925854&lon=-3.021994'
api_base = 'http://api.openweathermap.org/data/2.5/weather?'
url = api_base + localizacion + '&appid=' + clave
periodo_actualizacion = 60 # segundos

i2c = I2C(0, sda=Pin(4, pull=Pin.PULL_UP), scl=Pin(5, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 32, i2c)

def get_weather():
    if not mm_wlan.is_connected():
        mm_wlan.connect_to_network(ssid, password)
    respuesta = urequests.get(url)
    if respuesta.status_code == 200:
        data = json.loads(respuesta.text)
        description = data['weather'][0]['description']
        # print(data) # imprimir en caso de error
        temp = data['main']['temp'] - 273.15
        return (temp, description)
    else:
        if respuesta.status_code == 401:
            print('No estás autorizado, revisa tu clave')
            exit() # no lo intentamos más
        elif respuesta.status_code == 404:
            print(f'Página no encontrada, revisa tu url: {url}')
            exit() # no lo intentamos más
        elif respuesta.status_code == 500:
            print('El servidor no está listo')
        else:
            print(f'Error: {response.status_code}')
        return(0, 'No disponible')
        
def update_display():
    temp, descripcion = get_weather()
    oled.fill(0)
    temp_str = '{:.1f} deg C'.format(temp)
    oled.text(temp_str, 0, 0, 1)
    oled.text(descripcion, 0, 20, 1)
    oled.show()

while True:
    update_display()
    sleep(periodo_actualizacion)
