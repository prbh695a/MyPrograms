import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
mData=pd.read_csv("movie_metadata1.csv")
mData.head()
clusteringmData=mData[['num_critic_for_reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_1_facebook_likes', 'gross', 'num_voted_users', 'cast_total_facebook_likes', 'facenumber_in_poster','num_user_for_reviews', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']]

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
clusteringData=sc.fit_transform(clusteringmData)
pd.DataFrame(clusteringData,columns=clusteringmData.columns).head()

from sklearn.cluster import KMeans
within_cluster_distance=[]
for i in range(1,15):
    kTempObj=KMeans(n_clusters=i,max_iter=300,init="k-means++",n_init=15)
    kTempObj.fit(clusteringData)
    within_cluster_distance.append(kTempObj.inertia_)

plt.plot(range(1,15),within_cluster_distance)
plt.title("Elbow Method")
plt.xlabel("No of clusters")
plt.ylabel("Within Cluster Distance")

from sklearn.metrics import silhouette_samples,silhouette_score
all_silhoutte_score=[]
for i in range(2,15):
    kTempObj=KMeans(n_clusters=i,max_iter=300,init="k-means++",n_init=15)
    kTempObj.fit(clusteringData)
    all_silhoutte_score.append(silhouette_score(clusteringData,kTempObj.labels_)

plt.plot(range(2,15),all_silhoutte_score)
plt.title("Elbow Method")
plt.xlabel("No of clusters")
plt.ylabel("Within Cluster Distance")



from sklearn.cluster import KMeans
kobject=KMeans(n_clusters=10,max_iter=300,init="k-means++",n_init=15)
kobject.fit(clusteringmData)

kobject.cluster_centers_
kobject.labels_
kobject.inertia_
plt.scatter(clusteringData[0][:,0],clusteringData[0][:,1],c=kobject.labels_)



