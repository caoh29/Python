import tkinter
import sys
import sqlite3



window = tkinter.Tk()

#Titulo de la ventana
titulo = 'Estudiantes'
window.title(titulo)

#Icono de la ventana
ruta = 'assets/books.png'
photo = tkinter.PhotoImage(file = ruta)
window.iconphoto(False, photo)

#Tamaño de la ventana
dimension = '550x550'
window.geometry(dimension)

#Encabezado
encabezado = tkinter.Label(window, text='Insertar un nuevo estudiante en la Base de Datos', font=('Arial', 12),)
encabezado.grid(row=0, column=1, padx=20, pady=20)

# Creando Text Boxes
db_title = tkinter.Entry(window, width=30)
db_title.grid(row=1, column=1)

id = tkinter.Entry(window, width=30)
id.grid(row=2, column=1)

primer_nombre = tkinter.Entry(window, width=30)
primer_nombre.grid(row=3, column=1)

segundo_nombre = tkinter.Entry(window, width=30)
segundo_nombre.grid(row=4, column=1)

primer_apellido = tkinter.Entry(window, width=30)
primer_apellido.grid(row=5, column=1)

segundo_apellido = tkinter.Entry(window, width=30)
segundo_apellido.grid(row=6, column=1)


#Creando Text Box Labels
db_title_label = tkinter.Label(window, text='Nombre Base de Datos')
db_title_label.grid(row=1, column=0, padx=10, pady=10)

id_label = tkinter.Label(window, text='Id')
id_label.grid(row=2, column=0, padx=10, pady=10)

primer_nombre_label = tkinter.Label(window, text='Primer Nombre')
primer_nombre_label.grid(row=3, column=0, padx=10, pady=10)

segundo_nombre_label = tkinter.Label(window, text='Segundo Nombre')
segundo_nombre_label.grid(row=4, column=0, padx=10, pady=10) 

primer_apellido_label = tkinter.Label(window, text='Primer Apellido')
primer_apellido_label.grid(row=5, column=0, padx=10, pady=10)  

segundo_apellido_label = tkinter.Label(window, text='Segundo Apellido')
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


    #Advierte al usuario si la transaccion fue exitosa
    advertencia = tkinter.Label(window, text='Se creó el estudiante', font=('Arial', 11),)
    advertencia.grid(row=8, column=1, padx=20, pady=20)
    
    # Limpiar las cajas de texto
    db_title.delete(0, tkinter.END)
    id.delete(0, tkinter.END)
    primer_nombre.delete(0, tkinter.END)
    segundo_nombre.delete(0, tkinter.END)
    primer_apellido.delete(0, tkinter.END)
    segundo_apellido.delete(0, tkinter.END)




#Creando Submit Button      
submit_btn = tkinter.Button(window, text='Añadir a la Base de Datos', command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


window.mainloop()
