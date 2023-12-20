# Operaciones calculadora
'''
cada funcion recibe la lista y la posición del signo, lo que hace es operar los numeros de al lado con el signo
correspondiente, colocando el resultado en la posición izquierda del signo, a continuación elimina los dos elementos
siguientes que serían el signo y el número de la derecha
'''

def sumi(lista_trabajable, i):
    lista_trabajable[i-1] = lista_trabajable[i-1] + lista_trabajable[i+1]
    lista_trabajable.pop(i)
    lista_trabajable.pop(i)

def resta(lista_trabajable, i):
    lista_trabajable[i-1] = lista_trabajable[i-1] - lista_trabajable[i+1]
    lista_trabajable.pop(i)
    lista_trabajable.pop(i)


def multiplicacion(lista_trabajable, i):
    lista_trabajable[i-1] = lista_trabajable[i-1] * lista_trabajable[i+1]
    lista_trabajable.pop(i)
    lista_trabajable.pop(i)


def division(lista_trabajable, i):
    lista_trabajable[i-1] = lista_trabajable[i-1] / lista_trabajable[i+1]
    lista_trabajable.pop(i)
    lista_trabajable.pop(i)
