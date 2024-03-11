nombre_fichero = 'testXX.txt'
try:
    f = open(nombre_fichero, 'rt')
    print(f.read())
    f.close()
except:
    print('El fichero {} no existe'.format(nombre_fichero))