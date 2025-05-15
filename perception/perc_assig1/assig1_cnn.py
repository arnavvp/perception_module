import tensorflow as tf
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Input, Flatten, Conv2D
#from tensorflow.keras.layers.convolutional import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import sparse_categorical_crossentropy
import numpy as np
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

gray_scale = 255

x_train = x_train.astype('float32') / gray_scale
x_test = x_test.astype('float32') / gray_scale

#Neural network:

model = Sequential([
    Input(shape = (28,28,1)),
    Conv2D(128, kernel_size=(2,2), activation = 'relu',padding = 'same'),
    Conv2D(64, kernel_size=(2,2), activation = 'relu',padding = 'same'), #complexity badhegi
    Flatten(),
    Dense(10, activation = 'softmax')
])

model.compile(Adam(learning_rate=0.001),loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, batch_size = 10, epochs = 20, shuffle=True, verbose = 2)