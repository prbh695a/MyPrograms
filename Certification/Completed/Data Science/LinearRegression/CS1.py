#1.Data Loading:
#a.Load the dataset “prisoners.csv” using pandas and display the first and last five rows in the dataset.
import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/prisoners.csv")
print("The first 5 rows")
print(df.head(5))
print("The last 5 rows")
print(df.tail(5))

#b.Use describe method in pandas and find out the number of columns. Can you say something about those rows who have zero inmates?
import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/prisoners.csv")
print(df.describe())
print("Total number of columns:",len(df.columns))

print(df.loc[(df['No. of Inmates benefitted by Elementary Education']==0) |
       (df['No. of Inmates benefitted by Adult Education']==0) |
       (df['No. of Inmates benefitted by Higher Education']==0) |
       (df['No. of Inmates benefitted by Computer Course']==0)])

#2.Data Manipulation:
# a.Create a new column -’total_benefitted’ that is a sum of inmates benefitted through all modes.
df['total_benefitted']=df.sum(axis=1)

#b.Create a new row -“totals” that is the sum of all inmates benefitted through each mode across all states.
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/prisoners.csv")
a=df['No. of Inmates benefitted by Elementary Education'].sum(axis=0)
b=df['No. of Inmates benefitted by Adult Education'].sum(axis=0)
c=df['No. of Inmates benefitted by Higher Education'].sum(axis=0)
d=df['No. of Inmates benefitted by Computer Course'].sum(axis=0)
e=df['total_benefitted'].sum(axis=0)
nrow={'STATE/UT':'total',
      'YEAR':2013,
      'No. of Inmates benefitted by Elementary Education':a,
      'No. of Inmates benefitted by Adult Education':b,
      'No. of Inmates benefitted by Higher Education':c,
      'No. of Inmates benefitted by Computer Course':d,
      'total_benefitted':e}
df = df.append(nrow, ignore_index=True)
print(df)

#Plotting
#a.Make a bar plot with each state name on the x -axis and their total benefitted inmates astheir bar heights. Which state has the maximum number of beneficiaries?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/prisoners.csv")
df['total_benefitted']=df.sum(axis=1)

x=df['STATE/UT']
y=df['total_benefitted']
plt.figure(figsize=(10,10))
plt.xticks(rotation=90)
plt.xlabel("States")
plt.ylabel("Total benefitted inmates")
plt.bar(x,y)
plt.show()

print("Andhra Pradesh has the the maximum number of beneficiaries")

#b.Make a pie chart that depicts the ratio among different modes of benefits.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/prateekb/Downloads/PythonPractice/Machine Learning/LinearRegression/prisoners.csv")
df['total_benefitted']=df.sum(axis=1)

a=df['No. of Inmates benefitted by Elementary Education'].sum(axis=0)
b=df['No. of Inmates benefitted by Adult Education'].sum(axis=0)
c=df['No. of Inmates benefitted by Higher Education'].sum(axis=0)
d=df['No. of Inmates benefitted by Computer Course'].sum(axis=0)
e=df['total_benefitted'].sum(axis=0)
nrow={'STATE/UT':'total',
      'YEAR':2013,
      'No. of Inmates benefitted by Elementary Education':a,
      'No. of Inmates benefitted by Adult Education':b,
      'No. of Inmates benefitted by Higher Education':c,
      'No. of Inmates benefitted by Computer Course':d,
      'total_benefitted':e}
df = df.append(nrow, ignore_index=True)
pieLabels=df.columns[2:6]
pieData=[a,b,c,d]
plt.figure(figsize=(8,8))
plt.pie(pieData,labels=pieLabels,autopct='%1.1f%%')
plt.show()