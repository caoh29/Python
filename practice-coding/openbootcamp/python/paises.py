def main():
    
    palabra = str(input('¿Qué tipo de objetos va a ingresar (paises, nombres, clientes, vehiculos, platillos, etc): '))

    print()

    lista = []

    objeto = (input(f'Ingrese l@s {palabra} se parados por comas ",": ') + '\n')

    word = ''

    count = 0

    for i in objeto:

        count += 1

        if i == ' ':
            continue

        if i == ',' or count == len(objeto):
            lista.append(word)
            word = ''
            continue

        word += i

    lista_final = [*set(lista)]

    print()

    print(f'L@s {palabra} ingresad@s son: {sorted(lista_final)}')

if __name__ == "__main__":
    main()