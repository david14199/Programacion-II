from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox

# Definir listas para almacenar los resultados de SJF y FIFO
SJF = []
rafa_SJF = []
FIFO = []
rafa_FIFO = []

# Crear la ventana principal
main = Tk()
main.geometry("800x600")

def FIFO1():
    try:
        rafaga = int(rafa.get())
        proceso = p.get()
        FIFO.append(proceso)
        rafa_FIFO.append(rafaga)
        messagebox.showinfo("Información", message=f"Proceso {proceso} con ráfaga {rafaga} añadido.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número entero para la ráfaga.")

def GFIFO(procesos, rafagas, algoritmo):
    fig, ax = plt.subplots()
    colores = plt.cm.get_cmap('tab10', len(procesos))  # Paleta de colores
    tiempo_inicio = 0
    for i, (proceso, rafaga) in enumerate(zip(procesos, rafagas)):
        color = colores(i)  # Color único para cada proceso
        ax.broken_barh([(tiempo_inicio, rafaga)], (i, 1), facecolors=(color,))
        ax.text(tiempo_inicio + rafaga / 2, i + 0.5, proceso, ha='center', va='center', color='white')
        tiempo_inicio += rafaga
    ax.set_xlim(0, max(tiempo_inicio, max(rafagas)) + 1)
    ax.set_ylim(0, len(procesos))
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Proceso')
    ax.set_title(f'Diagrama de Gantt ({algoritmo})')
    ax.set_yticks(range(len(procesos)))  # Establecer etiquetas de eje Y
    ax.set_yticklabels(procesos)  # Etiquetas de eje Y son los nombres de los procesos
    plt.grid(True)
    plt.show()

def mostrarGFIFO():
    if not FIFO or not rafa_FIFO:
        messagebox.showerror("Error", "No hay datos para mostrar. Por favor, agrega procesos y ráfagas primero.")
        return
    GFIFO(FIFO, rafa_FIFO, "FIFO")

def agregar_proceso_sjf():
    try:
        rafaga = int(rafa.get())
        proceso = p.get()
        SJF.append(proceso)
        rafa_SJF.append(rafaga)
        messagebox.showinfo("Información", message=f"Proceso {proceso} con ráfaga {rafaga} añadido.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número entero para la ráfaga.")

def planificar_sjf(procesos, rafagas):
    # Combinar procesos y ráfagas en una lista de tuplas y ordenar por ráfaga
    lista_procesos = list(zip(procesos, rafagas))
    lista_procesos.sort(key=lambda x: x[1])
    
    procesos_ordenados = [proceso for proceso, rafaga in lista_procesos]
    rafagas_ordenadas = [rafaga for proceso, rafaga in lista_procesos]
    
    return procesos_ordenados, rafagas_ordenadas

def mostrar_gantt_sjf(procesos, rafagas):
    fig, ax = plt.subplots()
    colores = plt.cm.get_cmap('tab10', len(procesos))  # Paleta de colores
    tiempo_inicio = 0
    
    for i, (proceso, rafaga) in enumerate(zip(procesos, rafagas)):
        color = colores(i)  # Color único para cada proceso
        ax.broken_barh([(tiempo_inicio, rafaga)], (i, 1), facecolors=(color,))
        ax.text(tiempo_inicio + rafaga / 2, i + 0.5, proceso, ha='center', va='center', color='white')
        tiempo_inicio += rafaga
    
    ax.set_xlim(0, tiempo_inicio + 1)
    ax.set_ylim(0, len(procesos))
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Proceso')
    ax.set_title('Diagrama de Gantt (SJF)')
    ax.set_yticks(range(len(procesos)))
    ax.set_yticklabels(procesos)
    plt.grid(True)
    plt.show()

def mostrar_sjf():
    if not SJF or not rafa_SJF:
        messagebox.showerror("Error", "No hay datos para mostrar. Por favor, agrega procesos y ráfagas primero.")
        return
    procesos_ordenados, rafagas_ordenadas = planificar_sjf(SJF, rafa_SJF)
    mostrar_gantt_sjf(procesos_ordenados, rafagas_ordenadas)

def calcular_fifo():
    try:
        tiempo_llegada = list(map(int, tll.get().split(',')))
        tiempo_ejecucion = list(map(int, teje.get().split(',')))
        tiempo_salida = list(map(int, tsalida.get().split(',')))
        rafaga_cpu = list(map(int, traf.get().split(',')))

        if not (len(tiempo_llegada) == len(tiempo_ejecucion) == len(rafaga_cpu) == len(tiempo_salida)):
            raise ValueError("Las listas deben tener la misma longitud")

        n = len(tiempo_llegada)
        tiempo_espera = [0] * n
        tiempo_respuesta = [0] * n

        # Calcular tiempos de espera y de respuesta
        for i in range(n):
            tiempo_espera[i] = tiempo_ejecucion[i] - tiempo_llegada[i]
            tiempo_respuesta[i] = tiempo_salida[i] - tiempo_llegada[i]

        tiempo_espera_promedio = sum(tiempo_espera) / n
        tiempo_respuesta_promedio = sum(tiempo_respuesta) / n

        messagebox.showinfo("Resultados FIFO", 
                            f"Tiempo de Espera: {tiempo_espera}\n"
                            f"Tiempo de Respuesta: {tiempo_respuesta}\n"
                            f"Tiempo de Espera Promedio: {tiempo_espera_promedio:.2f}\n"
                            f"Tiempo de Respuesta Promedio: {tiempo_respuesta_promedio:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", f"Error en los datos ingresados: {e}")

# Configurar la interfaz gráfica
titles = Label(main, text="Algoritmos de Planificación", font=("arial", 16))
titles.place(x=300, y=0)
proceso_label = Label(main, text="Nombre del Proceso").place(x=250, y=50)
rafaga_label = Label(main, text="Cantidad de Ráfaga").place(x=250, y=100)

p = Entry(main)
p.place(x=400, y=50)
rafa = Entry(main)
rafa.place(x=400, y=100)


# Botones para agregar y mostrar los diagramas FIFO y SJF
AgregarF = Button(main, text="Agregar FIFO", command=FIFO1).place(x=350, y=200)
MostrarF = Button(main, text="Mostrar FIFO", command=mostrarGFIFO).place(x=450, y=200)

AgregarSJF = Button(main, text="Agregar SJF", command=agregar_proceso_sjf).place(x=350, y=250)
MostrarSJF = Button(main, text="Mostrar SJF", command=mostrar_sjf).place(x=450, y=250)

# Subtítulo para la sección de cálculo
calculo_title = Label(main, text="Cálculo (FIFO)", font=("arial", 16))
calculo_title.place(x=350, y=300)

# Campos para introducir los datos de cálculo
tll_label = Label(main, text="Tiempos de Llegada (separados por coma)").place(x=150, y=350)
teje_label = Label(main, text="Tiempos de Ejecución (separados por coma)").place(x=150, y=400)
traf_label = Label(main, text="Ráfagas de CPU (separadas por coma)").place(x=150, y=450)
tsalida_label = Label(main, text="Tiempo de Salida (separado por coma)").place(x=150, y=500)
tsalida = Entry(main)
tsalida.place(x=450, y=500)

tll = Entry(main)
tll.place(x=450, y=350)
teje = Entry(main)
teje.place(x=450, y=400)
traf = Entry(main)
traf.place(x=450, y=450)

# Botón para realizar el cálculo
calcular_btn = Button(main, text="Calcular", command=calcular_fifo).place(x=380, y=550)

# Iniciar el bucle principal de la interfaz gráfica
main.mainloop()