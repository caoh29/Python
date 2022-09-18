import math


numero = int(input("Digite un numero entero: "))
if numero > 0 :
    digits = int(math.log10(numero)) + 1
    print(str(digits))

elif numero == 0:
    digits = 1
    print(str(digits))
else :
    print("Debe ingresar un numero positivo")