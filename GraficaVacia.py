import matplotlib.pyplot as plt


class GraficaVacia:
    def __init__(self, limite):
        self.__fig = None
        self.__ax = None
        self.__limite = limite

    def generarGrafica(self):
        # Crear una figura vacía
        self.__fig, self.__ax = plt.subplots()

        # Establecer límites de los ejes x e y
        self.__ax.set_xlim(0, self.__limite+1)
        self.__ax.set_ylim(0, self.__limite+1)

        # Etiquetas de ejes
        self.__ax.set_xlabel('X1')
        self.__ax.set_ylabel('X2')

        # Título del gráfico
        self.__ax.set_title('Clasificación Lineal')

        # Habilitar la cuadrícula
        self.__ax.grid(True)

        # Retorna la figura para colgarla en un Frame de Tkinter
        return self.__fig