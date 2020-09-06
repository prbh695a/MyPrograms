import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cData=pd.read_csv("cancer.csv")
cData.drop(['Unnamed: 32'],axis=1,inplace=True)
cData.drop(['id'],axis=1,inplace=True)
cData['diagnosis']=cData['diagnosis'].map({'M':1,'B':0})
#corr=cData.corr()
#plt.figure(figsize=(14,14))
#sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
#plt.show()

#sns.boxplot(x='diagnosis',y='radius_mean',data=cData)


selectedColumns=['radius_mean','texture_worst','compactness_worst']
X=cData[selectedColumns]
Y=cData['diagnosis']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))



