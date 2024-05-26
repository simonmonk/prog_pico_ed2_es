from microdot import Microdot
import mm_wlan

ssid = 'mi_wifi'
password = 'mi_password'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hola desde la Pico W'

app.run(port=80)