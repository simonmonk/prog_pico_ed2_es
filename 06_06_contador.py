fichero_configuracion = 'configuracion.txt'
contador = 0

def lee_configuracion():
    global contador
    try:
        f = open(fichero_configuracion, 'r')
        contador = int(f.read())
        f.close()
    except:
       pass
       
def escribe_configuracion():
    f = open(fichero_configuracion, 'w')
    f.write(str(contador))
    f.close()
    

lee_configuracion()
print(contador)
contador += 1
escribe_configuracion()