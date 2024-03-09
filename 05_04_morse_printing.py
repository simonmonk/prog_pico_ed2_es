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

def envia_morse_letra(caracter):
    if caracter == ' ':
        print('espacio')
    else:
        puntos_y_rayas = codigos_morse.get(caracter.lower())
        if puntos_y_rayas:
            print(caracter + ' ' + puntos_y_rayas)
        else:
            print('caracter desconocido: ' + caracter)
            
while True:
    texto = input('Mensaje: ')
    for caracter in texto:
        envia_morse_letra(caracter)