# Seminario de solucion de problemas de Inteligencia Artificial II
# Juan Manuel Romero Proa
# 218744872
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

from Grafica import Grafica
from GraficaVacia import GraficaVacia
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox, ttk, simpledialog

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__x = []
        self.__y = []
        self.__xs = [0, 1]
        self.__theta = tk.DoubleVar()
        self.__w0 = -self.__theta.get()
        self.__w1 = tk.DoubleVar(value=1)
        self.__w2 = tk.DoubleVar(value=1)
        self.__fig = None

        # Opciones de Configuración de la Ventana(Semi Automatico pero distingue pantalla principal)
        self._anchoVentana = 780
        self._altoVentana = 505

        self._xVentana = self.winfo_screenwidth() // 2 - self._anchoVentana // 2
        self._yVentana = self.winfo_screenheight() // 2 - self._altoVentana // 2

        self._posicion = f'{str(self._anchoVentana)}x{str(self._altoVentana)}+{str(self._xVentana)}+{str(self._yVentana-40)}'
        self.minsize(self._anchoVentana, self._altoVentana)
        self.geometry(self._posicion)

        # Configuracion de Estilo de la ventana
        self.title('Practica 1: Clasificador Lineal')
        self.iconbitmap('img/logo.ico')
        self.style = ttk.Style(self)

        # Configuración de Frame Prncipal
        self.principalFrame = tk.Frame(self)
        self.principalFrame.rowconfigure(index=0, weight=9)
        self.principalFrame.rowconfigure(index=1, weight=1)
        self.principalFrame.columnconfigure(index=0, weight=1)
        self.principalFrame.grid(row=0, column=0, sticky=tk.NSEW)

        # Comfiguración de Frame Superior
        self.upperFrame = tk.Frame(self.principalFrame)
        self.upperFrame.columnconfigure(index=0, weight=1)
        self.upperFrame.columnconfigure(index=1, weight=5)
        self.upperFrame.grid(row=0, column=0, sticky=tk.NSEW)

        # Configuración de Frame Inferior
        self.downFrame = tk.Frame(self.principalFrame, bg="#4C2A85")
        self.downFrame.grid(row=1, column=0, sticky=tk.NSEW)

        # Establece Atributo Canvas/Label como global de la clase
        self.canvas = None
        self.label = None
        self.graphFrame = None
        # Llama a la función que agrega los componenetes principales, al Frame Superior
        self.principalComponents(self.upperFrame)
        self.secondComponents(self.downFrame, '')


    # Función para manejar el evento de clic del mouse
    def onclick(self, event):
        if event.button == 1:
            x, y = event.xdata, event.ydata
            self.__x.append(float(f'{x:.2f}'))
            self.__y.append(float(f'{y:.2f}'))
            coordenadas = f'Coordenadas del clic: x={x:.2f}, y={y:.2f}'
            print(coordenadas)
            self.secondComponents(self.downFrame, coordenadas)
            self.generarGrafica()


    def isNum(self, P):
        # Puedes verificar si el contenido es un número intentando convertirlo a float
        try:
            float(P)
            return True
        except ValueError:
            return False


    def generarGraficaVacia(self):
        self.__x = []
        self.__y = []
        self.__fig = GraficaVacia(self.__theta.get()).generarGrafica()
        self.__fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.canvas = FigureCanvasTkAgg(self.__fig, self.graphFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=tk.NSEW)


    def generarGrafica(self):
        # Actualiza el valor de w0
        self.__w0 = -self.__theta.get()
        # Genera una gráfica utilizando eL Objeto Grafica con los atributos de Ventana
        self.__fig = Grafica(
            self.__x,
            self.__y,
            self.__xs,
            self.__theta.get(),
            self.__w0,
            self.__w1.get(),
            self.__w2.get()
        ).graficar()
        self.__fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.canvas = FigureCanvasTkAgg(self.__fig, self.graphFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=tk.NSEW)


    def validateEntry(self, entry, *args):
        valor = entry.get()
        if not self.isNum(valor):
            # Si no es un número válido, elimina el último carácter ingresado
            entry.delete(len(valor) - 1, tk.END)


    def principalComponents(self, frame):
        sidebarFrame = tk.Frame(frame, bg="#4C2A85")
        sidebarFrame.rowconfigure(index=0, weight=1)
        sidebarFrame.rowconfigure(index=1, weight=9)
        sidebarFrame.grid(row=0, column=0, sticky=tk.NSEW)

        self.graphFrame = tk.Frame(frame)
        self.graphFrame.grid(row=0, column=1, sticky=tk.NSEW)

        # Definición de variables locales
        theta = tk.StringVar(value='')

        # Funciones Locales
        def validateEntry(*args):
            self.validateEntry(entry_x1, *args)

        def graficar():
            if not self.__x:
                messagebox.showwarning(
                    "Advertencia", 
                    "No se Puede Graficar sin antes seleccionar puntos en el Plano\n\nFavor de seleccionar al menos un punto coordenado del Plano antes de Generar la Grafica"
                )
            else:
                self.generarGrafica()

        # Definicion de Propiedades visuales dentro de la Pestaña
        labelImg = tk.Label(
            sidebarFrame, 
            text='Juan Manuel Romero Proa\n218744872',
            bg="#4C2A85",
            fg='#ffffff'
            )
        labelImg.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.NSEW)

        label_x1 = tk.Label(sidebarFrame, text='θ: ', bg="#4C2A85", fg='#ffffff')
        label_x1.grid(row=2, column=0, sticky=tk.W)

        entry_x1 = ttk.Entry(sidebarFrame, width=20, textvariable=self.__theta)
        entry_x1.bind("<KeyRelease>", validateEntry)
        entry_x1.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

        label_w1 = tk.Label(sidebarFrame, text='W1: ', bg="#4C2A85", fg='#ffffff')
        label_w1.grid(row=3, column=0, sticky=tk.W)

        entry_w1 = ttk.Entry(sidebarFrame, width=20, textvariable=self.__w1)
        entry_w1.bind("<KeyRelease>", validateEntry)
        entry_w1.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

        label_w2 = tk.Label(sidebarFrame, text='W2: ', bg="#4C2A85", fg='#ffffff')
        label_w2.grid(row=4, column=0, sticky=tk.W)

        entry_w2 = ttk.Entry(sidebarFrame, width=20, textvariable=self.__w2)
        entry_w2.bind("<KeyRelease>", validateEntry)
        entry_w2.grid(row=4, column=1, padx=5, pady=5, sticky=tk.E)

        buttonGraficar = ttk.Button(sidebarFrame, text=f'Graficar', command=graficar)
        buttonGraficar.grid(row=5, column=0, columnspan=2, padx=5, pady=6, sticky=tk.NSEW)

        buttonLimpiar = ttk.Button(sidebarFrame, text=f'Limpiar', command=self.generarGraficaVacia)
        buttonLimpiar.grid(row=6, column=0, columnspan=2, padx=5, sticky=tk.NSEW)

        # Agrega el Canvas de MatplotLib a un Frame en especifico
        self.generarGraficaVacia()


    def secondComponents(self, frame, text):
        if self.label:
            self.label.destroy()
        self.label = tk.Label(frame, text=f'{text}', bg="#4C2A85")
        self.label.configure(font=("Arial", 14), fg='#ffffff')
        self.label.pack()


if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()