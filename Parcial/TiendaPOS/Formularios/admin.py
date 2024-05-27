import tkinter as tk 
from PIL import Image, ImageTk

import tkinter as tk

class admin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Configuraciones de administrador")
        self.geometry("800x650")
        self.resizable(False, False)
        self.config(bg="black")

        # Títulos guías
        self.titulo_registror = tk.Label(self,text="SESION DE ADMINISTRADOR", font=("Cooper Black", 30), background="black", foreground="white")
        self.titulo_registror.place(x=150, y=100, height=28)

