# IMPORTACION DE FUNCIONES
from operaciones import multiplicacion, sumi, resta, division



# Recibe una expresión y la convierte a una lista trabajable, por el momento no reconoce parentesis
# ni operadores matematicos juntos
def conversion(expresion):
    NUMS = "1234567890"
    lista_trabajable = []
    numero = ""
    i = 0
    # Recorre la ecuacion
    while i < len(expresion):
        # Si ve un numero lo agrega a la variable numero
        if expresion[i] in NUMS:
            numero += expresion[i]
            # Si la posición es la última, agrega el número a la lista directamente
            if i == len(expresion) - 1:
                lista_trabajable.append(int(numero))

        # Si ve algo diferente de un numero,
        else:
            # Agrega el numero a la lista trabajable
            lista_trabajable.append(int(numero))
            # Agrega la operación que hay entremedio de los números
            lista_trabajable.append(expresion[i])
            # Reinicia la variable numero
            numero = ""
        i += 1
    
    return lista_trabajable

# realiza las operaciones correspondientes en la lista trabajable
def operaciones(lista_trabajable):
    i = 0
    # recorre la lista trabajable
    while i < len(lista_trabajable):
        # si encuentra el signo *, realiza una multiplicación con los numeros que lo acompañan
        if lista_trabajable[i] == "*":
            multiplicacion(lista_trabajable, i)
            # se debe restar uno al indice, ya que despues el ciclo iterador suma uno, haciendo que de esta forma el indice
            # queda en la misma posición, esto funciona ya que las funciones de operación borran los últimos dos elementos
            # de la expresión, haciendo que el elemento que sigue a la operación que se realiza quede en la posición del indice
            i -= 1
        # si encuentra el signo /, realiza una división con los numeros que lo acompañan
        elif lista_trabajable[i] == "/":
            division(lista_trabajable, i)
            i -= 1
        i += 1
        
    i = 0
    while i < len(lista_trabajable):
        # si encuentra el signo +, realiza una suma con los numeros que lo acompañan
        if lista_trabajable[i] == "+":
            sumi(lista_trabajable, i)
            i -= 1
        # si encuentra el signo -, realiza resta con los numeros que lo acompañan
        elif lista_trabajable[i] == "-":
            resta(lista_trabajable, i)
            i -= 1
        i += 1
    
    return lista_trabajable




