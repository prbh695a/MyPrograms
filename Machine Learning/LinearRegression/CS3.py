#1.Compute --Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.  Is there a correlation?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/FyntraCustomerData.csv")

import seaborn as sns
reduceddf=df[['Time_on_Website','Yearly_Amount_Spent']]
correlation=reduceddf.corr()
sns.heatmap(correlation,cmap="YlGnBu",annot=True)
plt.yticks(rotation=0)
plt.show()
print("The correlation is negative 0.0026, hence there is no correlation between these and are independent variables")
#2.Compute –Do the same as above but now with Time on App and Yearly Amount Spent. Is this correlation stronger than 1stOne?
import seaborn as sns
reduceddf=df[['Time_on_App','Yearly_Amount_Spent']]
correlation=reduceddf.corr()
sns.heatmap(correlation,cmap="YlGnBu",annot=True)
plt.yticks(rotation=0)
plt.show()
print("The correlation is 0.5, hence there is better correlation between these variables as compare to 1st one")
#3.Compute --Explore types of relationships across the entire data set using pairplot . Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
sns.set(style='ticks')
sns.pairplot(df)
plt.show()
print("The most correlated feature with Yearly Amount Spent is (order descending) Length_of_Membership=>Time_on_App=>Avg_Session_Length=>Time_on_Website")
#4.Compute –Create linear model plot of Length of Membership and Yearly Amount Spent. Does the data fits well in linear plot?
x=df['Length_of_Membership']
y=df['Yearly_Amount_Spent']
plt.plot(x,y,'o')
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)
plt.xlabel("Length_of_Membership")
plt.ylabel("Yearly_Amount_Spent")
plt.show()
print("The data is almost near the line indicating near linear relationship")
#5.Compute –Train and Test the data and answer multiple questions --What is the use of random_state=85?
x=df[['Length_of_Membership','Time_on_Website','Avg_Session_Length','Time_on_App']]
y=df['Yearly_Amount_Spent']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=85)
print("The random state is used as pseudoo random generator to generate the same model again and again and decide shuffling extent")
#6.Compute –Predict the data and do a scatter plot. Check if actual and predicted data match?
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,Y_train)
Y_pred=lm.predict(X_test)

plt.scatter(Y_test,Y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()
print("They almost match")

#7.What is the value of Root Mean Squared Error?
from sklearn.metrics import mean_squared_error
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print("The value of Root Mean Squared Error is :",rmse)
abse=np.mean(np.abs(Y_test-Y_pred)/Y_test)
accuracy=(1-abse)
print("The accuracy of the model is ",accuracy*100)
#8.Final Question –Based on coefficients interpret company should focus more on their mobile app or on their website
cdf=pd.DataFrame(data=lm.coef_,columns=['Coefficient'] ,index = X_train.columns)
print(cdf)
print("The coefficient for Time_on_App is 39.066821 and for Time_on_Website is 0.682530.")
print("This mean Time_on_App increases the Yearly_Amount_Spent by almost 39.066821 units.")
print("Hence company should focus more on their mobile app.")