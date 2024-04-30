from tkinter import *
from tkinter import messagebox
ap=Tk()

ap.geometry("600x600")

ap.configure(bg="black")
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
        messagebox.showinfo("DATOS REGISTRADOS",message=f"Nombre:{n}\nApellido:{a}\nEdad:{e}\nDirrecion:{d}\ntelefono:{t}\nCiudad:{elemento}\nSexo:{seta}", title="Sus datos son")
    except:
        messagebox.showinfo(message="ERROR NO SE PUDO MOSTRAR SUS DATOS")
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
titulo.grid(column=0,row=1,padx=200,pady=50, ipadx=0,sticky=W)

nom.grid(column=0,row=2,padx=200, pady=0,sticky=W,ipadx=3)

apell.grid(column=0,row=3,padx=200, pady=5,sticky=W,ipadx=3)

dir.grid(column=0,row=4,padx=200, pady=0,sticky=W,ipadx=1)

tel.grid(column=0,row=5,padx=200, pady=5,sticky=W,ipadx=2)

ed.grid(column=0,row=6,padx=200, pady=0,sticky=W,ipadx=12)

ciu.grid(column=0,row=7,padx=255, pady=0,sticky=W,ipadx=0)

se.grid(column=0,row=9,padx=255, pady=5,sticky=W,ipadx=0)

#Entry nombre, apellido, edad, direccion, telefono
nombre=Entry(ap)
apellido=Entry(ap)
dirrecion=Entry(ap)
telefono=Entry(ap)
edad=Entry(ap)
#posicionar entry
nombre.grid(column=0,row=2,padx=256,sticky=W,)
apellido.grid(column=0,row=3,padx=255, pady=0,sticky=W)
dirrecion.grid(column=0,row=4,padx=255, pady=0,sticky=W)
telefono.grid(column=0,row=5,padx=255, pady=0,sticky=W)
edad.grid(column=0,row=6,padx=255, pady=0,sticky=W,ipadx=0)

#crear listbox

ciudad=Listbox(ap, width=30,height=5, selectmode="single")

#posicionar listbox
ciudad.grid(column=0,row=8,padx=200, pady=0,sticky=W,ipadx=0)
#se insertan las opciones a la listbox
ciudades= ["Cartagena", "Sincelejo", "Turbaco", "Arjona"]
for ciudade in ciudades:
    ciudad.insert(END, ciudade)


#crear radio button

variable = IntVar()


opcion1 = Radiobutton(ap, text="Hombre", variable=variable, value=1, command="",bg="black",fg="white")
opcion2 = Radiobutton(ap, text="Mujer", variable=variable, value=2, command="",bg="black",fg="white")
opcion3 = Radiobutton(ap, text="Helicoptero apache de combate", variable=variable, value=3, command="",bg="black",fg="white")
#posicionar radio button
opcion1.grid(column=0,row=10,padx=200, pady=0,sticky=W,ipadx=0)
opcion2.grid(column=0,row=11,padx=200, pady=0,sticky=W,ipadx=0)
opcion3.grid(column=0,row=12,padx=200, pady=0,sticky=W,ipadx=0)
#creamos un botton
p=Button(ap,text="Mostrar",command=funcion)

#Posicionamos el boton
p.grid(column=0,row=13,padx=300, pady=5,sticky=W,ipadx=0)
mainloop()
