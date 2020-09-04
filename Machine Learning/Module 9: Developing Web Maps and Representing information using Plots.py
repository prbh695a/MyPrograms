
#1.Create a pandas dataframe having following structure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'float_col': [.1, .2, .2, 10.1, None],
                   'int_col': [1, 2, 6, 8, -1],
                   'str_col': ['a', 'b', None, 'c', 'a']

                   })
print(df)

#2.filter  the  columns  'float_col',  'int_col'  from  the  dataframe  in  one  query.  Hint-use  ix method of dataframes. Also print without using ix method
print(df[['float_col','int_col']])

#3.filter the records from float_col having value greater than 0.15 and in separate query filter float_col value equal to 0.1
print(df[df['float_col'] > .15])
print(df[df['float_col'] == .1])

#4.filter  the  records  from data  framewhich  satisfies  both  the  conditions  float_col greater than 0.1 and int_col greater than 2
print(df[(df['float_col']>.1) & (df['int_col'] > 2)])

#5.filter  the  records  from  data  frame  which  satisfies  both  the  conditions  float_col greater than 0.1 or int_colgreater than 2
print(df[(df['float_col']>.1) | (df['int_col'] > 2)])

#6.filter the records from data frame which satisfies the conditions float_col not greater than 0.1
print(df[~(df['float_col']>.1)])

#7.Create a new data frame in which column int_col is renamed to new_name.
ndf=df.rename(columns={'int_col':'new_name'})
print(ndf)

#8.Modify the existing dataframe and rename the column int_col to new_name
df.rename(columns={'int_col':'new_name'}, inplace=True)
print(df)

#9.Drop the rows where any value is missing from the dataframe
print(df.dropna())

#10.Change the missing value in column float_col as mean value of the float_col
meanVal=df['float_col'].mean()
df['float_col']=df['float_col'].fillna(meanVal)
print(df)
#11.change  all  the  values  of  str_col  with  new  valueand  drop  the  missing  values.  New value should have prefixmap_ and original value. Eg map_a, map_b
x=df['str_col'].dropna()
print(x.map(lambda x:"map_"+x))

#12.group  all  the  values  of  str_col  and  find  the  mean  of  float_col  in  all  the  groups respectively
m=df.groupby('str_col')
print(m['float_col'].mean())

#13.find the covariance of float_col and int_col
print(df.cov())
#14.find the correlation of float_col and int_col
print(df.corr())
#15.Create a data frame ‘other’ having columns some_val and str_col having values given below
ndf = pd.DataFrame({'some_val': [1, 2],
                    'str_col': ['a', 'b']

                    })
print(df.merge(ndf, how='inner'))
print(df.merge(ndf, how='outer'))
print(df.merge(ndf, how='left'))
print(df.merge(ndf, how='right'))

#16.When we want to send the same invitations to many people, the body of the mail does not change. Only the name (and maybe address) needs to be changed.
f = open("names.txt", "w")
f.write("Anil\nsunita\nsuman\nlokesh\nSumita\nJohn\nJohny")
f.close()

f = open("body.txt", "w")
f.write("I am going to Delhi.\nLets meet on 7th Jan 2018\nHave a great day\nRegards\nTeam Victory\n")
f.close()

f = open("names.txt", "r")
b = open("body.txt", "r")
body = b.read()
for i in f.read().split("\n"):
    print(i)
    f = open(i + ".txt", "w")
    f.write("Hello " + i + ",\n")
    f.write(body)
    f.close()
