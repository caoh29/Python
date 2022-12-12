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


    window.mainloop()

if __name__ == '__main__':
    main()