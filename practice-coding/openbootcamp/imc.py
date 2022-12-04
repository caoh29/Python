peso = int(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en Metros: "))

imc = round(peso / (estatura**2), 2)

print(f"Tu indice de masa corporal es: {imc}")