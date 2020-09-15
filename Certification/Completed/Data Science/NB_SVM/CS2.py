#1.Load the kinematics dataset as measured on mobile sensors from the file “run_or_walk.csv”. List out the columns in the dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.naive_bayes import GaussianNB
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/NB_SVM/run_or_walk.csv")
print(df.columns)

#2. Let the target variable ‘y’ be the activity and assign all the columns after it to ‘x’.
X=df.iloc[:,5:11]
Y=df['activity']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#3.Using Scikit-learn fit a Gaussian Naive Bayes model and observe the accuracy.Generate a classification report using scikitlearn.
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)
Y_pred_train=nb.predict(X_train)

print("The test classification report is: \n",classification_report(Y_pred,Y_test))
from sklearn.metrics import accuracy_score
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))
corr=X.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True)
plt.show()
#4.Repeat the model once using only the acceleration values as predictors and then using only the gyro values as predictors. Comment on the difference in accuracy between both the models.
X=df.iloc[:,5:8]
corr=X.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True)
plt.show()

Y=df['activity']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)
Y_pred_train=nb.predict(X_train)
print("The test classification report is: \n",classification_report(Y_pred,Y_test))
from sklearn.metrics import accuracy_score
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))


X=df.iloc[:,8:11]
corr=X.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,annot=True)
plt.show()
Y=df['activity']
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

nb=GaussianNB()
nb.fit(X_train,Y_train)
Y_pred=nb.predict(X_test)
Y_pred_train=nb.predict(X_train)
print("The test classification report is: \n",classification_report(Y_pred,Y_test))
from sklearn.metrics import accuracy_score
print("The test accuracy score is: ",accuracy_score(Y_pred,Y_test))

print("With only gyro we are getting accuracy of 65.34% and with only acceleration we get accuracy of 95.89%")
print("This could be because NB is based on assumption no correlation between independent variables")
print("gyro seems to be dependent variable")