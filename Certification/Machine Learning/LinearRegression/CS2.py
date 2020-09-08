#1.Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/cereal.csv")
print(df.head())
plt.hist(df['sugars'], bins='auto',alpha=0.7, rwidth=0.85,label="Sugar")
plt.xlabel("Sugar")
plt.ylabel("Cereal")
plt.legend(loc='best')
plt.show()

plt.hist(df['vitamins'], bins='auto',alpha=0.7, rwidth=0.85,label="Vitamins")
plt.xlabel("Vitamins")
plt.ylabel("Cereal")
plt.legend(loc='best')
plt.show()

plt.hist(df['sugars'], bins='auto',alpha=0.7, rwidth=0.85,label="Sugar")
plt.hist(df['vitamins'], bins='auto',alpha=0.7, rwidth=0.85,label="Vitamins")
plt.ylabel("Cereal")
plt.legend(loc='best')
plt.show()
#2. The names of the manufactures are coded using alphabets, create a new column with their fullname using the below mapping.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/cereal.csv")
print(df.head())
import seaborn as sns
plt.figure(figsize=(12,4))
sns.countplot(x ='mfr', data = df)
plt.show()

#3. Extract the rating as your target variable ‘y’ and all numerical parameters as your predictors ‘x’. Separate 25% of your data as test set.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/cereal.csv")
print(df.head())
x=df.iloc[:,4:15]
y=df['rating']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=.25,random_state=5)

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,Y_train)
Y_pred=lm.predict(X_test)

plt.scatter(Y_test,Y_pred)
plt.show()
#4. Fit a linear regression module and measure the mean squared error on test dataset.
from sklearn.metrics import mean_squared_error
print("The mean squared error is: ",mean_squared_error(Y_pred,Y_test))
rmse=np.sqrt(mean_squared_error(Y_pred,Y_test))
print("The root mean square error is: ",rmse)
abse=np.mean(np.abs((Y_pred-Y_test)/Y_test))
accuracy=1-abse
print("The accuracy with current model is: ",accuracy*100)