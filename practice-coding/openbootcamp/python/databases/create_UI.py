import tkinter
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
dimension = '450x550'
window.geometry(dimension)

#Encabezado
encabezado = tkinter.Label(window, text='Crear una nueva base de datos', font=('Arial', 12),)
encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Creando Text Boxes
db_title = tkinter.Entry(window, width=30)
db_title.grid(row=1, column=1)

cantdiad_notas = tkinter.Entry(window, width=30)
cantdiad_notas.grid(row=2, column=1)


#Creando Text Box Labels
db_title_label = tkinter.Label(window, text='Nombre de la nueva base de datos')
db_title_label.grid(row=1, column=0, padx=10, pady=10)

cantidad_notas_label = tkinter.Label(window, text='Cuantas notas sacará durante el periodo')
cantidad_notas_label.grid(row=2, column=0, padx=10, pady=10)  


#Creando Funcion submit() para la base de datos
def submit():
    # Crear base de datos
    db_name = str(db_title.get())
    notas_num = int(cantdiad_notas.get())

    connection = sqlite3.connect(f'{db_name}.db')

    cursor = connection.cursor()

    cursor.execute(
        f''' 
        CREATE TABLE IF NOT EXISTS {db_name} (
            id TEXT PRIMARY KEY,
            primer_nombre TEXT NOT NULL,
            segundo_nombre TEXT,
            primer_apellido TEXT NOT NULL,
            segundo_apellido TEXT
        )
        '''
    )

    notas =[]
    for i in range(notas_num):
        notas.append(f'nota{i+1} REAL')

    for j in range(len(notas)):
        cursor.execute(
            f'''
            ALTER TABLE {db_name} ADD {notas[j]}
            '''
        )

    cursor.execute(f'ALTER TABLE {db_name} ADD promedio REAL')
    cursor.execute(f'ALTER TABLE {db_name} ADD observaciones TEXT')


    connection.commit()
    cursor.close()
    connection.close()

    #Advierte al usuario si la transaccion fue exitosa
    advertencia = tkinter.Label(window, text='Se creó la base de datos', font=('Arial', 11),)
    advertencia.grid(row=6, column=1, padx=20, pady=20)
    
    # Limpiar las cajas de texto
    db_title.delete(0, tkinter.END)
    cantdiad_notas.delete(0, tkinter.END)




#Creando Submit Button      
submit_btn = tkinter.Button(window, text='Crear Base de Datos', command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


window.mainloop()
