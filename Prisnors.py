import numpy as np
import pandas as pd
pData=pd.read_csv("prisoners.csv")
#print(pData.head())
#print(pData.tail())
#print(len(pData.columns))
desc=pData.describe()
#print(desc)
zero_indexes = pData.loc[pData['No. of Inmates benefitted by Elementary Education']==0]
print(zero_indexes)