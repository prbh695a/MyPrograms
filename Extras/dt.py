import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cData=pd.read_csv("cancer.csv")
cData.drop('id',axis=1,inplace=True)
cData.drop('Unnamed: 32',axis=1,inplace=True)
cData['diagnosis']=cData['diagnosis'].map({'M':1,'B':0})

X=cData[['radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean','concave points_mean', 'symmetry_mean', 'fractal_dimension_mean','radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se','compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se','fractal_dimension_se', 'radius_worst', 'texture_worst','perimeter_worst', 'area_worst', 'smoothness_worst','compactness_worst', 'concavity_worst', 'concave points_worst','symmetry_worst', 'fractal_dimension_worst']]
Y=cData[['diagnosis']]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=101)

from sklearn.tree import DecisionTreeClassifier
d=DecisionTreeClassifier()
d.fit(X_train,Y_train)

#from sklearn.tree import export_graphviz
#export_graphviz(d,out_file='/Users/prateekb/Downloads/PythonDS/graph.dot',feature_names=X_train.columns)

Y_pred=d.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))