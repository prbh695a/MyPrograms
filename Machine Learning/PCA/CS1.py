#1.Scikitlearn comes with pre-loaded dataset, load the digits dataset from that collection and write a helper function to plot the image using matplotlib
def displayImage(index):
    plt.gray()
    plt.imshow(digits.images[index])
    plt.show()

import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
digits=load_digits()
displayImage(0)

#2.Make a train -test split with 20% of the data set aside for testing. Fit a logistic regression model and observe the accuracy.
X=digits.data
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=42)
lr=LogisticRegression(max_iter=10000)
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)
Y_pred_training=lr.predict(X_train)

print("The training accuracy is: ",accuracy_score(Y_pred_training,Y_train))
print("The test accuracy is: ",accuracy_score(Y_pred,Y_test))
#3.Using scikitlearn perform a PCA transformation such that the transformed dataset can explain 95% of the variance in the original dataset. Find out the number of components in the projected subspace.
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
digits=load_digits()

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X=digits.data
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=42)

print("The number of components before PCA:",X_train.shape[1])

pca=PCA(.95)
pca.fit(X_train)
X_train=pca.transform(X_train)
X_test=pca.transform(X_test)
print("The number of components after PCA:",X_train.shape[1])


#4.Transform the dataset and fit a logistic regression and observe the accuracy. Compare it with the previous model andcomment on the accuracy.
lr=LogisticRegression(max_iter=10000)
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)
Y_pred_training=lr.predict(X_train)

print("The training accuracy is: ",accuracy_score(Y_pred_training,Y_train))
print("The test accuracy is: ",accuracy_score(Y_pred,Y_test))
print("For this model the accuracy is less for PCA by 2 percent")
#5.Compute the confusion matrix and count the number of instances that has gone wrong. For each of the wrong sample,plot the digit along with predicted and original label.
from sklearn.metrics import confusion_matrix
import seaborn as sns
plt.figure(figsize=(10,10))
cm = confusion_matrix(Y_test, Y_pred)
sns.heatmap(cm,annot=True)
plt.ylabel("Actual")
plt.xlabel("Prediction")
plt.show()


def displayImage(index, predIndex, testIndex):
    plt.figure(figsize=(2, 2))
    plt.gray()
    plt.imshow(digits.images[index])
    label = "Predicted=" + str(predIndex) + "     " + "Actual=" + str(testIndex)
    plt.xlabel(label)
    plt.show()


count = 1
for i in range(len(Y_pred)):
    if Y_pred[i] != Y_test[i]:
        count = count + 1
        displayImage(Y_pred[i], Y_pred[i], Y_test[i])

print("The total number of instances went wrong are: ", count)



