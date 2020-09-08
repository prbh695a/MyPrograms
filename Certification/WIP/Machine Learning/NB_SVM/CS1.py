import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/NB_SVM/voice-classification.csv")
df.label=pd.Categorical(df.label)
df['label']=df.label.cat.codes

X=df.iloc[:,0:20]
Y=df['label']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)
Y_pred_train=nb.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

corr=X.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corr,annot=True)
plt.show()

X=X.drop(['centroid','median','kurt','skew'],axis=1)
Y=df['label']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)
Y_pred_train=nb.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))