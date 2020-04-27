import tensorflow as tf
import logging
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
logger=tf.get_logger()
logger.setLevel(logging.INFO)

#Loading Data
data=keras.datasets.fashion_mnist

#Passing training and test data
(train_images,train_labels),(test_images,test_labels) = data.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal',      'Shirt',   'Sneaker',  'Bag',   'Ankle boot']

#print(train_images.shape)
#print(train_labels.shape)
#print(test_images.shape)
#print(test_labels.shape)

def normalize(images):
    images=tf.cast(images,tf.float32)
    images=images/255.0
    return images

train_images=normalize(train_images)
test_images=normalize(test_images)

#plt.figure()
#plt.imshow(train_images[0],cmap=plt.cm.binary)
#plt.colorbar()
#plt.grid(False)
#plt.show()

'''plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i],cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
'''
model=tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=[28,28]),
    tf.keras.layers.Dense(128,activation=tf.nn.relu),
    tf.keras.layers.Dense(10,activation=tf.nn.softmax)
])

model.compile(optimizer='adam',loss=tf.keras.losses.sparse_categorical_crossentropy,metrics=['accuracy'])
model.fit(train_images,train_labels,epochs=10)

test_loss,test_acc=model.evaluate(test_images,test_labels,verbose=2)
print(test_acc)a

probability_model=tf.keras.Sequential([
    model,tf.keras.layers.Softmax()
])
predictions=probability_model(test_images)
print(predictions[0])
print(np.argmax(predictions[0]))
print(test_labels[0])