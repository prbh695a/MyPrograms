#1.Let’s attempt to predict the survival of a horse based on various observed medical conditions. Load the data from ‘horses.csv’ and observe whether it contains missing values.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/horse.csv")
df.isnull()
#2.This dataset contains many categorical features, replace them with label encoding.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/horse.csv")
print(df.dtypes)
dummy=pd.get_dummies(df[['surgery', 'age','temp_of_extremities','peripheral_pulse',
                           'mucous_membrane','capillary_refill_time','pain','peristalsis',
                           'abdominal_distention','nasogastric_tube','nasogastric_reflux',
                           'rectal_exam_feces','abdomen','abdomo_appearance','surgical_lesion','cp_data']])
df=pd.concat([df,dummy],axis=1)

#3.Replace the missing values by the most frequent value in each column.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/horse.csv")

im=SimpleImputer(strategy='most_frequent')
im=im.fit(df)
df[:]=im.transform(df)
#4.Fit a decision tree classifier and observe the accuracy.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/DecisionTree/horse.csv")

im=SimpleImputer(strategy='most_frequent')
im=im.fit(df)
df[:]=im.transform(df)

dummy=pd.get_dummies(df[['surgery', 'age','temp_of_extremities','peripheral_pulse',
                           'mucous_membrane','capillary_refill_time','pain','peristalsis',
                           'abdominal_distention','nasogastric_tube','nasogastric_reflux',
                           'rectal_exam_feces','abdomen','abdomo_appearance','surgical_lesion','cp_data']])
df=pd.concat([df,dummy],axis=1)

df=df.drop(['surgery', 'age','temp_of_extremities','peripheral_pulse',
                           'mucous_membrane','capillary_refill_time','pain','peristalsis',
                           'abdominal_distention','nasogastric_tube','nasogastric_reflux',
                           'rectal_exam_feces','abdomen','abdomo_appearance','surgical_lesion','cp_data'],axis=1)

df.outcome=pd.Categorical(df.outcome)
df['outcome']=df.outcome.cat.codes

x=df.drop(['outcome'],axis=1)
y=df['outcome']

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.2,random_state=81)
dt=tree.DecisionTreeClassifier()
dt.fit(X_train,Y_train)
Y_pred=dt.predict(X_test)
Y_pred_train=dt.predict(X_train)

print("The training accuracy score is: ",accuracy_score(Y_train,Y_pred_train))
print("The test accuracy score is: ",accuracy_score(Y_test,Y_pred))
#5.Fit a random forest classifier and observe the accuracy.
rf=RandomForestClassifier()
rf.fit(X_train,Y_train)
Y_pred=rf.predict(X_test)
Y_pred_train=rf.predict(X_train)

print("The training accuracy score is: ",accuracy_score(Y_train,Y_pred_train))
print("The test accuracy score is: ",accuracy_score(Y_test,Y_pred))
