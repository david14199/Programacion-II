from Formularios.Registro import *
from Formularios.admin import *
import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import os



class login1(tk.Tk):
    usuarios = []
    contraseñas = []
    archivo_usuarios = "user/usuarios.json"
    tipos = []
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.geometry("1024x650")
        self.resizable(False, False)
        self.config(bg="black")
        # Titulos y guias
        self.titulo_registro = tk.Label(self, text="INICIO DE SESION", font=("Cooper Black", 30), background="black", foreground="white")
        self.titulo_registro.place(x=400, y=100, height=28)

        self.nombre_usuario = tk.Label(self, text="Ingrese su nombre", font=("Cooper Black", 15), background="black", foreground="white")
        self.nombre_usuario.place(x=400, y=170)

        self.clave = tk.Label(self, text="Ingrese su clave", font=("Cooper Black", 15), background="black", foreground="white")
        self.clave.place(x=400, y=270)

        self.nombre_usuario_entry = tk.Entry(self, width=25, font=20, bg="black", foreground="white", border=0)
        self.nombre_usuario_entry.place(x=400, y=200, height=22)

        self.clave_entry = tk.Entry(self, width=25, font=20, bg="black", foreground="white", border=0, show="*")
        self.clave_entry.place(x=400, y=300, height=22)

        tk.Frame(self, width=320, height=2, bg="white").place(x=400, y=222)
        tk.Frame(self, width=320, height=2, bg="white").place(x=400, y=322)

        # Botón
        self.boton_inicio_sesion = tk.Button(self, text="Iniciar Sesión", command=self.inicio_sesion, font=("Cooper Black", 16), border=5)
        self.boton_inicio_sesion.place(x=400, y=370)
        self.boton_registro=tk.Button(self,text="Registrar",font=("Cooper Black", 16), border=5,padx=10,command=self.registro1)
        self.boton_registro.place(x=580, y=370)
        self.FONDO = utl.leer_imagen(r"imagenes/inicio-img.png", (250, 250))
        # Frame para la imagen
        self.frame_imagen = tk.Frame(self, bd=0, width=320, relief=tk.SOLID, padx=30, pady=210, bg="black")
        self.frame_imagen.pack(side=tk.LEFT, expand=tk.NO, fill=tk.BOTH)
        self.label_imagen = tk.Label(self.frame_imagen, bg="black",image=self.FONDO)
        self.label_imagen.place(x=50, y=0, relwidth=1, relheight=1)

        # Cargar imagen
     
        # Cargar usuarios
        self.cargar_usuarios()

    def cargar_usuarios(self):
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "r") as file:
                for line in file:
                    username, password, apellido, correo, nombres,cliente = line.strip().split(",")
                    self.usuarios.append(username)
                    self.contraseñas.append(password)
                    self.tipos.append(cliente)

    def inicio_sesion(self):
        username = self.nombre_usuario_entry.get()
        password = self.clave_entry.get()

        if username in self.usuarios:
            index = self.usuarios.index(username)
            if self.contraseñas[index] == password and self.tipos[index] =="Cliente":
                messagebox.showinfo("Inicio", message="Inicio de sesión exitoso")
                self.nombre_usuario_entry.delete(0, tk.END)
                self.clave_entry.delete(0, tk.END)
                self.destroy()
            if self.contraseñas[index] == password and self.tipos[index] =="admin":
                messagebox.showinfo("Inicio", message="Inicio de sesión exitoso")
                self.nombre_usuario_entry.delete(0, tk.END)
                self.clave_entry.delete(0, tk.END)
                self.destroy()
                app = admin()
                app.mainloop()

            else:
                messagebox.showinfo("Error", message="Contraseña incorrecta")
                self.clave_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", message="Usuario no encontrado")
            self.nombre_usuario_entry.delete(0, tk.END)
    def registro1(self):
        self.withdraw()
        app = Registro()
        self.destroy()
        app.mainloop()
       
  
  
