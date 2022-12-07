import sys

try:
    choice = int(input('Para leer un archivo, marque 1, para escribir un archivo, marque 2: '))
except:
    sys.exit()

if choice == 2:

    title = str(input('Ingrese el nombre del documento de texto: '))

    fhandler = open(f'{title}.txt', 'w')

    text=[]

    while True:
        line = str(input('Ingrese una linea ("^" para finalizar):'))

        if line == '^':
            break

        text.append(line+'\n')


    fhandler.writelines(text)
    fhandler.close()

else:

    while True:
        document = str(input('Ingrese el nombre del archivo("^" para finalizar): '))

        if document == '^':
            sys.exit()

        try:
            fhandler = open(f'{document}.txt', 'r')
            break
        except:
            print('El archivo no existe')

    for linea in fhandler:
        print(linea)
    fhandler.close()