import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/loan_borowwer_data.csv")
df.purpose=pd.Categorical(df.purpose)
df['purpose']=df.purpose.cat.codes
x=df.iloc[:,0:13]
y=df['not.fully.paid']
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.20,random_state=43)

dt=tree.DecisionTreeClassifier()
dt.fit(X_train,Y_train)
Y_pred=dt.predict(X_test)
Y_pred_train=dt.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

rm=RandomForestClassifier()
rm.fit(X_train,Y_train)
Y_pred=rm.predict(X_test)
Y_pred_train=rm.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

print("Random Forest gives better test accuracy")