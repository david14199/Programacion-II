from tkinter import *
from tkinter import messagebox
ap=Tk()

ap.geometry("600x600")

ap.configure(bg="aqua")
ap.title("FORMULARIO")
def funcion():
    
    #obtenemos nombre, apellido, edad, direccion, telefono

    
    n=nombre.get()
    a=apellido.get()
    e=edad.get()
    d=dirrecion.get()
    t=telefono.get()
    
    #obtener la selecion de la listbox
    
    seleccionados = ciudad.curselection()
    for index in seleccionados:
        elemento = ciudad.get(index)
      
   
       
    #obtenemos las opciones selecionadas de los radio button
    seleccion = variable.get()
    if seleccion == 1:
       
       seta="Hombre"
    elif seleccion == 2:
        seta="Mujer"
    elif seleccion == 3:
        seta="Helicoptero Apache de Combate"
    try:
        messagebox.showinfo(message=f"Nombre:{n}\nApellido:{a}\nEdad:{e}\nDirrecion:{d}\ntelefono:{t}\nCiudad:{elemento}\nSexo:{seta}", title="Sus datos son")
    except:
        messagebox.showinfo(message="a")
    nombre.delete(0, END)
    apellido.delete(0, END)   
    dirrecion.delete(0, END)     
    telefono.delete(0, END) 
    edad.delete(0, END) 
    variable.set(-1)
    # Obtener todos los índices de elementos seleccionados
   

    # Deseleccionar todos los elementos seleccionados
    for index in seleccionados:
        ciudad.selection_clear(index)
    
#label nombre, apellido, edad, direccion, telefono
titulo=Label(ap,text="FORMULARIO",bg="black", fg="white", font=("Arial", 16), width=20, height=2, anchor="center")
nom=Label(ap,text="Nombre",bg="black",fg="white")
apell=Label(ap,text="Apellido",bg="black",fg="white")
dir=Label(ap,text="Dirrecion",bg="black",fg="white")
tel=Label(ap,text="Telefono",bg="black",fg="white")
se=Label(ap,text="Genero",bg="black", fg="white", font=("Arial", 16), width=5, height=0, anchor="center")
ciu=Label(ap,text="Ciudad",bg="black", fg="white", font=("Arial", 16), width=5, height=0, anchor="center")
ed=Label(ap,text="Edad",bg="black",fg="white")

#posicionar label
titulo.place(x=200,y=120)
nom.place(x=200,y=200)
apell.place(x=200,y=230)
dir.place(x=200,y=260)
tel.place(x=200,y=290)
ed.place(x=200,y=320)
se.place(x=250,y=460)
ciu.place(x=250,y=350)

#Entry nombre, apellido, edad, direccion, telefono
nombre=Entry(ap)
apellido=Entry(ap)
dirrecion=Entry(ap)
telefono=Entry(ap)
edad=Entry(ap)

#posicionar entry
nombre.place(x=255,y=200)
apellido.place(x=255,y=230)
dirrecion.place(x=255,y=260)
telefono.place(x=255,y=290)
edad.place(x=255,y=320)

#crear listbox
ciudad=Listbox(ap, width=30,height=5, selectmode="single")

#posicionar listbox
ciudad.place(x=200,y=380)
#se insertan las opciones a la listbox
ciudades= ["Cartagena", "Sincelejo", "Turbaco", "Arjona"]
for ciudade in ciudades:
    ciudad.insert(END, ciudade)


#crear radio button
variable = IntVar()


opcion1 = Radiobutton(ap, text="Hombre", variable=variable, value=1, command="",bg="aqua",fg="black")
opcion2 = Radiobutton(ap, text="Mujer", variable=variable, value=2, command="",bg="aqua",fg="black")
opcion3 = Radiobutton(ap, text="Helicoptero apache de combate", variable=variable, value=3, command="",bg="aqua",fg="black")
#posicionar radio button
opcion1.place(x=200,y=490)
opcion2.place(x=200,y=510)
opcion3.place(x=200,y=530)

#creamos un botton
p=Button(ap,text="Mostrar",command=funcion)

#Posicionamos el boton
p.place(x=200,y=560)
mainloop()
