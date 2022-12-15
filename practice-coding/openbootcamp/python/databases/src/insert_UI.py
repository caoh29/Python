import tkinter
import sqlite3


def main():
    
    insert_window = tkinter.Tk()

    #Titulo de la ventana
    titulo_insert = 'Insertar estudiantes'
    insert_window.title(titulo_insert)

    #Tamaño de la ventana
    dimension = '500x450'
    insert_window.geometry(dimension)

    #Encabezado
    encabezado = tkinter.Label(insert_window, text='Insertar un nuevo estudiante en la Base de Datos', font=('Arial', 12),)
    encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Creando Text Boxes
    db_title = tkinter.Entry(insert_window, width=30)
    db_title.grid(row=1, column=1)

    id = tkinter.Entry(insert_window, width=30)
    id.grid(row=2, column=1)

    primer_nombre = tkinter.Entry(insert_window, width=30)
    primer_nombre.grid(row=3, column=1)

    segundo_nombre = tkinter.Entry(insert_window, width=30)
    segundo_nombre.grid(row=4, column=1)

    primer_apellido = tkinter.Entry(insert_window, width=30)
    primer_apellido.grid(row=5, column=1)

    segundo_apellido = tkinter.Entry(insert_window, width=30)
    segundo_apellido.grid(row=6, column=1)


    #Creando Text Box Labels
    db_title_label = tkinter.Label(insert_window, text='Nombre Base de Datos')
    db_title_label.grid(row=1, column=0, padx=10, pady=10)

    id_label = tkinter.Label(insert_window, text='Id')
    id_label.grid(row=2, column=0, padx=10, pady=10)

    primer_nombre_label = tkinter.Label(insert_window, text='Primer Nombre')
    primer_nombre_label.grid(row=3, column=0, padx=10, pady=10)

    segundo_nombre_label = tkinter.Label(insert_window, text='Segundo Nombre (Si NO tiene, ingrese "*")')
    segundo_nombre_label.grid(row=4, column=0, padx=10, pady=10) 

    primer_apellido_label = tkinter.Label(insert_window, text='Primer Apellido')
    primer_apellido_label.grid(row=5, column=0, padx=10, pady=10)  

    segundo_apellido_label = tkinter.Label(insert_window, text='Segundo Apellido (Si NO tiene, ingrese "*")')
    segundo_apellido_label.grid(row=6, column=0, padx=10, pady=10)


    #Creando Funcion submit() para la base de datos
    def submit():
        db_name = str(db_title.get())
        # Insertar los campos de texto en la base de datos
        connection = sqlite3.connect(f'{db_name}.db')

        cursor = connection.cursor()

        cursor.execute(
            f'INSERT INTO {db_name} (id, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido) VALUES (:estudiante_matricula, :estudiante_primerNombre, :estudiante_segundoNombre, :estudiante_primerApellido, :estudiante_segundoApellido)', 
            {
                    'estudiante_matricula': id.get(),
                    'estudiante_primerNombre': primer_nombre.get(),
                    'estudiante_segundoNombre': segundo_nombre.get(),
                    'estudiante_primerApellido': primer_apellido.get(),
                    'estudiante_segundoApellido': segundo_apellido.get()
            }
            )

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

        
        #Advierte al usuario si la transaccion fue exitosa
    
        advertencia = tkinter.Label(insert_window, text='Se creó el estudiante', font=('Arial', 11),)
        advertencia.grid(row=8, column=1, padx=20, pady=20)

        x = advertencia.destroy
        advertencia.after(5000, x)
        





    #Creando Submit Button      
    submit_btn = tkinter.Button(insert_window, text='Añadir a la Base de Datos', command=submit)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    insert_window.mainloop()

if __name__ == '__main__':
    main()
