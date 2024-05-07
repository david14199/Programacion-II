from tkinter import *
import matplotlib
from tkinter import messagebox
# Definir listas para almacenar los resultados de SJF1
SJF = []
rafa_SJF = []
FIFO= []
rafa_FIFO = []

main=Tk()
main.geometry("800x800")

def FIFO1():
    rafaga=rafa.get()
    int (rafaga)
    proceso=p.get()
    FIFO.append(proceso)
    rafa_FIFO.append(rafaga)
    messagebox.showinfo("muestra",message=f"{FIFO,rafa_FIFO}")
    print()


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
def SJF1():
    rafaga = int(rafa.get())
    proceso=p.get()
    SJF.append(proceso)
    rafa_SJF.append(rafaga)
    return [proceso, rafaga]
   

def SJF2():
    lista_principal = [SJF1()]
    lista_principal.sort(key=lambda x: x[1])
    for elemento in lista_principal:
        proceso, rafaga = elemento
        return proceso, rafaga
    

def MostrarGSJF(procesos, rafagas, algoritmo):
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
    
def mostrarG():
    proceso, rafaga = SJF2()
    MostrarGSJF(proceso, rafaga, "FIFO")


mainloop()