#1.We shall use the same dataset used in previous assignment -digits.Make a 80-20 train/test split.
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
digits=load_digits()

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

X=digits.data
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=42)
#2.Using scikit learn perform a LDA on the dataset. Find out the number of components in the projected subspace.
print("The number of components before LDA:",X_train.shape[1])

lda=LinearDiscriminantAnalysis()
lda.fit(X_train,Y_train)
X_train=lda.transform(X_train)
X_test=lda.transform(X_test)
print("The number of components after LDA:",X_train.shape[1])
#3.Transform the dataset and fit a logistic regression and observe the accuracy. Compare it with the previous model based on PCA in terms of accuracy and model complexity.
lr=LogisticRegression(max_iter=10000)
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)
Y_pred_training=lr.predict(X_train)

print("The training accuracy is: ",accuracy_score(Y_pred_training,Y_train))
print("The test accuracy is: ",accuracy_score(Y_pred,Y_test))
print("For this model the accuracy with PCA is slightly better than LDA")
