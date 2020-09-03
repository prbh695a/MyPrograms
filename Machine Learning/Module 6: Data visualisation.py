import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Case Study I
#1.You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring in the United States along the coast of the Atlantic. Load the data from the dataset into your program and plot a Bar Graph of the data, takingthe Year as the x-axis and the number of hurricanes occurring as the Y-axis.
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/Hurricanes.csv')
x=df['Year']
y=df['Hurricanes']
plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("No of hurricanes")
plt.show()

#2.The dataset given, records data of city temperatures over the years 2014 and 2015. Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/CityTemps.csv',delimiter=',')
plt.hist(df['San Francisco'],color='orange')
plt.xlabel("Temperatures of San Francisco")
plt.show()

df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/CityTemps.csv',delimiter=',')
plt.hist(df['Moscow'],color='green')
plt.xlabel("Temperatures of Moscow")
plt.show()

df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/CityTemps.csv',delimiter=',')
plt.hist(df["Moscow"],label='Moscow',color='green')
plt.hist(df["San Francisco"],label='San Francisco',color='orange')
plt.legend(loc='best')
plt.xlabel("Temperatures of both")
plt.show()

#3.Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide. Also mention the name of the manufacture with the largest releases.
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/Cars2015.csv')
df = df.drop(['Model','Type','LowPrice','HighPrice','Drive','CityMPG','HwyMPG','FuelCap','Length'], axis=1)
df = df.drop(['Width','Wheelbase','Height','UTurn','Weight','Acc030','Acc060'],axis=1)
df = df.drop(['QtrMile','PageNum','Size'],axis=1)
df['count'] = df.groupby('Make')['Make'].transform('count')
df.drop_duplicates('Make',inplace=True)
df.sort_values(by='count',ascending=False,inplace=True)
plt.figure(figsize=(50,50))
ax1 = plt.subplot(121, aspect='equal')
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d})".format(pct, absolute)
df.plot(kind='pie', y = 'count', ax=ax1,autopct = lambda pct: func(pct, df['count']),startangle=90, shadow=False, labels=df['Make'], legend = False, fontsize=10)
plt.show()

#4.Create csv file from the data below and read in pandas data frame
#Phase 1 -Reading Data
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/sample-salesv2.csv')

#Phase 2 –Describe the data
#Describe the data on the unit price
print(df['unit price'].describe())

#Phase 3 –filter the data
#Create new dataframe having columns 'name','net_price','date' and group all the records according to name
ndf=df[['name','net_price','date']]
ndfRes=ndf.groupby('name')

#Phase 4 –Plotting graph
#Plot the graph after calculating total sales by each customer. Customer name should be on x axis and total sales in y axis.
sales=ndfRes.sum()
sales.plot(kind='bar')
plt.show()

#5.Let the x axis data points and y axis data points are
#X = [1,2,3,4]
#y = [20, 21, 20.5, 20.8]
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
#5.1: Draw a Simple plot
plt.plot(X,Y)
plt.show()
#5.2: Configure the line and markers in simple plot
plt.plot(X,Y,'co-')
plt.show()
#5.3: configure the axes
plt.plot(X,Y,'co-')
plt.xticks(X)
plt.yticks(Y)
plt.show()
#5.4: Give title of Graph & labels of x axis and y axis
plt.plot(X,Y,'co-')
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Simple plot")
plt.xticks(X)
plt.yticks(Y)
plt.show()
#5.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(X,Y,yerr=y_error)
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Simple plot")
plt.xticks(X)
plt.yticks(Y)
plt.show()
#5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
plt.figure(figsize=(4, 5), dpi=100)
plt.errorbar(X,Y,yerr=y_error)
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Simple plot")
plt.xticks(X)
plt.yticks(Y)
plt.show()
#5.7: Give a font size of 14
plt.rc('font',size=14)
plt.errorbar(X,Y,yerr=y_error)
plt.xlabel("X-values")
plt.ylabel("Y-values")
plt.title("Simple plot")
plt.xticks(X)
plt.yticks(Y)
plt.show()
#5.8: Draw a scatter graph of any 50 random values of x and y axis
X = random.rand(50)
Y = random.rand(50)
plt.scatter(X,Y)
plt.show()
#5.9: Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
df=pd.DataFrame({'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
   'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]})
X=df['preTestScore']
Y=df['postTestScore']
plt.scatter(X,Y,s=df['age'])
plt.show()
#5.10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300 and the color determined by sex
df=pd.DataFrame({'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
   'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]})
X=df['preTestScore']
Y=df['postTestScore']
plt.scatter(X,Y,s=300,c=df['female'])
plt.show()

#============================================================================================
#Case Study II

#1.Plot Total Sales Per Month for Year 2011.  How the total sales has increased over months in Year 2011. Which month has lowest Sales?
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/BigMartSalesData.csv')
sales=df[(df['Year']== 2011)]
sales=df[(df['Year']== 2011)]
s2011=sales.groupby('Month')
s=s2011['Amount'].sum()
s.plot(kind='line')
plt.show()

#2.Plot Total Sales Per Month for Year 2011 as Bar Chart.  Is Bar Chart Better to visualize than Simple Plot
s.plot(kind='bar')
plt.show()

#3.Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales ?
c2011=sales.groupby('Country')
c=c2011['Amount'].sum()
plt.figure(figsize=(20,8))
c.plot(kind='pie', startangle=90)
plt.show()

#4.Plot Scatter Plot for the invoice amounts and see the concentration of amount. In which range most of the invoice amounts are concentrated
c2011=sales.groupby('InvoiceNo')
c=c2011['Amount'].sum()
print(c)
plt.scatter(x=c,y=c)
plt.show()