<<<<<<< HEAD
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/SalaryGender.csv')
print (df.head())
salary=np.array(df['Salary'])
gender=np.array(df['Gender'])
age=np.array(df['Age'])
phd=np.array(df['PhD'])

filtermen=df[(df['Gender']==1) & (df['PhD']==1)]
numberofmen=np.array(np.array(filtermen['Gender']))
print(numberofmen.size)
filterwmen=df[(df['Gender']==0) & (df['PhD']==1)]
numberofwmen=np.array(np.array(filterwmen['Gender']))
print(numberofwmen.size)

df=df[(df['PhD'])==1]
df=df.drop(columns=['Salary','Gender'])
print(df.head())

phd=df[(df['PhD']==1)]
#print(phd)
phdArray=np.array(phd['PhD'])
print(phdArray.size)


a=[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
b=[]
y=0
count=0
while(y!=10):
    for i in a:
        if y == i:
            count=count+1
    b.append(count)
    count=0
    y=y+1
print(b)


a=np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])
comp = a > 5
b=a[a>5]
print(b)

a = np.array([np.nan,   1.,   2.,  np.nan,   3.,   4.,   5.])
b=~np.isnan(a)
print(a[b])

import numpy as np
a=np.random.random([10,10])
print(a.max())
print(a.min())

a=np.random.random([30])
print(a.size)
print(a.mean())

import numpy as np
a=np.arange(0,10)
print(np.where(a <= 2, a, a*-1))

df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
print(df.describe())
print(df.groupby(['school_rating']).mean())

df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
#print(df.head())
df=df[['reduced_lunch', 'school_rating']]
print(df.corr())

df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
xvalues=df['reduced_lunch']
print(xvalues)
yvalues=df['school_rating']
print(yvalues)
plt.xlabel("reduced lunch")
plt.ylabel("school's rating")
plt.scatter(xvalues,yvalues)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
plt.figure(figsize=(14,8)) # set the size of the graph
_ = sns.regplot(data=df, x='reduced_lunch', y='school_rating')
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
xvalues=df['reduced_lunch']
#print(xvalues)
yvalues=df['school_rating']
#print(yvalues)
plt.xlabel("reduced lunch")
plt.ylabel("school's rating")
plt.scatter(xvalues,yvalues)

z = np.polyfit(xvalues, yvalues, 1)
p = np.poly1d(z)
plt.plot(xvalues,p(xvalues),"r--")

plt.show()


corr = df.corr()
_, ax = plt.subplots(figsize=(13,10))# graph correlation matrix
_ = sns.heatmap(corr, ax=ax, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()
=======
import numpy as np
import pandas as pd
salaryData=pd.read_csv("SalaryGender.csv")
salary=np.array(salaryData['Salary'])
gender=np.array(salaryData['Gender'])
age=np.array(salaryData['Age'])
phd=np.array(salaryData['PhD'])

salaryData.groupby('Gender').agg({'PhD':'sum'})


new=salaryData[['Age','PhD']]
print(new)
actualdf=new[new['PhD']!=0]
print(actualdf)

phds=salaryData.groupby('PhD').agg({'PhD':'sum'})
totalphds=phds[phds['PhD']==1]
print(totalphds)
>>>>>>> ffe6d83ed825025415b416cb6ad47ba86f6d2321
