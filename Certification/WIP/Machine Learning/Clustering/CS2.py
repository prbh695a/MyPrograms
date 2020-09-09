#1.Open and display the image “dog.jpeg”. Convert the image in to numpy array,so that i can be   used in further processing.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from PIL import Image
from numpy import asarray
image=Image.open("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Clustering/dogs.jpeg")
data=asarray(image)

plt.figure(figsize = (8,8))
plt.imshow(image)
plt.show()
#2. Find out the dimensions of the image and convert it in to a two-dimensional array.
data2D=np.float32(data.reshape(-1,3))
print(data.shape)

#3.Use kmeans clustering with k set to 3 and cluster the image
from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=3)
kmeans.fit(data2D)

#4. Predict the cluster label of every pixel in the image and plot it back as an image.
center=kmeans.cluster_centers_
center = np.uint8(center)
label=kmeans.labels_
segImage=(center[label]).reshape(data.shape)
plt.figure(figsize=(8,8))
plt.imshow(segImage)
plt.show()
#5. Find out the three dominant color in the image.
print("The three dominant color in format [R,G,B] are \n",center)

#