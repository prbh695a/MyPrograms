#1.Extract data from the givenCSV file and store the data from each column in a separate NumPy array
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/SalaryGender.csv')
print (df.head())
salary=np.array(df['Salary'])
gender=np.array(df['Gender'])
age=np.array(df['Age'])
phd=np.array(df['PhD'])

#2.Find:1. The number of men with a PhD2. The number of women with a PhD
filtermen=df[(df['Gender']==1) & (df['PhD']==1)]
numberofmen=np.array(np.array(filtermen['Gender']))
print(numberofmen.size)
filterwmen=df[(df['Gender']==0) & (df['PhD']==1)]
numberofwmen=np.array(np.array(filterwmen['Gender']))
print(numberofwmen.size)

#3.Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD
df=df[(df['PhD'])==1]
df=df.drop(columns=['Salary','Gender'])
print(df.head())

#4.Calculate the total number of people who have a PhD degree
phd=df[(df['PhD']==1)]
#print(phd)
phdArray=np.array(phd['PhD'])
print(phdArray.size)

#5.How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of Integers?
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

#6.Create  a  numpy  array  [[0,    1,    2],[  3,    4,    5],[  6,    7,    8],[  9,  10,  11]])  and  filter  the elements greater than 5.
a=np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])
comp = a > 5
b=a[a>5]
print(b)

#7.Create a numpy array having NaN (Not a Number) and print it.
a = np.array([np.nan,   1.,   2.,  np.nan,   3.,   4.,   5.])
print(a)
b=~np.isnan(a)
print(a[b])

#8.Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values
import numpy as np
a=np.random.random([10,10])
print(a.max())
print(a.min())

#9.Create a random vector of size 30 and find the mean value.
a=np.random.random([30])
print(a.size)
print(a.mean())

#10.Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
import numpy as np
a=np.arange(0,11)
print(np.where((a>1) & (a<=9), a*-1,a))

#11.Create a random array of 3 rows and 3 columns and sort it according to 1stcolumn, 2ndcolumn or 3rdcolumn.
a=np.random.rand(3,3)
print("before sorting\n",a)
a=a[a[:,0].argsort()] #0 column
print("sorting column1\n",a)
a=a[a[:,1].argsort()] #0 column
print("sorting column2\n",a)
a=a[a[:,2].argsort()] #0 column
print("sorting column3\n",a)

#12.Create a four dimensions array get sum over the last two axis at once.

#13.Create a random array and swap two rows of an array.
a=np.random.randint(0,10,(2,2))
print("before swapping\n",a)
a[[0,1]]=a[[1,0]]
print("after swapping\n",a)

#14.Create a random matrix and Compute a matrix rank.
import numpy as np
from numpy.linalg import matrix_rank

matrix=np.random.randint(0,10,(5,5))
print("Matrix\n",matrix)
print("rank of a matrix is :",matrix_rank(matrix))

#15.
#Phase 1 -Data Collection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
print(df.describe())

#Phase 2 -Group data by school ratings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print(df.groupby(['school_rating']).mean())

#Phase 3 –Correlation analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
#print(df.head())
df=df[['reduced_lunch', 'school_rating']]
print(df.corr())

#Phase 4 –Scatter Plot
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

#Phase 5 –Correlation Matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/middle_tn_schools.csv')
corr = df.corr()
_, ax = plt.subplots(figsize=(13,10))# graph correlation matrix
_ = sns.heatmap(corr, ax=ax, xticklabels=corr.columns.values, yticklabels=corr.columns.values)
plt.show()

#============================================================================================
#Case Study II
#1.Read the three csv files which contains the score of same students in term1 for each Subject
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dfMaths = pd.read_csv('/Users/prateekb/Downloads/Dataset/MathScoreTerm1.csv')
dfDS = pd.read_csv('/Users/prateekb/Downloads/Dataset/DSScoreTerm1.csv')
dfPhysics = pd.read_csv('/Users/prateekb/Downloads/Dataset/PhysicsScoreTerm1.csv')

#2.Remove the name and ethnicity column (to ensure confidentiality)
dfMaths=dfMaths.drop(columns=['Name','Ethinicity'])
dfDS=dfDS.drop(columns=['Name','Ethinicity'])
dfPhysics=dfPhysics.drop(columns=['Name','Ethinicity'])

#3.Fill missing score data with zero
dfMaths['Score']=dfMaths['Score'].fillna(0)
dfDS['Score']=dfDS['Score'].fillna(0)
dfPhysics['Score']=dfPhysics['Score'].fillna(0)

#4.Merge the three files
frames = [dfMaths, dfDS, dfPhysics]
temp = pd.merge(dfMaths,dfDS,on=['ID','Age','Sex'],how='outer')
result = pd.merge(temp,dfPhysics,on=['ID','Age','Sex'],how='outer')

#5.Change Sex(M/F) Columnto 1/2 for further analysis
result['Sex'].replace(['F','M'],[0,1],inplace=True)

#6.Store the data in new file –ScoreFinal.csv
result.to_csv('ScoreFinal.csv',index=False)