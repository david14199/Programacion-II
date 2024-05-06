import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "usuario" and password == "contraseña":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Nombre de usuario o contraseña incorrectos")
    entry_username.setvar(-1)

ventana = tk.Tk()
ventana.title("Login")

frame = tk.Frame(ventana)
frame.place(relx=0.5, rely=0.5, anchor="center")


ventana.geometry("600x600")
ventana.config(bg="sky blue")
# Crea los campos de entrada para el nombre de usuario y la contraseña
label_username = tk.Label(frame, text="Nombre de usuario:")
label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(frame, text="Contraseña:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Crear el botón de inicio de sesión
login_button = tk.Button(frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


ventana.mainloop()