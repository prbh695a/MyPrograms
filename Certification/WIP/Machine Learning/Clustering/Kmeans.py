import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Clustering/movie_metadata1.csv")
clustering_data=df[['movie_facebook_likes','director_facebook_likes']]
from sklearn.preprocessing import StandardScaler
s=StandardScaler()
s.fit(clustering_data)
clustering_data=s.transform(clustering_data)

withinClusterDistance = []
for cluster in range(1,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(clustering_data)
    withinClusterDistance.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
plt.figure(figsize=(12,6))
plt.plot(range(1,20), withinClusterDistance, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

from sklearn.metrics import silhouette_samples,silhouette_score
silhouette_score(clustering_data,kmeans.labels_)
silhoutte_scores = []
for cluster in range(2,20):
    kmeans = KMeans(n_jobs = -1, n_clusters = cluster, init='k-means++')
    kmeans.fit(clustering_data)
    silhoutte_scores.append(silhouette_score(clustering_data,kmeans.labels_))

kmeans=KMeans(n_clusters=2,n_init=15,max_iter=300,init='k-means++')
kmeans.fit(clustering_data)
plt.scatter(df['movie_facebook_likes'],df['director_facebook_likes'],c=kmeans.labels_)