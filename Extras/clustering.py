import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
data=make_blobs(n_samples=500,n_features=4,centers=4,cluster_std=2,random_state=42)
plt.scatter(data[0][:,0],data[0][:,1],c=data[1])

from sklearn.cluster import KMeans
kobject=KMeans(n_clusters=3,max_iter=300,init="k-means++",n_init=15)
kobject.fit(data[0])

kobject.cluster_centers_
kobject.labels_
kobject.inertia_
plt.scatter(data[0][:,0],data[0][:,1],c=kobject.labels_)

within_cluster_distance=[]
for i in range(1,15):
    kTempObj=KMeans(n_clusters=i,max_iter=300,init="k-means++",n_init=15)
    kTempObj.fit(data[0])
    within_cluster_distance.append(kTempObj.inertia_)

plt.plot(range(1,15)within_cluster_distance)
plt.title("Elbow Method")
plt.xlabel("No of clusters")
plt.ylabel("Within Cluster Distance")


