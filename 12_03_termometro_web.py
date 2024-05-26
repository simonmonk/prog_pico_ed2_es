from microdot import Microdot
from machine import ADC
import mm_wlan

ssid = 'mi_wifi'
password = 'mi_password'

temp_sensor = ADC(4)
puntos_por_voltio = 3.3 / 65535

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

def lee_temp_c():
    lectura = temp_sensor.read_u16() * puntos_por_voltio
    temp_c = 27 - (lectura - 0.706)/0.001721
    return temp_c

@app.route('/')
def index(request):
    return f'Temperatura: {lee_temp_c():.1f}'

app.run(port=80)
