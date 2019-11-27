#librerias
from keras.models import model_from_json
from client.bots import red_neuronal_1 as rn1
from client.bots import entreno_red_gol as rn2

NOMBRE_ARCHIVO_1 = "modeloAgarrar"
NOMBRE_ARCHIVO_2 = "modeloGol"

def iniciar():
    modelos = []
    mod_1 = cargar_modelo(NOMBRE_ARCHIVO_1)
    if mod_1==None: #Si no habia ningun modelo guardado, se crea
            mod_1 = rn1.entrenar()
            guardar_modelo(mod_1,NOMBRE_ARCHIVO_1)
    modelos.append(mod_1)
    
    mod_2 = cargar_modelo(NOMBRE_ARCHIVO_2)
    if mod_2==None: #Si no habia ningun modelo guardado, se crea
            mod_2 = rn2.entrenar()
            guardar_modelo(mod_2,NOMBRE_ARCHIVO_2)
    modelos.append(mod_2)
    #Poner el otro modelo por que se deben cargar una sola vez, si no el juego se ve lagueado
    return modelos

def calcular(jugadores, balon, modelos):
    #Este metodo es el encargado de actualizar las posicinoes de los jugadores pasados por parametro. No devuelve nada, actualiza los mismo objetos del model
    print(f"{jugadores==None}-{balon==None}-{modelos==None}")
    if balon.get_usuario()=="": #la red 1 tiene que hacer que atrape el balon
        pass
    else: #la red 2 tiene que hacer gol
        pass

def convertir_a_entrada(tipo,jugador):
    #de acuerdo al tipo (0 para agarrar balon, 1 para hacer gol) devuelve un arreglo en formato de  estimulo
    if tipo==0:
        pass
    elif tipo==1:
        pass

def guardar_modelo(model,nombre_archivo):
    # serializar el modelo a JSON
    model_json = model.to_json()
    with open(f"{nombre_archivo}.json", "w") as json_file:
        json_file.write(model_json)
    # serializar los pesos a HDF5
    model.save_weights(f"{nombre_archivo}.h5")
    print("Modelo Guardado!")

def cargar_modelo(nombre_archivo):
    # cargar json y crear el modelo
    file_name = f'{nombre_archivo}.json'
    try:
        json_file = open(file_name, 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # cargar pesos al nuevo modelo
        loaded_model.load_weights(f"{nombre_archivo}.h5")
        print("Cargado modelo desde disco.")
        # Compilar modelo cargado y listo para usar.
        loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
    except Exception as e:
        return None
    return loaded_model