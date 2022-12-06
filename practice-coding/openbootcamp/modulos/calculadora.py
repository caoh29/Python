def sumar(*args):
    suma = 0
    for i in args:
        suma+=i
    return suma

def restar(*args):
    resta = args[0]
    for i in args[1:]:
        resta-=i
    return resta

def multiplicar(*args):
    multiplicacion = 1
    for i in args:
        multiplicacion*=i
    return multiplicacion

def dividir(*args):
    division = args[0]
    for i in args[1:]:
        division/=i
    return division