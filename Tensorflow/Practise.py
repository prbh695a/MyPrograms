import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import matplotlib.pyplot as plt

zipDir="/Users/prateekb/Downloads/PythonDS/Tensorflow"
baseDir=os.path.join(zipDir,'cats_and_dogs_filtered')
train_dir=os.path.join(baseDir,'train')
validation_dir=os.path.join(baseDir,'validation')

train_cat_dir=os.path.join(train_dir,'cats')
train_dog_dir=os.path.join(train_dir,'dogs')
validation_cat_dir=os.path.join(validation_dir,'cats')
validation_dog_dir=os.path.join(validation_dir,'dogs')

total_train_cat_dir=len(os.listdir(train_cat_dir))
total_train_dog_dir=len(os.listdir(train_dog_dir))
total_validation_cat_dir=len(os.listdir(validation_cat_dir))
total_validation_dog_dir=len(os.listdir(validation_dog_dir))

total_train_num=total_train_cat_dir+total_train_dog_dir
total_validation_num=total_validation_cat_dir+total_validation_dog_dir

batch=100
image=150

train_gen=ImageDataGenerator(
    rescale=1./255,
    width_shift_range=.2,
    height_shift_range=.2,
    zoom_range=.2,
    horizontal_flip=True,
    shear_range=.2,
    rotation_range=40,
    fill_mode='nearest'
)


train_data_gen=train_gen.flow_from_directory(
    directory=train_dir,
    batch_size=batch,
    shuffle=True,
    target_size=[image,image],
    class_mode='binary'
)

validation_gen=ImageDataGenerator(
    rescale=1./255,
)

validation_data_gen=validation_gen.flow_from_directory(
    directory=validation_dir,
    batch_size=batch,
    target_size=[image, image],
    class_mode='binary'
)


model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=[image,image,3]),
    tf.keras.layers.MaxPool2D((2,2)),

    tf.keras.layers.Conv2D(64, (3, 3),activation='relu',),
    tf.keras.layers.MaxPool2D((2, 2)),

    tf.keras.layers.Conv2D(128, (3, 3),activation='relu'),
    tf.keras.layers.MaxPool2D((2, 2)),

    tf.keras.layers.Dropout(.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation='relu'),
    tf.keras.layers.Dense(2,activation=tf.nn.softmax)
])

model.compile(optimizer='adam',loss=tf.losses.sparse_categorical_crossentropy,metrics=['accuracy'])

epoch=2
history=model.fit_generator(
    train_data_gen,
    epochs=epoch,
    steps_per_epoch=total_train_num//batch,
    validation_data=validation_data_gen,
    validation_steps=total_validation_num//batch
)

acc=history.history['accuracy']
loss=history.history['loss']

val_acc=history.history['val_accuracy']
val_loss=history.history['val_loss']

epochs_range=range(epoch)

plt.figure(figsize=(8,8))
plt.subplot(1,2,1)
plt.plot(epochs_range,acc,label='Training accuracy')
plt.plot(epochs_range,val_acc,label='Validation accuracy')
plt.legend(loc='lower right')
plt.title("accuracy graph")

plt.subplot(1,2,2)
plt.plot(epochs_range,loss,label='Training loss')
plt.plot(epochs_range,val_loss,label='Validation loss')
plt.legend(loc='lower left')
plt.title("loss graph")

plt.show()