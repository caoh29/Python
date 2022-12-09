import tkinter

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text='Hola!', background='cyan', foreground='gray')

label_saludo.pack(ipadx=50, ipady=50, expand=True)

label_saludo = tkinter.Label(window, text='Bye!', background='red', foreground='white')

label_saludo.pack(ipadx=40, ipady=60, fill='both')

window.mainloop()