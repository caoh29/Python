import tkinter
import sqlite3


def main():
    
    delete_window = tkinter.Tk()

    #Titulo de la ventana
    titulo_delete = 'Eliminar estudiantes'
    delete_window.title(titulo_delete)

    #Tamaño de la ventana
    dimension = '500x450'
    delete_window.geometry(dimension)

    #Encabezado
    encabezado = tkinter.Label(delete_window, text='Eliminar un estudiante en la Base de Datos', font=('Arial', 12),)
    encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    # Creando Text Boxes
    db_title = tkinter.Entry(delete_window, width=30)
    db_title.grid(row=1, column=1)

    id = tkinter.Entry(delete_window, width=30)
    id.grid(row=2, column=1)



    #Creando Text Box Labels
    db_title_label = tkinter.Label(delete_window, text='Nombre Base de Datos')
    db_title_label.grid(row=1, column=0, padx=10, pady=10)

    id_label = tkinter.Label(delete_window, text='Id')
    id_label.grid(row=2, column=0, padx=10, pady=10)



    #Creando Funcion submit() para la base de datos
    def submit():
        db_name = str(db_title.get())
        # Eliminar los campos de texto en la base de datos
        connection = sqlite3.connect(f'{db_name}.db')

        cursor = connection.cursor()

        id_value = id.get()

        cursor.execute(f'DELETE FROM {db_name} WHERE id = :estudiante_matricula', {'estudiante_matricula': id_value})

        connection.commit()
        cursor.close()
        connection.close()

        
        # Limpiar las cajas de texto
        db_title.delete(0, tkinter.END)
        id.delete(0, tkinter.END)
       

        
        #Advierte al usuario si la transaccion fue exitosa
    
        advertencia = tkinter.Label(delete_window, text='Se eliminó el estudiante', font=('Arial', 11),)
        advertencia.grid(row=8, column=1, padx=20, pady=20)

        x = advertencia.destroy
        advertencia.after(5000, x)
        





    #Creando Submit Button      
    submit_btn = tkinter.Button(delete_window, text='Eliminar de la Base de Datos', command=submit)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    delete_window.mainloop()

if __name__ == '__main__':
    main()
