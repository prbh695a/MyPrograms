

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Case Study I
#1.Find the highest rated movie in the“Quest” story type.
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/HollywoodMovies.csv')
qMovie=df[(df['Story']== 'Quest')]
qMovie=qMovie[qMovie['RottenTomatoes']==qMovie['RottenTomatoes'].max()]
x=qMovie[qMovie['AudienceScore']==qMovie['AudienceScore'].max()]
for i,j in x['Movie'].iteritems():
    print("The highest rated movie in the Quest=story type is = ",j)

#2.Find the genre in which there has been the greatest number of movie releases.
hn=df.groupby('Genre').count()
m=hn[hn['Movie']==hn['Movie'].max()]
m=m['Movie']
for i,j in m.iteritems():
    print("The genere with highest number of release is {} with {}".format(i,j))

#3.Print the names of the top five movies with the costliest budgets.
b=df.nlargest(5,'Budget')
count=0
for i,j in b['Movie'].iteritems():
    count = count+1
    for k,l in b['Budget'].iteritems():
        if i==k:
            print("The {} is \"{}\" with budget of {}".format(count,j,l))

#4.Is there any correspondence between the critics’ evaluation of a movie and itsacceptance by the public? Find out, by plotting the net profitability of a movie against the ratings it receives on Rotten Tomatoes.
plt.scatter(df['Profitability'],df['RottenTomatoes'])
plt.xlim(0,500)
plt.show()

#5.Perform Operations on Files
#5.1: From the raw data below create a data frame
df=pd.DataFrame({
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 'age': [42, 52, 36, 24, 73], 'preTestScore': [4, 24, 31, ".", "."],'postTestScore': ["25,000", "94,000", 57, 62, 70]
})
#5.2: Save the dataframe into a csv file as example.csv
df.to_csv('example.csv',index=False)
#5.3: Read the example.csv and print the data frame
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv')
print(df)
#5.4: Read the example.csv without column heading
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv',header=None)
print(df)
#5.5: Read the example.csv andmake the index columns as 'First Name’ and 'Last Name'
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv',index_col=['First Name', 'Last Name']
               ,names=['First Name', 'Last Name','Age', 'Pre-Test Score', 'Post-Test Score'])
print(df)

#5.6:  Print  the  data  frame  in  a  Boolean  form  as  True  or  False.  True  for  Null/  NaN values and false for non-nullvalues
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv',na_values=["."])
print(df.notnull())

#5.7: Read the dataframe by skipping first 3 rows and print the data frame
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv',skiprows=3)
print(df)

#5.8: Comma should be ignored while reading the data. It is default behaviour,but you need to give argument to read_csv function which makes sure commas are ignored.
df=pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/example.csv',thousands=',')
print(df)

#6.1: From the raw data below create a Pandas Series
#a) Print all elements in lower case
import pandas as pd
import numpy as np
s=pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.lower())
#b) Print all the elements in upper case
print(s.str.upper())
#c) Print the length of all the elements
print(s.str.len())

#6.2: From the raw data below create a Pandas Series
#a) Print all elements after stripping spaces from the left and right
import pandas as pd
import numpy as np
s=pd.Series([' Atul','John ',' jack ','Sam'])
print(s.str.strip())
#b) Print all the elements after removing spaces from the left only
print(s.str.rstrip())
#c) Print all the elements after removing spaces from the right only
print(s.str.lstrip())

#6.3: -Create a series from the raw data below
# a)split the individual strings wherever ‘_’ comes and create a list out of it.
import pandas as pd
import numpy as np
s=pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
l=s.str.split('_')
print(l)
# b)Access the individual element of a list
print(l[0],l[1],l[2],l[3])
# c)Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements
l=s.str.split('_',expand=True)
print(l)

#6.4: Create a series and replace either X or dog with XX-XX'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
import pandas as pd
import numpy as np
s=pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
l=s.replace(regex=r'X|dog',value='XX-XX')
print(l)
#6.5: Create a series and remove dollar from the numeric values'12', '-$10', '$10,000'
import pandas as pd
import numpy as np
s=pd.Series(['12', '-$10', '$10,000'])
l=s.replace(regex=r'\$',value='')
print(l)
#6.6:-Create a series and reverse all lower case words'india 1998', 'big country', np.nan
import pandas as pd
import numpy as np
s=pd.Series(['india 1998', 'big country', np.nan])
replaceValue=lambda m:m.group(0)[::-1]
l=s.str.replace(r'[a-z]+',replaceValue)
print(l)
#6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.'1', '2', '1a', '2b', '2003c'
import pandas as pd
import numpy as np
s=pd.Series(['1', '2', '1a', '2b', '2003c'])
print(s.str.isalnum())
#6.8: Create pandas series and print true if value is containing ‘A’'1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c
import pandas as pd
import numpy as np
s=pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
print(s.str.contains('A'))
#6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values'a', 'a|b', np.nan, 'a|c'
import pandas as pd
import numpy as np
s=pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(s.str.get_dummies())
#6.10: Create pandas dataframe having keys and ltable and rtable as below -'key': ['One', 'Two'], 'ltable': [1, 2]'key': ['One', 'Two'], 'rtable': [4, 5]Merge both the tables based of key
import pandas as pd
import numpy as np
df1=pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
df2=pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})
mdf=pd.merge(df1,df2,on='key')
print(mdf)

#============================================================================================
#Case Study II

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/PythonPractice/Machine Learning/Salaries.csv')
#1.Compute how much total salary cost has increased from year 2011 to 2014
s2011=df[df['Year']==2011]
print(s2011['TotalPayBenefits'].sum())
s2014=df[df['Year']==2014]
print(s2014['TotalPayBenefits'].sum())
diff=(s2014['TotalPayBenefits'].sum())-(s2011['TotalPayBenefits'].sum())
print("The salary cost increases to {} from 2011 to 2014".format(diff))

#2.Which Job Title in Year 2014 has highest mean salary?
smean=df.groupby('JobTitle').mean()
hjt=smean[smean['TotalPayBenefits']==smean['TotalPayBenefits'].max()]
for i,j in hjt['TotalPayBenefits'].iteritems():
    print("The job title {} has the highest salary mean of {}".format(i,j))

#3.How much money could have been saved in Year 2014 by stopping OverTimePay?
s2014=df[df['Year']==2014]
print("The money saved by stopping overtime pay is {}".format(s2014['OvertimePay'].sum()))
#4.Which are the top 5 common job in Year 2014 and how much do they cost SFO ?
s2014=df[df['Year']==2014]
top5jobs=s2014['JobTitle'].value_counts().head(5)
topjobs=[]
for i,j in top5jobs.iteritems():
    topjobs.append(i)
totalSal=s2014.groupby('JobTitle').sum()
cost=0
for i,j in totalSal['TotalPayBenefits'].iteritems():
    if(i in topjobs):
        cost=cost+j
print("The cost for 5 common jobs in 2014 to SFO is = ",cost)
#5.Who was the top earning employee across all the years?
totalSal=df.groupby('EmployeeName').sum()
#print(totalSal.sort_values(by='TotalPayBenefits',ascending=False))
hjt=totalSal[totalSal['TotalPayBenefits']==totalSal['TotalPayBenefits'].max()]
for i,j in hjt['TotalPayBenefits'].iteritems():
    print("The highest salaried employee is {} with salary mean of {}".format(i,j))
