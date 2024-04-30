from tkinter import *
from tkinter import messagebox
ap=Tk()

ap.geometry("800x600")
#img=open(file="image.jpg")

#im=Label(ap,image=img)
#im.pack()
titulo=Label(ap,text="Trabaja con Nosotros",font=("Arial",24),background="white")
titulo.place(x=200,y=0)

subtitulo=Label(ap,text="¡Empieza a construir tu futuro con nosotros, ayúdanos a obtener más clientes satisfechos!",font=("docs-Roboto",11),background="white")
subtitulo.place(x=200,y=50)


corr=Label(ap,text="Correo electrónico",font=("Arial",11),background="white",border=3)
corr.place(x=200,y=150)

correo=Entry(ap,width=50)
correo.place(x=200,y=180)
carho=Label(ap,text="¿Cargo al que Aplica?",font=("Arial",11),background="white",border=3)
carho.place(x=200,y=200)
variable = IntVar()
opcion1 = Radiobutton(ap, text="Ayudante de Obra Civil", variable=variable, value=1, command="")
opcion2 = Radiobutton(ap, text="Enchapador", variable=variable, value=2, command="")
opcion3 = Radiobutton(ap, text="Oficial Obras Civiles", variable=variable, value=3, command="")
opcion4= Radiobutton(ap, text="Maestro de obra", variable=variable, value=4, command="")
opcion5 = Radiobutton(ap, text="Plomero", variable=variable, value=5, command="")
opcion6 = Radiobutton(ap, text="Ayudante eléctrico", variable=variable, value=6, command="")

opcion1.place(x=200,y=225)
opcion2.place(x=200,y=250)
opcion3.place(x=200,y=275)
opcion4.place(x=200,y=300)
opcion5.place(x=200,y=325)
opcion6.place(x=200,y=350)






















mainloop()
