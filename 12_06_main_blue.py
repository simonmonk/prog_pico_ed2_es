# Import necessary modules
from machine import Pin , ADC
import bluetooth
from led_periferico_ble import BLESimplePeripheral

# Creamos un objeto  Bluetooth Low Energy (BLE)
ble = bluetooth.BLE()

# Creamos un instance of the BLESimplePeripheral class with the BLE object
sp = BLESimplePeripheral(ble)

# Create a Pin object for the onboard LED, configure it as an output
led = Pin("LED", Pin.OUT)


temp_sensor = ADC(4)

puntos_por_voltio = 3.3 / 65535

def leer_temp_c():
    lectura = temp_sensor.read_u16() * puntos_por_voltio
    temp_c = 27 - (lectura - 0.706)/0.001721
    return temp_c

# Define a callback function to handle received data
def on_rx(data):
    print("Datos recibidos: ", data)  # Mostramos los datos recibidos
    global led_state  
    if data == b'on\r\n':  # comando para encender el LED
        led.on()
        sp.send('On\r\n')
    elif data == b'off\r\n': # comando para apagar el LED
        led.off()
        sp.send('Off\r\n')
    elif data == b'inv\r\n': # comando para invertir el LED
        led.toggle()
        sp.send(f'LED: {led.value()}\r\n')
    elif data == b'temp\r\n': # comando temperatura
        sp.send(f'{leer_temp_c():.1f}\r\n')
         
# Start an infinite loop
while True:
    if sp.is_connected():  # Check if a BLE connection is established
        sp.on_write(on_rx)  # Set the callback function for data reception