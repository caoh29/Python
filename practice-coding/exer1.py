
name = str.upper(input("Ingrese su nombre: "))
age = int(input("Ingrese su edad: "))
copies = int(input("Cuantas copias desea ver?: "))


x = 100 - age 

#Donde X es el numero de años restantes para alcanzar 100

birth_year = 2021 + x

#Donde BIRTH_YEAR es el año en el cual la persona cumplira 100 años

i = 0

for i in range (copies):

    print(f"FELICIDADES {name}!,\n En el año {birth_year} cumpliras 100 años")
    i= i+1
