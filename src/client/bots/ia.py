#librerias
import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Dense

def calcular(jugadores):
    #Este metodo es el encargado de actualizar las posicinoes de los jugadores pasados por parametro. No devuelve nada, actualiza los mismo objetos del model
    pass

def convertir_a_entrada(tipo,jugador):
    #de acuerdo al tipo (0 para agarrar balon, 1 para hacer gol) devuelve un arreglo en formato de  estimulo
    if tipo==0:
        pass
    elif tipo==1:
        pass
    
print(keras.__version__)