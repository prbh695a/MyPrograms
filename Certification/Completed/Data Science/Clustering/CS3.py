#1.Load the file “zoo.data” and look at the info and first five rows. The first column denotes the animal name and the last one specifies a high-level class for the corresponding animal.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Clustering/zoo.csv")
print(df.head(5))

#2. Find out the unique number of high level class.
print(df['class_type'].unique())

#3. Use the 16-intermediate feature and perform an agglomerative clustering.
X=df.iloc[:,1:17]
import scipy.cluster.hierarchy as sch
dendro = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendrogram')
plt.xlabel('Animals')
plt.ylabel('Euclidean distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering
ac = AgglomerativeClustering(n_clusters = 7, affinity = 'euclidean', linkage = 'ward')
ac.fit(X)

#4. Compute the mean squared error by comparing the actual class and predicted high level class.
from sklearn.metrics import mean_squared_error,accuracy_score
print("The root mean square is :", mean_squared_error(df['class_type'], ac.labels_ , squared=False))
