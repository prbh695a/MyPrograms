import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/BostonHousing.csv")

x=df.iloc[:,0:13]
y=df.iloc[:,13:14]

import seaborn as sns
correlation=df.corr()
plt.figure(figsize=(10,10))

sns.heatmap(correlation,cmap="YlGnBu",annot=True)
plt.yticks(rotation=0)
plt.xticks(rotation=0)
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.2)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,Y_train)
Y_pred=lm.predict(X_test)

plt.scatter(Y_test,Y_pred)
plt.show()

from sklearn.metrics import mean_squared_error
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
abse=np.mean(np.abs(Y_test-Y_pred)/Y_test)
accuracy=(1-abse)
print((accuracy[0])*100)