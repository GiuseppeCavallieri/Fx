'''
Resumen Aplicacion: intenta simular una calculadora, recibe una expresion matematica que hasta el momento no puede contener
parentesis y mas de un signo matematico juntos, no esta pensado para recibir espacios o simbolos ajenos a los operadores
matematicos basicos, los cuales son: "+", "-", "x", "/".

Consta de dos partes, la interfaz que va a mostrar las operaciones que se podran realizar y recibir el resultado,
y el codigo el cual resolvera las ecuaciones ingresadas
'''

### BLOQUE DE DEFINICIONES ###

# IMPORTACIÓN DE FUNCIONES
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from operaciones import sumi, multiplicacion, division, resta
from desarrollo import conversion, operaciones

# DEFINICIÓN DE FUNCIONES

# Lee lo que hay en la caja de texto, lo desarrolla y modifica "resultado" con el resultado
def desarrollar_expresion(caja_texto_expresion):
    expresion = conversion(caja_texto_expresion.get())
    expresion_desarrollada = operaciones(expresion)
    resultado["text"] = expresion_desarrollada

# Limpia la caja de texto
def borrar_texto():
    caja_texto_expresion.delete(0, END)
    resultado["text"] = ""


### BLOQUE PRINCIPAL ###

# ENTRADA

# Variable de la expresion

# Creacion de la ventana y sus caracteristicas
ventana = tk.Tk()
ventana.title("Calculadora pro")
ventana.geometry("283x329")
ventana.resizable(0,0)
ventana.configure(bg="#323030")

# Abre la imagen
foto = Image.open("Fx-69.png")
# Reajusta la imagen
foto_resize = foto.resize((100,100))
# Convierte la imagen con ImageTk
foto_imagen = ImageTk.PhotoImage(foto_resize)
# Crea un label donde se ingresa la imagen
Label_imagen = Label(ventana, image= foto_imagen, bg="#323030")
# Se coloca el label
Label_imagen.place(x=84, y=-25)

# Caja de texto donde se ingresa la expresión
caja_texto_expresion = tk.Entry(ventana)
caja_texto_expresion.place(x=20, y= 86)

# Botones que ingresan el correspondiente simbolo en la caja de texto de la expresion
boton_0 = tk.Button(ventana, height=2, width=6, text="0", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "0"))
boton_0.place(x=80, y=269)

boton_1 = tk.Button(ventana, height=2, width=6, text="1", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "1"))
boton_1.place(x=20, y=220)

boton_2 = tk.Button(ventana, height=2, width=6, text="2", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "2"))
boton_2.place(x=80, y=220)
 
boton_3 = tk.Button(ventana, height=2, width=6, text="3", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "3"))
boton_3.place(x=145, y=220)

boton_4 = tk.Button(ventana, height=2, width=6, text="4", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "4"))
boton_4.place(x=20, y=171)

boton_5 = tk.Button(ventana, height=2, width=6, text="5", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "5"))
boton_5.place(x=80, y=171)

boton_6 = tk.Button(ventana, height=2, width=6, text="6", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "6"))
boton_6.place(x=145, y=171)

boton_7 = tk.Button(ventana, height=2, width=6, text="7", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "7"))
boton_7.place(x=20, y=122)

boton_8 = tk.Button(ventana, height=2, width=6, text="8", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "8"))
boton_8.place(x=80, y=122)

boton_9 = tk.Button(ventana, height=2, width=6, text="9", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "9"))
boton_9.place(x=145, y=122)

boton_suma = tk.Button(ventana, height=2, width=6, text="+", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "+"))
boton_suma.place(x=210, y=122)

boton_resta = tk.Button(ventana, height=2, width=6, text="-", fg= "White", bg= "#494848",
                    command= lambda: caja_texto_expresion.insert("end", "-"))
boton_resta.place(x=210, y=171)

boton_multiplicacion = tk.Button(ventana, height=2, width=6, text="*", fg= "White", bg= "#494848",
                                command= lambda: caja_texto_expresion.insert("end", "*"))
boton_multiplicacion.place(x=210, y=220)

boton_division = tk.Button(ventana, height=2, width=6, text="/", fg= "White", bg= "#494848",
                                command= lambda: caja_texto_expresion.insert("end", "/"))
boton_division.place(x=210, y=269)

boton_limpiar = tk.Button(ventana, height=2, width=6, text="limpiar", fg= "White", bg= "#494848",
                                command= borrar_texto)
boton_limpiar.place(x=20, y=269)

boton_igualdad = tk.Button(ventana, height=2, width=6, text="=", fg= "White", bg= "#494848",
                    command=lambda: desarrollar_expresion(caja_texto_expresion))
boton_igualdad.place(x=145, y=269)

# resultado es una caja de texto que muestra el desarrollo de la expresion
resultado = Label(text= "", fg="White", bg="#323030")
resultado.place(x=167, y= 85)

expresion_texto = Label(text= "Expresión:", fg= "White", bg="#323030")
expresion_texto.place(x=20, y= 60)

resultado_texto = Label(text= "Resultado:", fg= "White", bg="#323030")
resultado_texto.place(x=167, y= 60)


# mainloop debe estar al final del codigo, hace que la ventana funcione
ventana.mainloop()