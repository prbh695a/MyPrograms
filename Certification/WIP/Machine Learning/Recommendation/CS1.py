import pandas as pd
import numpy as np
dfBook=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Recommendation/BX-Books.csv"
                   ,encoding='latin-1')
dfRating=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Recommendation/BX-Book-Ratings.csv",
                    encoding='latin-1')
dfRating.drop_duplicates()
dfRating=dfRating.head(10000)
dfRating=dfRating[dfRating['isbn'].str.isdigit()]
dfRating['isbn']=dfRating['isbn'].astype('int')

newMap=pd.Series(sorted(dfRating['user_id'].unique())).to_dict()

bookrating=dfRating.pivot(index='user_id',columns='isbn',values='rating').fillna(-999999)
from sklearn.metrics import pairwise_distances
#from scipy.spatial.distance import cosine,correlation
dsim= pairwise_distances(bookrating.values,metric='cosine')
sim=1-dsim
np.fill_diagonal(sim,0)
user_simdf=pd.DataFrame(sim)
sUser=pd.DataFrame(user_simdf.idxmax(axis=1),columns=['U1'])
sUser['dummyUID']=pd.DataFrame({'dummyUID':genRange()})
sUser['User1']=sUser['dummyUID'].map(newMap)
sUser['User2']=sUser['U1'].map(newMap)
sUser=sUser.drop(['U1','dummyUID'],axis=1)

findId=14
print("We are finding recommendation for user id",findId)
print("The recommendation for this user is book with title...")
similarUser=sUser[sUser['User1']==findId]['User2'].values[0]
recommend=dfRating[dfRating['user_id']==similarUser]
for i,j in recommend['isbn'].iteritems():
    #print(j)
    book=dfBook[dfBook['isbn']==str(j)]
    for k,l in book['book_title'].iteritems():
        print(l)
