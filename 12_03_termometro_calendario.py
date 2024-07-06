from machine import ADC
from microdot import Microdot
import mm_wlan

ssid = 'mi_wifi'
password = 'mi_password'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password,verbose=False)

print(f'Conéctate a http://{mm_wlan.get_ip()}')


temp_sensor = ADC(4)
puntos_por_voltio = 3.3 / 65535

def lee_temp_c():
    lectura = temp_sensor.read_u16() * puntos_por_voltio
    temp_c = 27 - (lectura - 0.706)/0.001721
    # formateamos la temperatura con 1 decimal
    return f'{temp_c:3.1f}'

index_html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Termómetro y calendario web</title>
        <meta http-equiv="refresh" content="5" >
    </head>
<body>
    <h1>{}</h1>
    <br/>
    <h3>{}</h3>
</body>
</html>
'''

import time

dias_semana = ('lunes', 'martes', 'miércoles.', 'jueves','viernes', 'sábado', 'domingo')

def get_hora():
    año,mes,dia,hora,minuto,segundo,dia_semana,dia_año = time.localtime()
    
    fecha_str = f'{dia:02d}/{mes:02d}/{año}'
    tiempo_str = f'{hora:02d}:{minuto:02d}:{segundo:02d}'
    dia_str = f'{dia_año}/365'
    
    return f'{tiempo_str} {dias_semana[dia_semana]} {fecha_str} {dia_str}'

@app.route('/')
def index(request):
    return index_html.format(lee_temp_c(),get_hora()), 200, {'Content-Type': 'text/html'}

app.run(port=80)