import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/pacific.csv")

df.Status=pd.Categorical(df.Status)
df['Status']=df.Status.cat.codes

sns.countplot(df['Status'],label='count')
plt.show()

df=df.drop(['ID','Name','Event','Latitude','Longitude'],axis=1)

x=df[['Date', 'Time', 'Maximum Wind', 'Minimum Pressure',
       'Low Wind NE', 'Low Wind SE', 'Low Wind SW', 'Low Wind NW',
       'Moderate Wind NE', 'Moderate Wind SE', 'Moderate Wind SW',
       'Moderate Wind NW', 'High Wind NE', 'High Wind SE', 'High Wind SW',
       'High Wind NW']]
y=df['Status']

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.2,random_state=43)
tc=tree.DecisionTreeClassifier()
tc.fit(X_train,Y_train)
Y_pred=tc.predict(X_test)
Y_pred_train=tc.predict(X_train)

print("The train accuracy of the model is ",accuracy_score(Y_train,Y_pred_train))
print("The test accuracy of the model is ",accuracy_score(Y_test,Y_pred))


rf=RandomForestClassifier(n_estimators=100)
rf.fit(X_train,Y_train)
Y_pred=rf.predict(X_test)
Y_pred_train=rf.predict(X_train)

print("The train accuracy of the model is ",accuracy_score(Y_train,Y_pred_train))
print("The test accuracy of the model is ",accuracy_score(Y_test,Y_pred))