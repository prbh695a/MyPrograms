import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/CrossValidationAndBoosting/Diabetes.txt",
              header=None,sep=',')
df.columns=['nPreg','conc','dbp','ts','si','bmi','dpf','age','class']
X=df[['nPreg','conc','dbp','ts','si','bmi','dpf','age']]
Y=df['class']
kfold=model_selection.KFold(n_splits=10,random_state=7)
adaBoost=AdaBoostClassifier(n_estimators=30,random_state=7)
result=model_selection.cross_val_score(adaBoost,X,Y,cv=kfold)
print(result.mean())