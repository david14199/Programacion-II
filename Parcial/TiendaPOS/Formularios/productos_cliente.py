import tkinter as tk
import os
from tkinter import messagebox


class comprar(tk.Tk):
    archivo_productos = r"Formularios/productosdb/productos.txt"
    productos = {}
    productos_carrito = []
    def __init__(self):
        super().__init__()
        self.title("Comprar")
        self.geometry("800x650")
        self.resizable(False, False)
        self.config(bg="black")
        self.cargar_productos()
        self.titulo_comprar = tk.Label(self, text="COMPRAR", font=("Cooper Black", 30), bg="black", fg="white")
        self.titulo_comprar.place(x=200, y=100)
        self.comprar = tk.Button(self, text="COMPRAR", command=self.calcular_precios)
        self.comprar.place(x=200, y=200)
        self.comprar = tk.Button(self, text="Añadir al carrito", command=self.anadir_a_lista)
        self.comprar.place(x=300, y=200)
        self.productos1=tk.Listbox(self, width=60,height=5, selectmode="single")
        self.productos1.place(x=200, y=300)




        self.cargar_productos()
        self.actualizar_listbox()
        self.mainloop()

    def comprar1(self):
        seleccionados = self.productos1.curselection()
        for index in seleccionados:
            elemento = self.productos1.get(index)
        print(elemento)
 
 
    def cargar_productos(self):
        print("Intentando cargar productos...")  # Verificación de inicio de la función
        if os.path.exists(self.archivo_productos):
            print(f"Archivo {self.archivo_productos} encontrado.")  # Verificación de existencia del archivo
            with open(self.archivo_productos, "r") as file:
                for line in file:
                    print(f"Leyendo línea: {line.strip()}")  # Imprimir cada línea leída
                    producto, inventario, precio = line.strip().split(",")
                    self.productos[producto] = {"inventario": int(inventario), "precio": float(precio)}
                    print(self.productos)  # Imprimir el diccionario después de cada adición
        else:
            print(f"Archivo {self.archivo_productos} no encontrado.")   # Archivo no encontrado # Archivo no encontrado
    def actualizar_listbox(self):
        self.productos1.delete(0, tk.END)
        for producto, inventario in self.productos.items():
            display_text = f"Producto: {producto}, Inventario: {inventario}"
            self.productos1.insert(tk.END, display_text)
    def anadir_a_lista(self):
        seleccionados = self.productos1.curselection()
        for index in seleccionados:
            producto_seleccionado = self.productos1.get(index)
            # Añadir el producto seleccionado al carrito (en este caso, una lista)
            self.productos_carrito.append(producto_seleccionado)
            messagebox.showinfo("Producto añadido", f"Producto '{producto_seleccionado}' añadido al carrito.")
    def calcular_precios(self):
    # Precios sin IVA
        total_sin_iva = 0
        for producto in self.productos_carrito :
            if producto in self.productos and "precio" in self.productos[producto]:
                total_sin_iva += self.productos[producto]["precio"]

    # Total con IVA (19%)
        total_con_iva = total_sin_iva * 1.19

    # Mostrar resultados
        messagebox.showinfo("Precios", f"Total sin IVA: ${total_sin_iva:.2f}\nTotal con IVA (19%): ${total_con_iva:.2f}")
comprar()