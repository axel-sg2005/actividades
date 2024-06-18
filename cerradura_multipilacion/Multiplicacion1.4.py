print("cerradura: La multiplicacion de dos numero reales")
print("a * b Pertenece R")
print() # Linea en blanco que separa una seccion

print("El siguiente programa realiza la propiedd de cerradura.")
print() #linea en blanco para separar la introduccion de la siguiente seccion(separacion)

num1 = float(input("ingrse el primer numero: ")) #El float hace que se puedan ingresar los numeros decimales
num2 = float(input("ingrese el segundo numero: "))

Mult = num1 * num2
#verifica si la Mult es un numero entero
if Mult.is_integer():
    resultado = "entero"
else:
    resultado = "racional"

#Muestra el resultado
print()#Linea para dejar un espacio(opcionbal)
print("El resultado de la Mult es: ", Mult)
print("El resulatdo es un numero", resultado)
