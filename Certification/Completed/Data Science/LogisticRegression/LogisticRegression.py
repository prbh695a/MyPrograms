import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/LogisticRegression/data.csv')
df=df.drop(['Unnamed: 32','id'],axis=1)
df['diagnosis']=df['diagnosis'].map({'M':'1','B':'0'})

corr=df.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corr,annot=True)
plt.show()

x=df.iloc[:,1:31]
y=df['diagnosis']

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.2,random_state=43)

lr=LogisticRegression(max_iter=10000)
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

print(accuracy_score(Y_test,Y_pred))

