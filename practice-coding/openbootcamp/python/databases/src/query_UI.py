import tkinter
import sqlite3

def main():

    query_window = tkinter.Tk()

    #Titulo de la ventana
    titulo_query = 'Buscar estudiantes'
    query_window.title(titulo_query)

    #Tamaño de la ventana
    dimension = '550x550'
    query_window.geometry(dimension)

    #Encabezado
    encabezado = tkinter.Label(query_window, text='Buscar información en la Base de Datos', font=('Arial', 12),)
    encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Creando Text Boxes
    db_title = tkinter.Entry(query_window, width=30)
    db_title.grid(row=1, column=1)

    id = tkinter.Entry(query_window, width=30)
    id.grid(row=2, column=1)

    primer_nombre = tkinter.Entry(query_window, width=30)
    primer_nombre.grid(row=3, column=1)

    segundo_nombre = tkinter.Entry(query_window, width=30)
    segundo_nombre.grid(row=4, column=1)

    primer_apellido = tkinter.Entry(query_window, width=30)
    primer_apellido.grid(row=5, column=1)

    segundo_apellido = tkinter.Entry(query_window, width=30)
    segundo_apellido.grid(row=6, column=1)


    #Creando Text Box Labels
    db_title_label = tkinter.Label(query_window, text='Nombre Base de Datos')
    db_title_label.grid(row=1, column=0, padx=10, pady=10)

    id_label = tkinter.Label(query_window, text='Id')
    id_label.grid(row=2, column=0, padx=10, pady=10)

    primer_nombre_label = tkinter.Label(query_window, text='Primer Nombre')
    primer_nombre_label.grid(row=3, column=0, padx=10, pady=10)

    segundo_nombre_label = tkinter.Label(query_window, text='Segundo Nombre')
    segundo_nombre_label.grid(row=4, column=0, padx=10, pady=10) 

    primer_apellido_label = tkinter.Label(query_window, text='Primer Apellido')
    primer_apellido_label.grid(row=5, column=0, padx=10, pady=10)  

    segundo_apellido_label = tkinter.Label(query_window, text='Segundo Apellido')
    segundo_apellido_label.grid(row=6, column=0, padx=10, pady=10)

    #Creando Funcion submit() para la base de datos
    def search():
        db_name = str(db_title.get())
        # Insertar los campos de texto en la base de datos
        connection = sqlite3.connect(f'{db_name}.db')

        cursor = connection.cursor()

        id_value = id.get()
        primer_nombre_value = primer_nombre.get()
        segundo_nombre_value = segundo_nombre.get()
        primer_apellido_value = primer_apellido.get()
        segundo_apellido_value = segundo_apellido.get()

        #1. En caso de que todos los campos esten vacios
        if (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value == '') and (primer_apellido_value == '') and (segundo_apellido_value == ''):
            cursor.execute(f'SELECT * FROM {db_name}')
        
        #2. En caso de que id tenga algun valor
        elif (id_value != ''):
            cursor.execute(f'SELECT * FROM {db_name} WHERE id = :estudiante_matricula', {'estudiante_matricula': id_value})

        #3. En caso de que ingrese PRIMER NOMBRE y SEGUNDO NOMBRE y PRIMER APELLIDO y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value != '') and (primer_apellido_value != '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND segundo_nombre = :estudiante_segundoNombre AND primer_apellido = :estudiante_primerApellido AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        #4. En caso de que ingrese PRIMER NOMBRE y PRIMER APELLIDO y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value == '') and (primer_apellido_value != '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND primer_apellido = :estudiante_primerApellido AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )
        
        #5. En caso de que ingrese PRIMER NOMBRE y SEGUNDO NOMBRE y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value != '') and (primer_apellido_value == '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND segundo_nombre = :estudiante_segundoNombre AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        #6. En caso de que ingrese PRIMER NOMBRE y SEGUNDO NOMBRE y PRIMER APELLIDO
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value != '') and (primer_apellido_value != '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND segundo_nombre = :estudiante_segundoNombre AND primer_apellido = :estudiante_primerApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value
                }
                )

        #7. En caso de que ingrese SEGUNDO NOMBRE y PRIMER APELLIDO y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value != '') and (primer_apellido_value != '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE segundo_nombre = :estudiante_segundoNombre AND primer_apellido = :estudiante_primerApellido AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        #8. En caso de que ingrese PRIMER NOMBRE y SEGUNDO NOMBRE 
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value != '') and (primer_apellido_value == '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND segundo_nombre = :estudiante_segundoNombre', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_segundoNombre': segundo_nombre_value
                }
                )
        
        #9. En caso de que ingrese PRIMER NOMBRE y PRIMER APELLIDO 
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value == '') and (primer_apellido_value != '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND primer_apellido = :estudiante_primerApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value
                }
                )
        
        #10. En caso de que ingrese PRIMER NOMBRE y SEGUNDO APELLIDO 
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value == '') and (primer_apellido_value == '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_primerNombre': primer_nombre_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        

        #11. En caso de que ingrese SEGUNDO NOMBRE y PRIMER APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value != '') and (primer_apellido_value != '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE segundo_nombre = :estudiante_segundoNombre AND primer_apellido = :estudiante_primerApellido', 
                {
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_primerApellido': primer_apellido_value
                }
                )

        #12. En caso de que ingrese SEGUNDO NOMBRE y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value != '') and (primer_apellido_value == '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE segundo_nombre = :estudiante_segundoNombre AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_segundoNombre': segundo_nombre_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        #13. En caso de que ingrese PRIMER APELLIDO y SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value == '') and (primer_apellido_value != '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_apellido = :estudiante_primerApellido AND segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_primerApellido': primer_apellido_value,
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        #14. En caso de que ingrese PRIMER NOMBRE
        elif (id_value == '') and (primer_nombre_value != '') and (segundo_nombre_value == '') and (primer_apellido_value == '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_nombre = :estudiante_primerNombre', 
                {
                    'estudiante_primerNombre': primer_nombre_value
                }
                )
        
        #15. En caso de que ingrese SEGUNDO NOMBRE
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value != '') and (primer_apellido_value == '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE segundo_nombre = :estudiante_segundoNombre', 
                {
                    'estudiante_segundoNombre': segundo_nombre_value
                }
                )

        #16. En caso de que ingrese PRIMER APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value == '') and (primer_apellido_value != '') and (segundo_apellido_value == ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE primer_apellido = :estudiante_primerApellido', 
                {
                    'estudiante_primerApellido': primer_apellido_value
                }
                )

        #17. En caso de que ingrese SEGUNDO APELLIDO
        elif (id_value == '') and (primer_nombre_value == '') and (segundo_nombre_value == '') and (primer_apellido_value == '') and (segundo_apellido_value != ''):
            cursor.execute(
                f'SELECT * FROM {db_name} WHERE segundo_apellido = :estudiante_segundoApellido', 
                {
                    'estudiante_segundoApellido': segundo_apellido_value
                }
                )

        info =cursor.fetchall()

        print_info = ''
        for i in info:
            print_info += str(i) + '\n'

        #Muestra la info buscada
        busqueda_label = tkinter.Label(query_window, text= print_info, font=('Arial', 10),)
        busqueda_label.grid(row=8, column=0, columnspan=2, padx=20, pady=20)


        connection.commit()
        cursor.close()
        connection.close()

        
        # Limpiar las cajas de texto
        db_title.delete(0, tkinter.END)
        id.delete(0, tkinter.END)
        primer_nombre.delete(0, tkinter.END)
        segundo_nombre.delete(0, tkinter.END)
        primer_apellido.delete(0, tkinter.END)
        segundo_apellido.delete(0, tkinter.END)




    #Creando Search Button      
    search_btn = tkinter.Button(query_window, text='Buscar en la Base de Datos', command=search)
    search_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    query_window.mainloop()

if __name__ == '__main__':
    main()