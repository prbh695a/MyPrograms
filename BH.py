import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
bData=pd.read_csv("BostonHousing.csv")
#print(bData.columns)

X=bData[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax','ptratio', 'b', 'lstat']]
Y=bData[['medv']]
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.2,random_state=42)

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,Y_train)
Y_pred=lm.predict(X_test)

from sklearn.metrics import mean_squared_error
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
#print(rmse)
abse=np.mean(np.abs(Y_test-Y_pred)/Y_test)
accuracy=1-abse
print(accuracy)
plt.scatter(Y_test,Y_pred)
plt.xlabel('Y_test')
plt.ylabel('Y_pred')
plt.show()

