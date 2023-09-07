import numpy as np
import matplotlib.pyplot as plt


class Grafica:
    def __init__(
            self,
            x1, 
            x2, 
            xs, 
            theta, 
            w0, 
            w1, 
            w2
    ):
        self.__x1 = x1
        self.__x2 = x2
        self.__xs = xs
        self.__theta = theta
        self.__w0 = w0
        self.__w1 = w1
        self.__w2 = w2


    # Función regresa el valor de m para el calculo de pendiente
    def m(self):
        return (-self.__w1)/self.__w2


    # Función regresa el valor de c para el calculo de pendiente
    def c(self):
        return (-self.__w0)/self.__w2


    # Función de Pendiente
    def y(self, m, x, c):
        return (m*x+c)


    # Llama a las funciones y, m, c para calcular segun los pesos dados
    def puntos(self):
        ys = []
        for x in self.__xs:
            y_aux = self.y(
                    self.m(),
                    x,
                    self.c()
                )
            ys.append(y_aux)
        # regresa un arreglo de arreglos con las coordenadas en Eje x y Eje y para la recta divisora
        return [self.__xs, ys]


    def listaPuntos(self, x1, x2):
        coordenadas = []
        for i in range(len(x1)):
            coordenadas.append((x1[i], x2[i]))
        return coordenadas


    def graficar(self):
        # weight vector
        w = np.array([self.__w0, self.__w1, self.__w2])
        # entry vector
        # x = np.array([(x1[0], x2[0]), (x1[1], x2[1]), (x1[2], x2[2]), (x1[3], x2[3])])
        x = np.array(self.listaPuntos(self.__x1, self.__x2))
        # mod entry vector
        xm = np.hstack((np.ones((len(self.__x1),1)), x))
        # arreglo de verdadero y falso Funcióna como compuerta AND
        validados = (np.dot(w, xm.T) >= 0)

        # Coordenadas de los dos puntos para la linea recta
        coordenadas = self.puntos()
        xs = coordenadas[0]
        ys = coordenadas[1]

        # Crear una figura y un eje de Matplotlib
        fig, ax = plt.subplots()

        # Graficar la línea
        ax.plot(xs, ys, color='green', linestyle='dashed', label='Clasificación Lineal', marker='o')

        # Graficar los puntos por True o False
        print(validados)
        for i in range(len(validados)):
            if validados[i]: # Valida si es Verdadero o Falso
                ax.scatter(self.__x1[i], self.__x2[i], color='red', marker='x', label='Puntos True') # Agrega el punto en Color Rojo verdadero
            else:
                ax.scatter(self.__x1[i], self.__x2[i], color='blue', marker='x', label='Puntos False') # Agrega el punto en Color azul falso

        # Establecer límites de los ejes x e y
        ax.set_xlim(0, self.__theta+1)
        ax.set_ylim(0, self.__theta+1)

        # Etiquetas y título
        ax.set_xlabel('X1')
        ax.set_ylabel('X2')
        ax.set_title('Clasificación Lineal')

        ax.grid(True)
        # Mostrar el gráfico
        # plt.show()
        return fig


if __name__ == '__main__':
    # Decalaración de puntos para x1 (Eje x) y x2 (Eje y)
    x1 = [0, 0, 1, 1, 1.1]
    x2 = [0, 1, 0, 1, 1.2]
    # Declaración de Puntos x1 (Eje X) de la recta divisora 
    xs = [0, 1]
    # Declaración de theta
    theta = 1.5
    # Declaración de Pesos
    w0 = -theta
    w1 = 1
    w2 = 1
    # Declaración de Objeto
    grafica = Grafica(x1, x2, xs, theta, w0, w1, w2)
    grafica.graficar()