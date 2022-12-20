import tkinter
import sqlite3


def main():
    
    update_window = tkinter.Tk()

    #Titulo de la ventana
    titulo_update = 'Editar Notas u Observaciones'
    update_window.title(titulo_update)

    #Tamaño de la ventana
    dimension = '350x200'
    update_window.geometry(dimension)

    #Encabezado
    encabezado = tkinter.Label(update_window, text='Editar Notas u Observaciones', font=('Arial', 12),)
    encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    pregunta = tkinter.Label(update_window, text='¿Qué acción desea realizar?', font=('Arial', 11),)
    pregunta.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    def editar_notas():
        notas_window = tkinter.Toplevel(update_window)

        notas_window.title('Editar Notas')
        notas_window.geometry('400x300')

        db_title = tkinter.Entry(notas_window, width=30)
        db_title.grid(row=1, column=1)

        nota = tkinter.Entry(notas_window, width=30)
        nota.grid(row=2, column=1)

        calificacion = tkinter.Entry(notas_window, width=30)
        calificacion.grid(row=3, column=1)

        id = tkinter.Entry(notas_window, width=30)
        id.grid(row=4, column=1)


        #Creando Text Box Labels
        db_title_label = tkinter.Label(notas_window, text='Nombre Base de Datos')
        db_title_label.grid(row=1, column=0, padx=10, pady=10)

        nota_label = tkinter.Label(notas_window, text='¿Qué Nota desea editar?')
        nota_label.grid(row=2, column=0, padx=10, pady=10)

        calificacion_label = tkinter.Label(notas_window, text='¿Qué valor desea asignar?')
        calificacion_label.grid(row=3, column=0, padx=10, pady=10)

        id_label = tkinter.Label(notas_window, text='Id')
        id_label.grid(row=4, column=0, padx=10, pady=10)



        #Creando Funcion submit() para la base de datos
        def submit():
            db_name = str(db_title.get())
            # Insertar los campos de texto en la base de datos
            connection = sqlite3.connect(f'{db_name}.db')

            cursor = connection.cursor()

            nota_value = nota.get()
            calificacion_value = calificacion.get()
            id_value = id.get()


            while True:
                try:
                    cursor.execute(f'UPDATE {db_name} SET nota{nota_value} = ? WHERE id =  ?', (calificacion_value, id_value))
                    break

                except:
                    error = tkinter.Label(notas_window, text='Ha ocurrido un error', font=('Arial', 11),)
                    error.grid(row=5, column=1, padx=20, pady=20)

                    error.after(3000, error.destroy)


            cursor.execute(f'SELECT SUM(nota) FROM {db_name}')
            x = cursor.fetchall()
            #cursor.execute(f'UPDATE {db_name} SET promedio = {} WHERE id = {id_value}')

            connection.commit()
            cursor.close()
            connection.close()

            
            # Limpiar las cajas de texto
            db_title.delete(0, tkinter.END)
            id.delete(0, tkinter.END)
            nota.delete(0, tkinter.END)
            calificacion.delete(0, tkinter.END)

            
            #Advierte al usuario si la transaccion fue exitosa
        
            advertencia = tkinter.Label(notas_window, text='Se editó el campo exitosamente', font=('Arial', 11),)
            advertencia.grid(row=5, column=1, padx=20, pady=20)

            x = advertencia.destroy
            advertencia.after(5000, x)

        #Creando Submit Button      
        submit_btn = tkinter.Button(notas_window, text='Añadir a la Base de Datos', command=submit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    
    def editar_observaciones():
        observaciones_window = tkinter.Toplevel(update_window)

        observaciones_window.title('Editar Observaciones')
        observaciones_window.geometry('400x300')

        db_title = tkinter.Entry(observaciones_window, width=30)
        db_title.grid(row=1, column=1)

        observacion = tkinter.Entry(observaciones_window, width=30)
        observacion.grid(row=2, column=1)

        id = tkinter.Entry(observaciones_window, width=30)
        id.grid(row=3, column=1)

        


        #Creando Text Box Labels
        db_title_label = tkinter.Label(observaciones_window, text='Nombre Base de Datos')
        db_title_label.grid(row=1, column=0, padx=10, pady=10)

        observacion_label = tkinter.Label(observaciones_window, text='Ingrese observación')
        observacion_label.grid(row=2, column=0, padx=10, pady=10)

        id_label = tkinter.Label(observaciones_window, text='Id')
        id_label.grid(row=3, column=0, padx=10, pady=10)


        #Creando Funcion submit() para la base de datos
        def submit():
            db_name = str(db_title.get())
            # Insertar los campos de texto en la base de datos
            connection = sqlite3.connect(f'{db_name}.db')

            cursor = connection.cursor()

            
            observacion_value = observacion.get()
            id_value = id.get()

            cursor.execute(f'UPDATE {db_name} SET observaciones = ? WHERE id =  ?', (observacion_value, id_value))
            

            connection.commit()
            cursor.close()
            connection.close()

            
            # Limpiar las cajas de texto
            db_title.delete(0, tkinter.END)
            id.delete(0, tkinter.END)
            observacion.delete(0, tkinter.END)

            
            #Advierte al usuario si la transaccion fue exitosa
        
            advertencia = tkinter.Label(observaciones_window, text='Se editó el campo exitosamente', font=('Arial', 11),)
            advertencia.grid(row=4, column=1, padx=20, pady=20)

            x = advertencia.destroy
            advertencia.after(5000, x)

        #Creando Submit Button      
        submit_btn = tkinter.Button(observaciones_window, text='Añadir a la Base de Datos', command=submit)
        submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    # Creando Text Boxes
    notas_btn = tkinter.Button(update_window, text='Editar Notas', command = editar_notas)
    notas_btn.grid(row=3, column=0, pady=10, padx=10)

    observaciones_btn = tkinter.Button(update_window, text='Editar Observaciones', command = editar_observaciones)
    observaciones_btn.grid(row=3, column=1, pady=10, padx=10)


    update_window.mainloop()

if __name__ == '__main__':
    main()