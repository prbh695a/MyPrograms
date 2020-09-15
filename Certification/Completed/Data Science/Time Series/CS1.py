import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Time Series/SeaPlaneTravel.csv")
df.rename(columns={'#Passengers':'Passengers'},inplace=True)
df['Month']=pd.to_datetime(df['Month'])
df=df.set_index('Month')

#To plot we set index as month,year or week
plt.figure(figsize=(10,10))
plt.plot(df['Passengers'])

##Rolling Statistics - Plot the moving average
def rollingStatPlot(df):
    tsMean = df.rolling(12).mean()
    tsSd = df.rolling(12).std()
    plt.figure(figsize=(10, 10))
    plt.plot(df, color='blue', label='original')
    plt.plot(tsMean, color='red', label='tsMean')
    plt.plot(tsSd, color='green', label='tsSd')
    plt.legend('best')
    plt.show()

    from statsmodels.tsa.stattools import adfuller
    test = adfuller(df)
    print("The test result for Augmented Dickey Fuller is %f" % (test[1]))

##Rolling Statistics - Plot the moving average
#rollingStatPlot(df)

#Take log and again do the moving averge
tsLog=np.log(df)
#rollingStatPlot(tsLog)

#Moving average
movingAverage=tsLog.rolling(12).mean()
#plt.plot(tsLog)
#plt.plot(movingAverage)

#1.Transform between moving average and ts_log
logAndMA=tsLog-movingAverage
logAndMA.dropna(inplace=True)
#rollingStatPlot(logAndMA)

#2.Difference between logs (d=1)
diff=tsLog-tsLog.shift()
diff.dropna(inplace=True)
#rollingStatPlot(diff)

#find p and q
from statsmodels.graphics.tsaplots import acf,pacf

acfLag=acf(diff,nlags=20)
pacfLag=pacf(diff,nlags=20,method='ols')

plt.subplot(121)
plt.plot(acfLag)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(pacfLag)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(diff)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
plt.show()

#ARIMA Model
from statsmodels.tsa.arima_model import ARIMA
model=ARIMA(tsLog,order=(2,1,2))
result=model.fit(disp=-1)
plt.plot(diff)
plt.plot(result.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((result.fittedvalues-diff['Passengers'])**2))
plt.show()
#Prediction
predictions_ARIMA_diff = pd.Series(result.fittedvalues, copy=True)
print (predictions_ARIMA_diff.head())
predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print(predictions_ARIMA_diff_cumsum.head())

predictions_ARIMA_log = pd.Series(tsLog['Passengers'], index=tsLog.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
print(predictions_ARIMA_log.head())

##We took the log so need put it back
predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.plot(df['Passengers'])
plt.plot(predictions_ARIMA)
plt.show()

#10 years = 120 + 144
result.plot_predict(1,264)
plt.show()

