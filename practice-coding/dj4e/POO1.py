          
def horadeldia(hora):
    
    if (hora >= 0 and hora < 6):
        print("Estamos de madrugada")
    elif (hora > 6 and hora < 12):
        print("Estamos en la mañana del día")
    elif (hora == 12):
        print("Estamos en medio día")
    elif (hora > 12 and hora < 18):
        print("Estamos en el la tarde del día")
    elif (hora > 18 and hora < 24):
        print("Estamos de noche")
    
    else:
        print("Error, dicha hora no existe")


horadeldia(int(input("Ingrese la hora: "))) 


