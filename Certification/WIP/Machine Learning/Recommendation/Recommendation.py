import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Recommendation/Recommend.csv",
              names=['UID','MID','Rating','Timestamp'])
df=df.drop(['Timestamp'],axis=1)
movies=df.pivot(index='UID',columns='MID',values='Rating').reset_index(drop=True)
movies=movies.fillna(0)
movies.shape

from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation

disSim=pairwise_distances(movies.values,metric='cosine')
user_sim=1-disSim

np.fill_diagonal(user_sim,0)
user_simdf=pd.DataFrame(user_sim)
user_simdf.idxmax(axis=1)

movie1=df[df['UID']==1]
movie915=df[df['UID']==916]
merged=pd.merge(movie1,movie915,on='MID',how='left')
movieSeenByUser1=merged[(merged['UID_y']!=916)]
movieSeenByUser1.sort_values(by='Rating_x',ascending=False)


import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Recommendation/Recommend.csv",
              names=['UID','MID','Rating','Timestamp'])
df=df.drop(['Timestamp'],axis=1)

movies=df.pivot(index='MID',columns='UID',values='Rating').reset_index(drop=True)
movies=movies.fillna(0)
movies
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation

disSim=pairwise_distances(movies.values,metric='correlation')
user_sim=1-disSim

np.fill_diagonal(user_sim,0)
user_simdf=pd.DataFrame(user_sim)
def genRange():
    MID=[]
    for i in range(1,1683):
        MID.append(i)
    return MID

mov= pd.DataFrame({'MID':genRange()})
mov['Similarity']=user_simdf.iloc[0]
mov.sort_values(by='Similarity',ascending=False)