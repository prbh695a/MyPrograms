import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("/Users/prateekb/Downloads/PythonDS/BOE-XUDLERD.csv")
data['Date']=pd.to_datetime(data['Date'])
index=data.set_index('Date')
plt.figure(figsize=(15,8))
plt.plot(index['Value'])


plt.figure(figsize=(15,8))
month=index['Value'].resample('M').mean()
plt.plot(month)

from statsmodels.tsa.stattools import adfuller
result=adfuller(month)
print("pvalue %f",result[1])
monthDiff=month-month.shift()
monthDiff.dropna(inplace=True)
result2=adfuller(monthDiff)
print("pvalue %f",result)