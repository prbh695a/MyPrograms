import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pData=pd.read_csv("pacific.csv")
pData['Status'].unique()
pData['Status'].value_counts()
pData.drop()['Status'==' SS']
rowIndex=pData[(pData.Status==' SS')|(pData.Status==' ST')|(pData.Status==' PT')|(pData.Status==' SD')|(pData.Status==' HU ')].index
newpData=pData.drop(rowIndex,axis=0)
newpData['Status'].value_counts()

Y=newpData['Status']
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
l.fit_transform(Y)
X=newpData[['Maximum Wind', 'Minimum Pressure', 'Low Wind NE','Low Wind SE', 'Low Wind SW', 'Low Wind NW', 'Moderate Wind NE','Moderate Wind SE', 'Moderate Wind SW', 'Moderate Wind NW','High Wind NE', 'High Wind SE', 'High Wind SW', 'High Wind NW']]

corr=X.corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
plt.show()


X=newpData[['Maximum Wind', 'Minimum Pressure', 'Low Wind NE']]

corr=X.corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
plt.show()

X=newpData[['Maximum Wind', 'Minimum Pressure']]

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
ld=LinearDiscriminantAnalysis(n_components=2)
X_lda=ld.fit_transform(X_scaled,Y)

corr=X.corr()
plt.figure(figsize=(14,14))
sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
plt.show()
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)

from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
ld=LinearDiscriminantAnalysis(n_components=1)
X_lda=ld.fit_transform(X,Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_lda,Y,test_size=.2,random_state=42)

from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))


from sklearn.svm import SVC
s=SVC()
s.fit(X_train,Y_train)

Y_pred=s.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))