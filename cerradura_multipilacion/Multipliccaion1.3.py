# Solicita al usuario que ingrese dos numeros
num1 = float(input("ingrse el primer numero: ")) #El float hace que se puedan ingresar los numeros decimales
num2 = float(input("ingrese el segundo numero: "))

# Compara
if num1 > num2:
    print("El primer numero es mayor ({}) es mayor que el segundo numero ({})".
    format(num1, num2))
elif num1 < num2:
    print("El segundo numero ({}) es mayor que el primer numero ({})".
    format(num2, num1))
else:
    print("Ambos numeros son iguales")
