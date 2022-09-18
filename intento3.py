def adding(x):
    global var
    var = 7
    return x + var

var = 1
print(adding(4))    # salida: 11
print(var)    # NameError