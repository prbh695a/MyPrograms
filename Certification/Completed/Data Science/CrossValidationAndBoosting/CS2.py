#1.Load the data from “glass.csv” and make a bar plot of different types of glasses.
import pandas as pd
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/CrossValidationAndBoosting/glass.csv")

X=df.drop(['Type'],axis=1)
Y=df['Type']
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(Y)

#2.Make a train_test split and fit a single decision tree classifier.
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)
sns.countplot(Y_train)
plt.show()
from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(X_train,Y_train)
Y_pred=dt.predict(X_test)
from sklearn.metrics import accuracy_score
print("The test accuracy score is:",accuracy_score(Y_pred,Y_test))

#3.Make a k-fold split with 3 splits and measure the accuracy score with each split
from sklearn.model_selection import cross_val_score
accuracy=cross_val_score(dt,X,Y,cv=3)
accuracy[0]
for i in range(0,3):
    print("For split {} the accuracy is: {}".format(i+1,accuracy[i]))

#4.Use gridSearchCV from sklearn for finding out a suitable number of estimators for a RandomForestClassifer alongwith a 10-fold cross validation.
from sklearn.ensemble import RandomForestClassifier
rt=RandomForestClassifier()
from sklearn.model_selection import GridSearchCV
param_grid = {
    'n_estimators': [200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
gs = GridSearchCV(estimator=rt, param_grid=param_grid, cv= 5)
gs.fit(X, Y)
print(gs.best_params_)
rt=RandomForestClassifier(criterion='entropy',max_depth=8,max_features='auto',n_estimators=200)
rt.fit(X_train,Y_train)
Y_pred=rt.predict(X_test)
from sklearn.metrics import accuracy_score
print("The test accuracy score is:",accuracy_score(Y_pred,Y_test))