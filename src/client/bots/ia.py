#librerias
import numpy as np
from keras.models import model_from_json
from client.bots import red_neuronal_1 as rn1
from client.model.balon import Balon

def calcular(jugadores, balon):
    #Este metodo es el encargado de actualizar las posicinoes de los jugadores pasados por parametro. No devuelve nada, actualiza los mismo objetos del model
    modelo = cargar_modelo()
    if balon.get_usuario()=="": #la red 1 tiene que hacer que atrape el balon
        if modelo==None: #Si no habia ningun modelo guardado, se crea
            modelo = rn1.entrenar()
            guardar_modelo(modelo)
        #print("Prediciendo valores....")
        #for i in range(0,101):
        #    yy = -i/100
        #    xx = 0
        #    val = modelo.predict(np.array(np.array([[xx,yy]])))
        #    speed = 1
        #    decimals = 2
        #    print(f"[{xx}    {yy}] -> x:{str(round((val[0][0])*speed, decimals))} - y:{str(round((val[0][1])*speed, decimals))}")
        #print("fin prediccion de valores....")
    else: #la red 2 tiene que hacer gol
        pass

def convertir_a_entrada(tipo,jugador):
    #de acuerdo al tipo (0 para agarrar balon, 1 para hacer gol) devuelve un arreglo en formato de  estimulo
    if tipo==0:
        pass
    elif tipo==1:
        pass

def guardar_modelo(model):
    # serializar el modelo a JSON
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    # serializar los pesos a HDF5
    model.save_weights("model.h5")
    print("Modelo Guardado!")

def cargar_modelo():
    # cargar json y crear el modelo
    file_name = 'model.json'
    try:
        json_file = open(file_name, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # cargar pesos al nuevo modelo
        loaded_model.load_weights("model.h5")
        print("Cargado modelo desde disco.")
        # Compilar modelo cargado y listo para usar.
        loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
    except Exception as e:
        return None
    return loaded_model

b = Balon()
b.set_usuario("") #Llamaria a red neuronal 1
calcular(None,b)