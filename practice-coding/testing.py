numbers = []
n = int(input("Ingrese la cantidad de iteraciones: "))
for i in range(n):
    j = int(input("Ingrese un valor: "))
    i=i+1
    numbers.append(j)
    
print(numbers)

for y in numbers:
        if(y % 5 == 0):
            print(y)   