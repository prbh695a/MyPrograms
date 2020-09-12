import pandas as pd
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/CrossValidationAndBoosting/bio-degradabale-data.csv",
              sep=';',header=None)
df.columns=['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',
'A11','A12','A13','A14','A15','A16','A17','A18','A19','A20',
'A21','A22','A23','A24','A25','A26','A27','A28','A29','A30',
'A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42']
df['A42'].unique()
df['A42']=df['A42'].map({'RB':1,'NRB':0})

X=df.iloc[:,0:41]
Y=df['A42']

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=30)

dt=DecisionTreeClassifier()
dt.fit(X_train,Y_train)
Y_pred=dt.predict(X_test)
print("The test accuracy with Decision Tree is:",accuracy_score(Y_pred,Y_test))

dt=DecisionTreeClassifier()
abc=AdaBoostClassifier(base_estimator=dt,n_estimators=30)
abc.fit(X_train,Y_train)
Y_pred=abc.predict(X_test)
print("The test accuracy after Boosting is:",accuracy_score(Y_pred,Y_test))