
a = [1,1,5,7,8,5,3,6,8,5,4,3,5,7,8,9,4]
resultado = []

x = int(input("Digite un numero del 1 al 9: "))

for n in a:
    if n < x:
        resultado.append(n)
        resultado.sort()
        

print(resultado)
