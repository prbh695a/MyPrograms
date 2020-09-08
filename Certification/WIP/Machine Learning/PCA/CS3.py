import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/PCA/breast-cancer-data.csv")
df['diagnosis']=df['diagnosis'].map({'M':1,'B':0})
df=df.drop(['id'],axis=1)

X=df.iloc[:,1:31]
Y=df['diagnosis']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print("*********************With LogisticRegression*********************")
def lr():
    lr=LogisticRegression(max_iter=10000)
    lr.fit(X_train,Y_train)
    Y_pred=lr.predict(X_test)
    Y_pred_train=lr.predict(X_train)
    from sklearn.metrics import accuracy_score
    print("The train accuracy score is: ",accuracy_score(Y_train,Y_pred_train))
    print("The test accuracy score is: ",accuracy_score(Y_test,Y_pred))

lr()

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(X_train)
X_train_s=ss.transform(X_train)
X_test_s=ss.transform(X_test)


from sklearn.decomposition import PCA
print("*********************With PCA+LogisticRegression*********************")
print("The number of components before PCA:",X_train.shape[1])
pca=PCA(.95)
pca.fit(X_train_s)
X_train=pca.transform(X_train_s)
X_test=pca.transform(X_test_s)
print("The number of components after PCA:",X_train.shape[1])
lr()

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
print("*********************With LDA+LogisticRegression*********************")
print("The number of components before LDA:",X_train.shape[1])
lda=LinearDiscriminantAnalysis()
lda.fit(X_train_s,Y_train)
X_train=lda.transform(X_train_s)
X_test=lda.transform(X_test_s)
print("The number of components after LDA:",X_train.shape[1])

lr()
print("==============================================================================")
print("The best accuracy model is given by PCA with test accuracy of 98.24 percent")
print("==============================================================================")
