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
dimension = '500x500'
window.geometry(dimension)

#Encabezado
encabezado = tkinter.Label(window, text='Insertar un nuevo estudiante en la tabla Estudiantes', font=('Arial', 12),)
encabezado.grid(row=0, column=1, padx=20, pady=20)

# Creando Text Boxes
id = tkinter.Entry(window, width=30)
id.grid(row=1, column=1)

nombre = tkinter.Entry(window, width=30)
nombre.grid(row=2, column=1)

apellido = tkinter.Entry(window, width=30)
apellido.grid(row=3, column=1)

promedio = tkinter.Entry(window, width=30)
promedio.grid(row=4, column=1)


#Creando Text Box Labels
id_label = tkinter.Label(window, text='Id')
id_label.grid(row=1, column=0, padx=10, pady=10)

nombre_label = tkinter.Label(window, text='Nombre')
nombre_label.grid(row=2, column=0, padx=10, pady=10)  

apellido_label = tkinter.Label(window, text='Apellido')
apellido_label.grid(row=3, column=0, padx=10, pady=10)  

promedio_label = tkinter.Label(window, text='Promedio')
promedio_label.grid(row=4, column=0, padx=10, pady=10)

#Creando Funcion submit() para la base de datos
def submit():
    # Insertar los campos de texto en la base de datos
    connection = sqlite3.connect('universidad.db')

    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO Estudiantes VALUES (:estudiante.matricula, :estudiante.nombre, :estudiante.apellido, :estudiante.promedio)', 
        {
                'estudiante_matricula': id.get(),
                'estudiante_nombre': nombre.get(),
                'estudiante_apellido': apellido.get(),
                'estudiante_promedio': promedio.get()
        }
        )

    connection.commit()
    cursor.close()
    connection.close()

    
    # Limpiar las cajas de texto
    id.delete(0, tkinter.END)
    nombre.delete(0, tkinter.END)
    apellido.delete(0, tkinter.END)
    promedio.delete(0, tkinter.END)




#Creando Submit Button      
submit_btn = tkinter.Button(window, text='Añadir a la Base de Datos', command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


window.mainloop()
