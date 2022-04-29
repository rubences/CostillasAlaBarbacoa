from math import *
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
import numpy as np
import sys



class JMPEstadisticas:

    def __init__(self,caracteristica):
        self.caracteristica = caracteristica

    def calculoMediaAritmetica(self):

        n = self.caracteristica.count()
        sumaValoresObservaciones = 0
        mediaAritmetica = 0
        for valorObservacion in self.caracteristica:
            sumaValoresObservaciones += valorObservacion

        mediaAritmetica = sumaValoresObservaciones / n
        return mediaAritmetica

    def calculoVarianzaDesviacionTipica(self):
        n = self.caracteristica.count()
        mediaAritmetica = self.caracteristica.mean()
        varianza = 0
        c3 = 0
        for valorObservacion in self.caracteristica:
            c1 = valorObservacion - mediaAritmetica
            c2 = c1 * c1
            c3 += c2

        varianza = c3 / (n - 1)

        desviacionTipica = sqrt(varianza)

        return ([varianza, desviacionTipica])
    def Calculos(self,peso):
        n=peso-self.calculoMediaAritmetica()
        valor=n/ self.calculoVarianzaDesviacionTipica()[1]

    def calculo (self, peso):
        valor=norm.cdf(peso, self.calculoMediaAritmetica(), self.calculoVarianzaDesviacionTipica()[1])
        return valor
    def visualizacion(self,peso):
        caracteristica = self.caracteristica.sort_values()
        caracteristica = caracteristica.reset_index(drop=True)
        resultado=self.calculo(peso)
        x_axis = np.arange(caracteristica[0], caracteristica[len(caracteristica)-1], 0.01)
        mean = statistics.mean(x_axis)
        sd = statistics.stdev(x_axis)

        plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
        plt.axvline(peso, color='red', linestyle='dashed', linewidth=1)
        plt.text(peso-5,0.05,"La probabilidad es: "+str(resultado),fontsize=14)
        plt.show()


    def analisisCaracteristica(self):

        print("-----------------------------------------")
        print("      MEDIDA DE TENDENCIA CENTRAL        ")
        print("-----------------------------------------\n")

        print("-- CANTIDAD DE OBSERVACIONES --")
        # -Cantidad de observaciones
        n = self.caracteristica.count()
        print("Cantidad de observaciones = " + str(n))

        # -Media artimética:
        print("\n-- MEDIA --")
        media = self.calculoMediaAritmetica()
        print("Peso medio = " + str(media))
        print("> Observaciones: Si todas las observaciones tuvieran el mismo valor (reparto equitativo), este sería " + str(media))


        print("\n\n-----------------------------------------")
        print("      MEDIDA DE DISPERSION        ")
        print("-----------------------------------------\n")

        varianzaDesviacionTipica = self.calculoVarianzaDesviacionTipica()

        print("\n-- DESVIACION TIPICA --")
        print("Desviación típica calculada = " + str(varianzaDesviacionTipica[1]))


        print("\n-- PROBABILIDADES --")
        print("Introduzca el número para calcular la probabilidad de que una naranja escogida al azar pese menos que ese número")
        peso=int(input())
        print(f"La probabilidad de que una naranja pese menos que {peso} es de:")
        print(self.calculo(peso))
        self.visualizacion(peso)