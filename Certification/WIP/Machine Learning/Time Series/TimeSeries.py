import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Time Series/BOE-XUDLERD.csv")
df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')

plt.figure(figsize=(10,10))
plt.plot(df['Value'])

ts_month=df['Value'].resample('M').mean()
plt.figure(figsize=(10,10))
plt.plot(ts_month)

from statsmodels.tsa.stattools import adfuller
results=adfuller(ts_month)
print("The adfullee test result is:%f" % results[1])
#p>0.05 timeseries is nonStationary

diff=ts_month-ts_month.shift()
diff.dropna(inplace=True)
resultsD=adfuller(diff)

print("The adfullee test result is:%f" % resultsD[1])
#p<0.05 timeseries is Stationary

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(diff,lags=20)

from statsmodels.graphics.tsaplots import plot_pacf
plot_pacf(diff,lags=10)

trainSize=int(len(ts_month)*.95)
train_data,test_data=ts_month[0:trainSize],ts_month[trainSize:]

from statsmodels.tsa.arima_model import ARIMA
model=ARIMA(train_data,order=(1,1,1))
result=model.fit()

result.summary()

Y_pred=result.forecast(steps=26)[0]
np.sqrt(np.mean((Y_pred-test_data)**2))
np.mean(np.abs(test_data-Y_pred)/test_data)
test_datad=pd.DataFrame(test_data)
test_datad['PValue']=Y_pred
test_datad
plt.plot(test_datad['PValue'])
plt.plot(test_datad['Value'])