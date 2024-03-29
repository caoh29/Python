import tkinter
import insert_UI
import query_UI
import create_UI
import delete_UI
import update_UI

window = tkinter.Tk()

#Titulo de la ventana
titulo = 'Estudiantes'
window.title(titulo)

#Icono de la ventana
ruta = 'src/assets/books.png'
photo = tkinter.PhotoImage(file = ruta)
window.iconphoto(False, photo)

#Tamaño de la ventana
dimension = '300x350'
window.geometry(dimension)


#Encabezado
encabezado = tkinter.Label(window, text='Menu', font=('Arial', 12))
encabezado.grid(row=0, column=0, columnspan=2, padx=20, pady=20)



# Creando Text Boxes
create_btn = tkinter.Button(window, text='Crear una base de datos', command=create_UI.main)
create_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10)


insert_btn = tkinter.Button(window, text='Insertar un estudiante en una base de datos', command=insert_UI.main)
insert_btn.grid(row=2, column=0, columnspan=2, pady=10, padx=10)


query_btn = tkinter.Button(window, text='Buscar en una base de datos', command=query_UI.main)
query_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10)


update_btn = tkinter.Button(window, text='Editar notas u observaciones en una base de datos', command=update_UI.main)
update_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10)


delete_btn = tkinter.Button(window, text='Eliminar en una base de datos', command=delete_UI.main)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)



window.mainloop()