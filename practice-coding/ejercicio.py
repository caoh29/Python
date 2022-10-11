import math

terreno = int(input("Defina el área en metros cuadrados del terreno: "))
antenas_viejas = int(input("¿Cuantas antenas viejas hay instaladas?: "))
rango_cubierto = 2300


zona_con_cobertura = rango_cubierto * antenas_viejas

sin_cobertura = terreno - zona_con_cobertura

while antenas_viejas < 0:
    print("El numero de antenas no puede ser negativo")
    antenas_viejas = int(input("Cuantas antenas viejas hay instaladas?: "))

while terreno <= 0:
    print("El numero del area del terreno no puede ser cero o negativo")
    terreno = int(input("Defina el area en metros cuadrados del terreno: "))


if sin_cobertura <= 0:
    print("El área sin cobertura es nula")

tipo_antena = input("¿Que tipo de antena se utilizará? Seleccione entre a,b,c,d,e \n")

def one():
    return "Tipo a"
 
def two():
    return "Tipo b"
 
def three():
    return "Tipo c"
 
def four():
    return "Tipo d"
 
def five():
    return "Tipo e"

def tipo_antena(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,

    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Data Error")
    
    # Execute the function
    print (func())

