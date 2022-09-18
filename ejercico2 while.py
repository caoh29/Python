import math


terreno = int(input("Defina el área en metros cuadrados del terreno: "))

while terreno <= 0:
    print("El numero del area del terreno no puede ser cero o negativo")
    terreno = int(input("Defina el area en metros cuadrados del terreno: "))

antenas_viejas = int(input("¿Cuantas antenas viejas hay instaladas?: "))

while antenas_viejas < 0:
    print("El numero de antenas no puede ser negativo")
    antenas_viejas = int(input("Cuantas antenas viejas hay instaladas?: "))

rango_cubierto = 2300


zona_con_cobertura = rango_cubierto * antenas_viejas

sin_cobertura = terreno - zona_con_cobertura

if sin_cobertura <= 0:
    print("El área sin cobertura es nula")

while True:

    tipo_antena = input("¿Que tipo de antena se utilizará? Seleccione entre a,b,c,d,e \n")
    if tipo_antena not in ("a","b","c","d","e"):
        print("Data Error")
        continue
    else:
        break


if tipo_antena == "a":
    nuevas_antenas = math.ceil(sin_cobertura / 45500)
    print(f"Antenas tipo a: {nuevas_antenas}")
elif tipo_antena == "b":
    nuevas_antenas = math.ceil(sin_cobertura / 16700)
    print(f"Antenas tipo b: {nuevas_antenas}")
elif tipo_antena == "c":
    nuevas_antenas = math.ceil(sin_cobertura / 27800)
    print(f"Antenas tipo c: {nuevas_antenas}")
elif tipo_antena == "d":
    nuevas_antenas = math.ceil(sin_cobertura / 7600)
    print(f"Antenas tipo d: {nuevas_antenas}")
elif tipo_antena == "e":
    nuevas_antenas = math.ceil(sin_cobertura / 13800)
    print(f"Antenas tipo e: {nuevas_antenas}")


