from functools import reduce

def main():
    lista = []

    while True:
        try:
            item = input('Ingrese un elemento dentro de la lista("^" para salir): ')

            if item == '^':
                break

            num = int(item)

        except:
            print('\nHa ocurrido un error, debe ingresar un numero entero\n')
            continue
        
        lista.append(num)
    
    impares = sorted(list(filter(lambda x : x % 2 != 0, lista)))

    suma = reduce(lambda x, y : x + y, impares)

    print(f'\nLa suma de los numero impares dentro de la lista es: {suma}\n')

if __name__ == '__main__':
    main()
    



      
