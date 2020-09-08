#1.Load the data from “college.csv” that has attributes collected about private and public colleges for a particular year. We will try to predict the private/public status of the college from other attributes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/NB_SVM/College.csv")

#2.Use LabelEncoder to encode the target variable in to numerical form and split the data such that 20% of the data is set aside fortesting.
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
le=LabelEncoder()
le.fit(df.Private)
df['Private']=le.transform(df.Private)
X=df.iloc[:,1:18]
Y=df['Private']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=85)

#3.Fit a linear svm from scikit learn and observe the accuracy.
s=SVC()
s.fit(X_train,Y_train)
Y_pred=s.predict(X_test)
Y_pred_train=s.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

#4.Preprocess the data using StandardScalar and fit the same model again and observe the change in accuracy
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(X_train)

X_train=ss.transform(X_train)
X_test=ss.transform(X_test)
s=SVC()
s.fit(X_train,Y_train)
Y_pred=s.predict(X_test)
Y_pred_train=s.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

print("\n The accuracy changed(increased) by almost 2 percent")

#5.Use scikit learn’s gridsearch to select the best hyperparameter for a non-linear SVM,identify the model with best score and its parameters.
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=85)
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(X_train)
X_train=ss.transform(X_train)
X_test=ss.transform(X_test)
from sklearn.model_selection import GridSearchCV
sv=SVC()
parameters=[{'C':[3.2],'kernel':['rbf']}]
g=GridSearchCV(estimator=sv,scoring='accuracy',param_grid=parameters)
g.fit(X_train,Y_train)
print(g.best_score_)
print(g.best_params_)
s=SVC(C=3.2)
s.fit(X_train,Y_train)
Y_pred=s.predict(X_test)
Y_pred_train=s.predict(X_train)

print("The train accuracy score is: ",accuracy_score(Y_pred_train,Y_train))
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))
