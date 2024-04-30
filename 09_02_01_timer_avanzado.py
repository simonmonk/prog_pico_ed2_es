from machine import Pin, Timer
from utime import  sleep

led = Pin('LED', Pin.OUT)

numero_parpadeos = 0

def tick(timer):
    global numero_parpadeos
    led.toggle()
    numero_parpadeos += 1

frecuencia_parpadeo = 10

mi_temporizador = Timer()
mi_temporizador.init(freq=frecuencia_parpadeo, mode=Timer.PERIODIC, callback=tick) # 10 parpadeos por segundo

x = 0

x_final = 10
pausa = 1.2
while x < x_final:
    print(x)
    x += 1
    sleep(pausa)

mi_temporizador.deinit()
# debe salir pausa * x_final * frecuencia_parpadeo
print(f'Se acabó el parpadeo tras {numero_parpadeos}')