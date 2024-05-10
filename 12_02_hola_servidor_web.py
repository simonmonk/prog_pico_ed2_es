from microdot import Microdot
import mm_wlan

ssid = 'Digifibra_4BB8_EXT'
password = 'qazxcvbgtrewsdf26'

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.route('/')
def index(request):
    return 'Hola desde la Pico W'

app.run(port=80)