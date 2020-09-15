import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Certifications/OnlineNewsPopularity.csv")
pd.options.display.max_columns = None
#url and timedelta are metadata
df=df.drop(['url','timedelta'],axis=1)

X=df.drop(['shares'],axis=1)
Y=df[['shares']]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=85)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print(rmse)
print(r2_score(Y_test,Y_pred))

#To Dig further lets try to remove multicolinearity using pvalues/VIF
#First lets try VIF
print("Trying VIF")
from statsmodels.stats.outliers_influence import variance_inflation_factor
ndf=df.drop(['shares'],axis=1)
vif = pd.DataFrame()
vif["features"] = ndf.columns
vif["vif_Factor"] = [variance_inflation_factor(ndf.values, i) for i in range(ndf.shape[1])]
Z=vif[~(vif['vif_Factor']>5)]

#Let try to see if we remove columns through VIF we get any improvement
X=df[Z['features']]
Y=df[['shares']]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=85)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print(rmse)
print(r2_score(Y_test,Y_pred))

#Lets try StandardScaler
print("After Standard Scaler")
from sklearn.preprocessing import StandardScaler
ss=MinMaxScaler()
ss.fit(X_train)
X_train=ss.transform(X_train)
X_test=ss.transform(X_test)

lr=LinearRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print(rmse)
print(r2_score(Y_test,Y_pred))


#Let try with pvalues now
print("Trying with pvalues")
X=df.drop(['shares'],axis=1)
Y=df[['shares']]

import statsmodels.api as sm
C=X
ncolumns=[]
C=sm.add_constant(C)
model=sm.OLS(df[['shares']],C).fit()
for i,j in model.pvalues.iteritems():
    if(j<.05): #If j>.05 we reject null hypothesis
        #print (i)
        ncolumns.append(i)
#print(ncolumns)

X=df[ncolumns]
Y=df[['shares']]

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=.20,random_state=85)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print(rmse)
print(r2_score(Y_test,Y_pred))

#lets try Standard scaler here
print("After Standard Scaler")
from sklearn.preprocessing import StandardScaler
ss=MinMaxScaler()
ss.fit(X_train)
X_train=ss.transform(X_train)
X_test=ss.transform(X_test)

lr=LinearRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import r2_score
rmse=np.sqrt(mean_squared_error(Y_test,Y_pred))
print(rmse)
print(r2_score(Y_test,Y_pred))
print("This means with current information it is tough to predict number of shares exactly")