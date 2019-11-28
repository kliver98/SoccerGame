import numpy as np
from keras.models  import Sequential
from keras.layers import Dense

def entrenar():
    '''[Enemigo_y,lineax_enemigo,porteria_atiro]'''
    '''para x & y: -1 posenemi<pos   0 posenemi=pos  1posene>pos '''
    training_data=np.array([[0,0,0],[0,0,1],[0,0,-1],[0,1,0],[0,1,1],[0,1,-1],[0,-1,0],[0,-1,1],[0,-1,-1],
                        [1,0,0],[1,0,1],[1,0,-1],[1,1,0],[1,1,1],[1,1,-1],[1,-1,0],[1,-1,1],[1,-1,-1],
                        [-1,0,0],[-1,0,1],[-1,0,-1],[-1,1,0],[-1,1,1],[-1,1,-1],[-1,-1,0],[-1,-1,1],[-1,-1,-1]],"float32")

    '''[movx,movy,patear]'''
    target_data=np.array([[1,-1,0],[0,0,1],[-1,1,0],[-1,-1,0],[0,0,1],[-1,1,0],[1,1,0],[0,0,1],[1,1,0],
                      [1,1,0],[0,0,1],[1,1,0],[1,1,0],[0,0,1],[1,1,0],[1,1,0],[0,0,1],[1,1,0],
                      [0,1,0],[0,0,1],[0,1,0],[-1,-1,0],[0,0,1],[-1,-1,0],[1,1,0],[0,0,1],[1,1,0]],"float32")


    model = Sequential()
    model.add(Dense(16, input_dim=3, activation='tanh'))
    model.add(Dense(3, activation='tanh'))

    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['binary_accuracy'])
    
    model.fit(training_data, target_data, epochs=1500)
    
    return model