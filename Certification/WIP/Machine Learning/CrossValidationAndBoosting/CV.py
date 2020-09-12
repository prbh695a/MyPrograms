import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/CrossValidationAndBoosting/mtcars_for_manymerge.csv")

X=df[['cyl','hp']]
Y=df['Feedback']
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
knnc=KNeighborsClassifier(n_neighbors=4)
from sklearn.model_selection import cross_val_score
print(cross_val_score(knnc,X,Y,cv=10,scoring='accuracy').mean())

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
from sklearn.model_selection import cross_val_score
print(cross_val_score(lr,X,Y,cv=10,scoring='accuracy').mean())

from sklearn.ensemble import AdaBoostClassifier
abc=AdaBoostClassifier()
print(cross_val_score(abc,X,Y,cv=10,scoring='accuracy').mean())

'''
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
lr=LogisticRegression(max_iter=10000)
dt=DecisionTreeClassifier()
rf=RandomForestClassifier()
nv=GaussianNB()
svc=SVC()
ad=AdaBoostClassifier()
print("LogisticRegression",cross_val_score(lr,X,Y,cv=10,scoring='accuracy').mean())
print("DecisionTreeClassifier",cross_val_score(dt,X,Y,cv=10,scoring='accuracy').mean())
print("RandomForestClassifier",cross_val_score(rf,X,Y,cv=10,scoring='accuracy').mean())
print("GaussianNB",cross_val_score(nv,X,Y,cv=10,scoring='accuracy').mean())
print("SVC",cross_val_score(svc,X,Y,cv=10,scoring='accuracy').mean())
print("AdaBoostClassifier",cross_val_score(ad,X,Y,cv=10,scoring='accuracy').mean())'''