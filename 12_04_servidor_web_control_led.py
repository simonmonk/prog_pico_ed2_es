from microdot import Microdot
import mm_wlan

from machine import Pin
led = Pin('LED', Pin.OUT)

ssid = 'Digifibra_4BB8_EXT'
password = 'qazxcvbgtrewsdf26'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password,verbose=False)

print(f'Conéctate a http://{mm_wlan.get_ip()}')

def estado_led():
    if led.value():
        return '<img src="https://img.icons8.com/?size=80&id=e9V-XJYOmiTY&format=png"/> <br/> Led encendido <a href="/off">Apagar</a>'
    else:
        return '<img src="https://img.icons8.com/?size=80&id=30144&format=png"/> <br/> Led apagado  <a href="/on">Encender</a>'

index_html = '''
<!DOCTYPE html>
<html>
    <head>
        <title>Led Control</title>
    </head>
<body>
    <h1>{}</h1>
</body>
</html>
'''

     
def get_web():
    return index_html.format(estado_led()), 200, {'Content-Type': 'text/html'}

@app.route('/on')
def on(request):
    led.on()
    return get_web()
    

@app.route('/off')
def off(request):
    led.off()
    return get_web()

@app.route('/')
def index(request):
    return get_web()

app.run(port=80)