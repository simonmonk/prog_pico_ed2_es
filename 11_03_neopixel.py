import array
from time import sleep_ms
from machine import Pin
import rp2
from random import randint

NUM_LEDS = 64
MAX_BRILLO = 50

# Inicio del código mágico para Neopixels usando PIO
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(22))
sm.active(1) # Activamos la máquina de estados
pixels = array.array("I", [0 for _ in range(NUM_LEDS)])
# Fin del código mágico para Neopixels usando PIO

def set_led(led, red, green, blue):
    pixels[led] = (red << 16) + (green << 8) + blue

def show():
    sm.put(pixels, 8)

def borrar():
    for i in range(NUM_LEDS):
        set_led(i, 0, 0, 0)
    show()
    
def aleatorio():
    borrar()
    for i in range(NUM_LEDS):
        set_led(i, randint(0, MAX_BRILLO), randint(0, MAX_BRILLO), randint(0, MAX_BRILLO))
        show()
        sleep_ms(5)
    
borrar()

print("Teclea el número del LED que quieres encender")
print("o b-borrar a-aleatorio s-salir")
while True:
    comando = input("comando: ")
    if (comando == 'b'):
        borrar()
    elif (comando == 'a'):
        aleatorio()
    elif (comando == 's'):
        print('Adiós')
        break
    else:
        try:
            led = int(comando)
            set_led(led, MAX_BRILLO, MAX_BRILLO, MAX_BRILLO) # Blanco
            show()
        except:
            pass