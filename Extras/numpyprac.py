import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm
#L=[1,2,3]
#A=np.array([1,2,3])

#print (A)
#print (A+A)
#print (np.sqrt(A))
#print (A**2)
#print (np.log(A))
#print (np.exp(A))
#print (np.ones((10,10)))
#print (np.random.random((10,10)))
#G=np.random.rand(10,10)

#print (G.mean())
#print (G.var())

#A=np.array([[1,1],[1.5,4]])
#B=np.array([2200,5050])
#C=np.linalg.solve(A,B)
#print (C)
#x=pd.read_csv("data_2d.csv",header=None)
#print (type(x))
#print (x.info())
#print (x.head())

#print (x[0])
#print (x.iloc[0])
#print (x[x[0] < 5])
#x=pd.read_csv("international-airline-passengers.csv",engine="python",skipfooter=3)
#print (x.columns)
#x.columns=["month","passengers"]
#print (x.columns)
#print (x.passengers)
#x['ones']=1
#print (x.head())

#datetime.strptime("1949-05","%Y-%m")
#x['dt']=x.apply(lambda row:datetime.strptime(row['month'],"%Y-%m"),axis=1)
#print (x.info())

#x=np.linspace(0,10,100)
#y=np.sin(x)
#plt.plot(x,y)
#plt.xlabel("Time")
#plt.ylabel("Some Function of time")
#plt.title("My Plot")
#plt.show()

#A= pd.read_csv('data_1d.csv', header=None).values
#x = A[:,0]
#y = A[:,1]
#plt.scatter(x,y)
#plt.show()

#x_line = np.linspace(0,100,100)
#y_line=2*x_line+1
#plt.scatter(x,y)
#plt.plot(x_line,y_line)
#plt.show()
#plt.hist(x)
#plt.show()
#y_actual = 2*x +1
#residuals = y -y_actual
#plt.hist(residuals)
#plt.show()

#df=pd.read_csv("train.csv")
#print (df.shape)
#M=df.values
#im=M[0,1:]
#print(im.shape)
#im=im.reshape(28,28)
#print(im.shape)
#plt.imshow(im,cmap='gray')
#plt.show()

#print(norm.pdf(0))
#print(norm.pdf(0,loc=5,scale=10))

#r=np.random.rand(10)
#print (norm.pdf(r))
#print (norm.logpdf(r))
#print (norm.cdf(r))
#print (norm.logcdf(r))

#r=np.random.randn(10000)
#plt.hist(r,bins=100)

#r=10*np.random.randn(10000)+5
#plt.hist(r,bins=100)
#plt.show()

r = np.random.randn(10000,2)
#plt.scatter(r[:,0],r[:,1])
#plt.show()

#r = np.random.randn(10000,2)
r[:,1]=5*r[:,1]+2
plt.scatter(r[:,0],r[:,1])
plt.axis('equal')
plt.show()