from microdot import Microdot
from machine import ADC
import mm_wlan

ssid = 'mi_wifi'
password = 'mi_password'

temp_sensor = ADC(4)
puntos_por_voltio = 3.3 / 65535

index_page = '''
<!DOCTYPE html>
<html>
<head>
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript" charset="utf-8"></script>
  <script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script> 
  <script src="https://cdnjs.cloudflare.com/ajax/libs/justgage/1.6.1/justgage.min.js"></script>
  <script>
  function callback(tempStr, status){
    if (status == "success") {
      temp = parseFloat(tempStr).toFixed(2);
      g.refresh(temp);
      setTimeout(getReading, 1000);
    }
    else {
      alert("There was a problem");
    }
  }
  function getReading(){
    $.get('/temp', callback);
  }
</script>
</head>

<body>
<h1>Temperatura (deg. C)</h1>
<div id="gauge" class="200x160px"></div>

<script>
var g = new JustGage({
    id: "gauge",
    value: 0,
    min: 0,
    max: 100,
});
getReading();
</script>
</body>
</html>
'''

app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

def lee_temp_c():
    lectura = temp_sensor.read_u16() * puntos_por_voltio
    temp_c = 27 - (lectura - 0.706)/0.001721
    return temp_c

@app.route('/')
def index(request):
    return index_page, 400, {'Content-Type': 'text/html'}

@app.route('/temp')
def temp(request):
    return str(lee_temp_c())

app.run(port=80)