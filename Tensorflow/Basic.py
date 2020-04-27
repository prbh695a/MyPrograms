import tensorflow as tf
import numpy as np
import logging
import matplotlib.pyplot as plt
logger = tf.get_logger()
logger.setLevel(logging.INFO)
celsius_q=np.array([-40,-10,0,8,15,22,38],dtype=float)
farheniet_f=np.array([-40,14,32,46,59,72,100],dtype=float)

l0=tf.keras.layers.Dense(units=1,input_shape=[1])
model=tf.keras.Sequential(l0)

model.compile(loss="mean_squared_error",optimizer=tf.keras.optimizers.Adam(.1))
history=model.fit(x=celsius_q,y=farheniet_f,epochs=500,verbose=False)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.plot(history.history['loss'])
plt.show()

print(model.predict([100.0]))
