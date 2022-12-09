

a=[]

while True:

    x = int(input("Digite un numero positivo: "))
    if x < 0:
        print("Data Error")
        continue
    break


n=1
while n <= x :
    if  x % n == 0:
        a.append(n)
        a.sort()
    n=n+1
          
print(a)
