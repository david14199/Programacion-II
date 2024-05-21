import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from util.generic import Utilidades as utl
from Formularios.inicio import login1


class Registro(tk.Tk):
    usuarios = []
    contraseñas = []
    apell = []
    correos = []
    usar = []
    tipos = []
    archivo_usuarios = "user/usuarios.json"

    def __init__(self):
        super().__init__()
        self.title("Registro de Usuario") 
        self.geometry("824x650")
        self.resizable(False, False) 
        self.config(bg="black")
      

        # Titulos guias
        self.titulo_registror = tk.Label(self, text="REGISTRO DE USUARIO", font=("Cooper Black", 30), background="black", foreground="white")
        self.titulo_registror.place(x=200, y=100, height=28)
        
        self.nombrer = tk.Label(self, text="Ingrese su nombre", font=("Cooper Black", 15), background="black", foreground="white")
        self.nombrer.place(x=200, y=166)

        self.apellidor = tk.Label(self, text="Ingrese su apellido", font=("Cooper Black", 15), background="black", foreground="white")
        self.apellidor.place(x=200, y=225)

        self.correor = tk.Label(self, text="Ingrese su correo", font=("Cooper Black", 15), background="black", foreground="white")
        self.correor.place(x=200, y=285)

        self.nombre_de_usuarior = tk.Label(self, text="Ingrese su nombre de usuario", font=("Cooper Black", 15), background="black", foreground="white")
        self.nombre_de_usuarior.place(x=200, y=346)

        self.claver = tk.Label(self, text="Ingrese su contraseña a usar", font=("Cooper Black", 15), background="black", foreground="white")
        self.claver.place(x=200, y=406)

        # Ingreso de datos por el usuario
        self.nombre1r = tk.Entry(self, width=25, font=20, bg="black", foreground="white", border=0)
        self.nombre1r.place(x=200, y=194, height=22)
        self.apellido1r = tk.Entry(self, width=25, font=20, bg="black", foreground="white", border=0)
        self.apellido1r.place(x=200, y=253, height=22)
        self.correo1r = tk.Entry(self, width=35, font=20, bg="black", foreground="white", border=0)
        self.correo1r.place(x=200, y=313, height=22)
        self.nombre_de_usuario1r = tk.Entry(self, width=25, font=20, bg="black", foreground="white", border=0)
        self.nombre_de_usuario1r.place(x=200, y=374, height=22)
        self.clave1r = tk.Entry(self, width=30, font=20, bg="black", foreground="white", border=0, show="*")
        self.clave1r.place(x=200, y=434, height=22)

       

        tk.Frame(self, width=320, height=2, bg="white").place(x=200, y=215)
        tk.Frame(self, width=320, height=2, bg="white").place(x=200, y=275)
        tk.Frame(self, width=320, height=2, bg="white").place(x=200, y=334)
        tk.Frame(self, width=320, height=2, bg="white").place(x=200, y=395)
        tk.Frame(self, width=320, height=2, bg="white").place(x=200, y=455)

        # Botón enviar a base de datos
        self.botonr = tk.Button(self, text="Registrarse", command=self.reg, font=("Cooper Black", 18), border=5)
        self.botonr.place(x=200, y=500)
        self.botonr2 = tk.Button(self, text="Atras", command=self.atras, font=("Cooper Black", 18), border=5,padx=25)
        self.botonr2.place(x=380, y=500)



    def cargar_usuarios(self):
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "r") as file:
                for line in file:
                    username, password, apellido, correo, nombres,cliente = line.strip().split(",")
                    self.usuarios.append(username)
                    self.contraseñas.append(password)
                    self.apell.append(apellido)
                    self.correos.append(correo)
                    self.usar.append(nombres)
                    self.tipos.append(cliente)

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, "w") as file:
            for username, password, apellido, correo, nombres,cliente in zip(self.usuarios, self.contraseñas, self.apell, self.correos, self.usar,self.tipos):
                file.write(f"{username},{password},{apellido},{correo},{nombres},{cliente}\n")

    def registrar_usuario(self):
        nombre = self.nombre1r.get()
        apellido = self.apellido1r.get()
        correo = self.correo1r.get()
        nombre_de_usuario = self.nombre_de_usuario1r.get()
        clave = self.clave1r.get()
        tipo1="cliente"
        
        # Validación del correo
        if correo.isdigit():
            messagebox.showinfo("Error", message="El correo no puede contener solo números.")
            return
        elif correo.isalpha():
            messagebox.showinfo("Error", message="El correo no puede contener solo letras.")
            return
        elif correo.isspace():
            messagebox.showinfo("Error", message="El correo no puede tener espacios.")
            return

        # Verificar si el usuario ya existe
        if nombre_de_usuario in self.usuarios:
            messagebox.showinfo("Error", message="El usuario ya existe. Por favor, elija otro nombre de usuario.")
            return

        # Guardar el usuario en las listas y en el archivo
        self.usuarios.append(nombre_de_usuario)
        self.contraseñas.append(clave)
        self.apell.append(apellido)
        self.correos.append(correo)
        self.usar.append(nombre)
        self.tipos.append(tipo1)
        self.guardar_usuarios()

        messagebox.showinfo("Registro Exitoso", message="Usuario registrado exitosamente.")

        # Limpiar los campos de entrada
        self.nombre1r.delete(0, tk.END)
        self.apellido1r.delete(0, tk.END)
        self.correo1r.delete(0, tk.END)
        self.nombre_de_usuario1r.delete(0, tk.END)
        self.clave1r.delete(0, tk.END)

    def reg(self):
        self.cargar_usuarios()
        self.registrar_usuario()
    def atras(self):
        app=login1()

        self.destroy()
        app.mainloop()
        
        