import pandas as pnd
import numpy as np
import JMPEstadisticas as jmp
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_dir, 'datos.csv')
raw_data = open(filename)
data = np.loadtxt(raw_data, delimiter=";",skiprows=1)
data=pnd.DataFrame({'Pesos':data})
stats = jmp.JMPEstadisticas(data["Pesos"])
stats.analisisCaracteristica()

