import keras
keras.__version__
import numpy as np

#---------------------load data-----------------*
f = np.load('mnist.npz')
train_images,train_labels = f['x_train'],f['y_train']
test_images,test_labels = f['x_test'],f['y_test']
f.close()

train_images.shape
test_images.shape

train_labels
test_labels

len(train_labels)
len(test_labels)

#------------build neural network-----------------*
from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

#---------loss function, optimizer and metrics----*
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

#----------reshape images to float----------------* 
'''
Preprocessing by reshaping. Previously, training images 
were stored in an array of shape (60000, 28, 28) of type uint8 
with values in the [0, 255]. Now convert it into a float32 
array of shape (60000, 28 * 28) with values between 0 and 1.
'''
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

#-----------------encode labels-------------------*
from keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#------------------training-----------------------*
network.fit(train_images, train_labels, epochs=5, batch_size=128)

#---------------training result-------------------*
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc:', test_acc)
#-------------Save model--------------------*
network.save('model.h5')

