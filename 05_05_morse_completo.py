from machine import Pin
from utime import sleep

led = Pin('LED', Pin.OUT)

duracion_punto = 0.2
duracion_raya = duracion_punto * 3
espera_entre_caracteres = duracion_punto * 3
espera_entre_palabras = duracion_punto * 7

duraciones = {'.' : duracion_punto, '-' : duracion_raya}

codigos_morse = {
    'a' : '.-',   'b' : '-...',  'c' : '-.-.',
    'd' : '-..',  'e' : '.',     'f' : '..-.',
    'g' : '--.',  'h' : '....',  'i' : '..',
    'j' : '.---', 'k' : '-.-',   'l' : '.-..',
    'm' : '--',   'n' : '-.',    'o' : '---',
    'p' : '.--.', 'q' : '--.-',  'r' : '.-.',
    's' : '...',  't' : '-',     'u' : '..-',
    'v' : '...-', 'w' : '.--',   'x' : '-..-',
    'y' : '-.--', 'z' : '--..'
}

def envia_pulso(punto_o_raya):
    espera = duraciones[punto_o_raya]
    led.on()
    sleep(espera)
    led.off()
    sleep(espera)

def envia_morse_letra(caracter):
    if caracter == ' ':
        sleep(espera_entre_palabras)
        print('espacio')
    else:
        puntos_y_rayas = codigos_morse.get(caracter.lower())
        if puntos_y_rayas:
            print(caracter + ' ' + puntos_y_rayas)

            for pulso in puntos_y_rayas:
                envia_pulso(pulso)
                sleep(espera_entre_caracteres)
        else:
            print('caracter desconocido: ' + caracter)
            
while True:
    texto = input('Mensaje: ')
    for caracter in texto:
        envia_morse_letra(caracter)