from random import randint

def mi_choice(lista):
    ultimo_indice_lista = len(lista)-1
    elemento_aleatorio = randint(0, ultimo_indice_lista)
    return lista[elemento_aleatorio]

fruta = ['manzana', 'plátano', 'naranja', 'uva']

print('Hoy comeré', mi_choice(fruta))