import sqlite3
import sys
import metodos
from estudiantes import Estudiante


def main():


    while True:
        try: 
            global operacion 
            operacion = int(input())
            break
        except:
            print('Ingrese un número entre (1,2,3,4)')



    if operacion == 1:
        metodos.create_students_table()
        decision = input('Desea realizar otra operación? Escriba (Si o No): ')
        decision = decision.lower()
        if decision == 'si':
            main()
        else:
            sys.exit()



    elif operacion == 2:
        frase = str(input('Ingrese los siguientes parámetros separados por comas "(id, nombre, apellido, promedio)": ') + '\n')

        lista=[]
        word = ''
        count = 0

        for i in frase:

            count += 1

            if i == ' ':
                continue

            if i == ',' or count == (len(frase)):
                lista.append(word)
                word = ''
                continue

            word += i

        stringToFloat = float(lista[3])
        del lista[3]
        lista.append(stringToFloat)
        estudiante = Estudiante(lista[0], lista[1], lista[2], lista[3])
        metodos.insert_estudiante(estudiante)

        decision = input('Desea realizar otra operación? Escriba (Si o No): ')
        decision = decision.lower()
        if decision == 'si':
            main()
        else:
            sys.exit()



    elif operacion == 3:
        
        id = str(input('Ingrese el id del estudiante a eliminar: '))
        metodos.delete_estudiante(id)
        print('el estudiante fue eliminado exitosamente de la base de datos')
           
        decision = input('Desea realizar otra operación? Escriba (Si o No): ')
        decision = decision.lower()
        if decision == 'si':
            main()
        else:
            sys.exit()



    elif operacion == 4:
        frase = str(input('Ingrese los siguientes parámetros separados por comas "(id, promedio)": ') + '\n')

        lista=[]
        word = ''
        count = 0

        for i in frase:

            count += 1

            if i == ' ':
                continue

            if i == ',' or count == (len(frase)):
                lista.append(word)
                word = ''
                continue

            word += i

        stringToFloat = float(lista[1])
        del lista[1]
        lista.append(stringToFloat)

        metodos.update_promedio(lista[0], lista[1])

        decision = input('Desea realizar otra operación? Escriba (Si o No): ')
        decision = decision.lower()
        if decision == 'si':
            main()
        else:
            sys.exit()



    else:
        print('''
        ¿Que tipo de consulta desea realizar?\n
        Marque (1) para consultar por id
        Marque (2) para consultar por nombre
        Marque (3) para consultar por apellido
        Marque (4) para consultar todos los estudiantes dentro de la base de datos''')

        while True:
            try:
                global tipo_consulta
                tipo_consulta = int(input())
                break
            except:
                print('Ingrese un número entre (1,2,3,4)')

        if tipo_consulta == 1:
            id = str(input('Ingrese el id del estudiante a consultar: '))
            datos = metodos.select_student_matricula(id)
            print(datos)

        elif tipo_consulta == 2:
            nombre = str(input('Ingrese el nombre del estudiante a consultar: '))
            datos = metodos.select_student_nombre(nombre)
            print(datos)

        elif tipo_consulta == 3:
            apellido = str(input('Ingrese el apellido del estudiante a eliminar: '))
            datos = metodos.select_student_apellido(apellido)
            print(datos)

        else:
            datos = metodos.select_all()
            print(datos)

        decision = input('Desea realizar otra operación? Escriba (Si o No): ')
        decision = decision.lower()
        if decision == 'si':
            main()
        else:
            sys.exit()

      

        

if __name__ == '__main__':
    main()
    