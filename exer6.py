c = []

string = input("Ingrese una palabra: ")
x = len(string)

for c in string: 
    if c[0] == c[1]:
        print(c)
    break


