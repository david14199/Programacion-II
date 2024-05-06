from tkinter import * 
import util.generic as utl

main=Tk()

main.geometry("800x800")
#
logo = utl.leer_imagen("image.jpg", (225, 225))
frame_logo = Frame(main, bd=0, width=300,relief=SOLID, padx=10, pady=10, bg="#F4F5F7")
frame_logo.pack(side=LEFT, expand=YES, fill=BOTH)
#
frame1=Frame(main)
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
imagen1=Label(frame1,image=logo)

#
frame1.pack(side="left")
frame2.pack(side="right")


mainloop()