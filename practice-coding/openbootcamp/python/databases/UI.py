import tkinter
import sys

def main():
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
    encabezado = tkinter.Label(window, text='Base de Datos Estudiantes', font=('Arial',14))
    encabezado.pack(padx=20, pady=20)

    # Creando Text Boxes
    id = tkinter.Entry(window, width=30)
    id.grid(row=0, column=1, padx=20)

    nombre = tkinter.Entry(window, width=30)
    nombre.grid(row=1, column=1, padx=20)

    apellido = tkinter.Entry(window, width=30)
    apellido.grid(row=2, column=1, padx=20)

    promedio = tkinter.Entry(window, width=30)
    promedio.grid(row=3, column=1, padx=20)


    #Creando Text Bpx Labels
    id_label = tkinter.Label(window, text='Id')
    id_label.grid(row=0, column=0)

    nombre_label = tkinter.Label(window, text='Nombre')
    nombre_label.grid(row=1, column=0)  

    apellido_label = tkinter.Label(window, text='Apellido')
    apellido_label.grid(row=2, column=0)  

    promedio_label = tkinter.Label(window, text='Promedio')
    promedio_label.grid(row=3, column=0)

    #Creando Funcion submit() para la base de datos
    def submit():
        # Limpiar las cajas de texto
        id.delete(0, tkinter.END)
        nombre.delete(0, tkinter.END)
        apellido.delete(0, tkinter.END)
        promedio.delete(0, tkinter.END)


    #Creando Submit Button      
    submit_btn = tkinter.Button(window, text='Añadir a la Base de Datos', command=submit)
    submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


    window.mainloop()

if __name__ == '__main__':
    main()