nombre_fichero = 'testXX.txt'
try:
    f = open(nombre_fichero, 'rt')
    print(f.read())
    f.close()
except:
    print(f'El fichero {nombre_fichero} no existe')
