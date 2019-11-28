import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

def entrenar():
    # datos de entreno
    print("Hola")
    training_data = np.array([[1,-1],[1,0],[1,1],
                          [0,-1],[0,0],[0,1],
                          [-1,-1],[-1,0],[-1,1]],"float32")

    # resultados que se obtienen, en el mismo orden
    target_data = np.array([[-1,-1],[-1,0],[-1,1],[0,-1],[0.045,0.13],[0,1],[1,-1],[1,0],[1,1]], "float32")
    model = Sequential()
    model.add(Dense(3, input_dim=2, activation='tanh'))
    model.add(Dense(2, activation='tanh'))
    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['binary_accuracy'])
    
    print("Chiax1")
    model.fit(training_data, target_data, epochs=1500)
    print("Chia")

    # evaluamos el modelo
    #scores = model.evaluate(training_data, target_data)

    #print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    #print (model.predict(training_data).round())
    
    #prueba = np.array([[1,0]])
    #print(model.predict(np.array(prueba)).round())
    
    return model