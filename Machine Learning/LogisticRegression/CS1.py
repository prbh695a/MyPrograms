#1.We will use acoustic features to distinguish a male voice from female. Load the dataset from “voice.csv”,identify the target variable and do a one-hot encoding for the same. Split the dataset in train-test with 20% of the data kept aside for testing.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LogisticRegression/voice.csv")
from sklearn.preprocessing import OneHotEncoder
targetV=df[['label']]
ohe=OneHotEncoder()
ohe.fit(targetV)
targetV=ohe.transform(targetV)
#2.Fit a logistic regression model and measure the accuracy on the test set.
from sklearn.preprocessing import OneHotEncoder
X=df.iloc[:,1:20]
Y=df['label'].map({'male':1,'female':0})
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=85)

lm=LogisticRegression(max_iter=10000)
lm.fit(X_train,Y_train)
Y_pred_training= lm.predict(X_train)
Y_pred=lm.predict(X_test)

print("The training accuracy is",accuracy_score(Y_pred_training,Y_train))
print("The testing accuracy is",accuracy_score(Y_pred,Y_test))

#3.Compute the correlation matrix that describes the dependence between all predictors and identify the predictors that are highly correlated.  Plot the correlation matrix using seaborn heatmap.
import matplotlib.pyplot as plt
import seaborn as sns
corr=df.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corr,annot=True)
plt.yticks(rotation=0)
plt.show()
#4.Based on correlation remove those predictors that are correlated and fit a logistic regression model again and compare the accuracy with that of previous model.
reduceddf=df[['meanfreq', 'skew',
       'meanfun', 'minfun', 'maxfun',
       'mindom', 'modindx']]
X=reduceddf
Y=df['label'].map({'male':1,'female':0})
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=85)

lm=LogisticRegression(max_iter=10000)
lm.fit(X_train,Y_train)
Y_pred_training= lm.predict(X_train)
Y_pred=lm.predict(X_test)

print("The training accuracy is",accuracy_score(Y_pred_training,Y_train))
print("The testing accuracy is",accuracy_score(Y_pred,Y_test))
print("The accuracy increases about 2 percent, not much change")