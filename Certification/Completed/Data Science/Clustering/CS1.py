import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Clustering/driver-data.csv")
clustering_data=df[['mean_dist_day','mean_over_speed_perc']]

from sklearn.preprocessing import StandardScaler
s=StandardScaler()
s.fit(clustering_data)
clustering_data=s.transform(clustering_data)

withinClusterDistance = []
for cluster in range(1, 10):
    kmeans = KMeans(n_clusters=cluster)
    kmeans.fit(clustering_data)
    withinClusterDistance.append(kmeans.inertia_)

plt.figure(figsize=(8, 8))
plt.plot(range(1, 10), withinClusterDistance)
plt.xlabel("No of clusters")
plt.ylabel("Interia")
plt.show()

from sklearn.metrics import silhouette_samples, silhouette_score

silhouetteScore = []
for cluster in range(2, 10):
    kmeans = KMeans(n_clusters=cluster)
    kmeans.fit(clustering_data)
    silhouetteScore.append(silhouette_score(clustering_data, kmeans.labels_))
    print("Cluster = {}, silhouetteScore= {}".format(cluster, silhouette_score(clustering_data, kmeans.labels_)))

plt.figure(figsize=(8, 8))
plt.plot(range(2, 10), silhouetteScore)
plt.xlabel("No of clusters")
plt.ylabel("silhouetteScore")
plt.show()

kmeans=KMeans(n_clusters=4,n_init=300)
kmeans.fit(clustering_data)
plt.scatter(clustering_data[:,0],clustering_data[:,1],c=kmeans.labels_)
plt.xlabel("mean_dist_day")
plt.ylabel("mean_over_speed_perc")
plt.show()