#1.The data file contains numerical attributes that describe a letter and its corresponding class. Read the datafile “letterCG.data” and set all the numerical attributes as features.Split the data in to train and test sets.
import pandas as pd
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/CrossValidationAndBoosting/letterCG.csv",
              sep=" ")
df=df.drop(['yegvx','Unnamed: 18'],axis=1)
X=df.drop(['Class'],axis=1)
Y=df[['Class']]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)
#2. Fit a sequence of AdaBoostClassifier with varying number of weak learners ranging from 1 to 16, keeping the max_depth as 1. Plot the accuracy on test set against the number of weak learners.Use decision tree classifier as the base classifier.
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
dt=DecisionTreeClassifier(max_depth=1)
weakLearner=[]
accuracy=[]
print("+++++++++++++++++++++Depth=1+++++++++++++++++++++")
for i in range(1,17):
    weakLearner.append(i)
    abc=AdaBoostClassifier(base_estimator=dt,n_estimators=i)
    abc.fit(X_train,Y_train.values.ravel())
    Y_pred=abc.predict(X_test)
    accuracy.append(accuracy_score(Y_pred,Y_test)*100)
    print("The accuracy score is with weaklerners {}: {}".format(i,accuracy_score(Y_pred,Y_test)))

import matplotlib.pyplot as plt
plt.scatter(weakLearner,accuracy)
plt.xlabel("Number of weak learners")
plt.ylabel("Test accuracy (in %)")
plt.show()
#3.Repeat step2 with max_depth set as 2
from sklearn.ensemble import AdaBoostClassifier
dt=DecisionTreeClassifier(max_depth=2)
weakLearner=[]
accuracy=[]
print("+++++++++++++++++++++Depth=2+++++++++++++++++++++")
for i in range(1,17):
    weakLearner.append(i)
    abc=AdaBoostClassifier(base_estimator=dt,n_estimators=i)
    abc.fit(X_train,Y_train.values.ravel())
    Y_pred=abc.predict(X_test)
    accuracy.append(accuracy_score(Y_pred,Y_test)*100)
    print("The accuracy score is with weaklerners {}: {}".format(i,accuracy_score(Y_pred,Y_test)))

import matplotlib.pyplot as plt
plt.scatter(weakLearner,accuracy)
plt.xlabel("Number of weak learners")
plt.ylabel("Test accuracy (in %)")
plt.show()

