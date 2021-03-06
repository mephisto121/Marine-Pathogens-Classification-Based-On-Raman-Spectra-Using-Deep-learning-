import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers
from tensorflow.keras.models import Model
input_shape = 1200
output_shape = 8
def model():
    input = layers.Input(shape=input_shape, name="input data")
    x1 = layers.Dense(1200, activation = 'relu')(input)
    x1 = layers.BatchNormalization()(x1)
    x1 = layers.Dropout(0.1)(x1)
    x1 = layers.Dense(1200, activation = 'relu')(x1)
    x1 = layers.BatchNormalization()(x1)
    x1 = layers.Dropout(0.1)(x1)
    x1 = layers.Dense(256, activation = 'relu')(x1)
    x1 = layers.BatchNormalization()(x1)
    x1 = layers.Dropout(0.1)(x1)
    x1 = layers.Dense(128, activation = 'relu')(x1)
    x1 = layers.BatchNormalization()(x1)
    x1 = layers.Dropout(0.1)(x1) 
    output = layers.Dense(8, activation = 'softmax')(x1) 
    model = Model(inputs = input, outputs = output)
    return model

def ready_model():
    model_train = model()
    return model_train