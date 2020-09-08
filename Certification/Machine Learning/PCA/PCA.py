import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/PCA/trans_us.csv",index_col=0,thousands=',')
df.index.names=['Stations']
df.columns.names=['Months']
df=df.fillna(15)

pca=PCA(n_components=2)
pca.fit(df)
tdf=pca.transform(df)

ndf=pd.DataFrame(tdf)
ndf.index=df.index
ndf.columns=['PC1','PC2']

print(pca.explained_variance_ratio_)