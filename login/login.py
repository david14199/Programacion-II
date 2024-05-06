from tkinter import * 
from tkinter import messagebox
import util.generic as utl
def inicio():
    user.delete(0, END)
    cla.delete(0, END)
    messagebox.showinfo("VENTANA", message="Estamos trabajando...")


main=Tk()
main.title("SPLAVIA")
main.geometry("800x150")
main.resizable(False,False)
#
icono = utl.leer_imagen("imagenes/images.jpg",(20,20))

main.iconphoto(True,icono)
#

logo = utl.leer_imagen("imagenes/logo.png", (600, 115))
frame_logo = Frame(main, bd=0, width=300,relief=SOLID, padx=10, pady=10, bg="#F4F5F7")
frame_logo.pack(side=LEFT, expand=YES, fill=BOTH)
#
#
frame2=Frame(main)
#
titulo=Label(frame2,text="Inicio Sesion",font=("Arial",16))
titulo.pack()

nombre=Label(frame2,text="USUARIO")
nombre.pack()
user=Entry(frame2)
user.pack()
clave=Label(frame2,text="CLAVE")
clave.pack()
cla=Entry(frame2)
cla.pack()

#
imagen1=Label(frame_logo,image=logo)
imagen1.pack()
#

frame2.pack(side="right")
frame_logo.pack(side="left")

hola=Button(frame2,text="inicio de sesion",command=inicio)
hola.pack()
mainloop()
