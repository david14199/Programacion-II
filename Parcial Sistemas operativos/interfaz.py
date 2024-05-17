from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
# Definir listas para almacenar los resultados de SJF1
SJF = []
rafa_SJF = []
FIFO= []
rafa_FIFO = []

main=Tk()
main.geometry("800x800")

def FIFO1():
    rafaga=int(rafa.get())
    proceso=p.get()
    FIFO.append(proceso)
    rafa_FIFO.append(rafaga)
    messagebox.showinfo("muestra",message=f"{FIFO,rafa_FIFO}")

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
    GFIFO(FIFO, rafa_FIFO, "FIFO") 
#
def agregar_proceso():
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
#
titles=Label(main,text="Algoritmos de planifiacion",font=("arial",16))
titles.place(x=300,y=0   )
proceso=Label(main,text="Nombre del proceso").place(x=250,y=200)
rafaga=Label(main,text="Cantidad de rafaga").place(x=250,y=250  )
#
p= Entry(main)
p.place(x=400,y=200)
rafa=Entry(main)
rafa.place(x=400,y=250)

#
AgregarF=Button(main,text="Agregar FiFO",command=FIFO1).place(x=350,y=300)
MosrtarF=Button(main,text   = "Mostrar FIFO",command=mostrarGFIFO).place(x=450,y=300)
#
AgregarSJF=Button(main,text="Agregar SJFO",command=SJF1).place(x=350,y=350)
mostrarGJJF=Button(main,text = "Agregar JFO",command=MostrarGSJF).place(x=450,y=350)

mainloop()