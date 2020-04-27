import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/Hurricanes.csv')
print(df.head())
x=df['Year']
y=df['Hurricanes']
plt.bar(x,y)
plt.xlabel("Year")
plt.ylabel("Hurricanes")
plt.show()

df = pd.read_csv('/Users/prateekb/Downloads/Dataset/CityTemps.csv',delimiter=',')
print(df.head())
plt.hist(df['San Francisco'])
plt.hist(df['Moscow'])
plt.xlabel("Temperatures")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/CityTemps.csv')
print(df.head())
plt.hist(df["San Francisco"])
plt.xlabel("Temperatures")
plt.show()
plt.hist(df["Moscow"])
plt.xlabel("Temperatures")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/Cars2015.csv')
#drop the column which are not require.
df = df.drop(['Model','Type','LowPrice','HighPrice','Drive','CityMPG','HwyMPG','FuelCap','Length'], axis=1)
df = df.drop(['Width','Wheelbase','Height','UTurn','Weight','Acc030','Acc060'],axis=1)
df = df.drop(['QtrMile','PageNum','Size'],axis=1)
#based on make count the number of models
df['count'] = df.groupby('Make')['Make'].transform('count')
df.drop_duplicates('Make',inplace=True)
df.sort_values(by='count',ascending=False,inplace=True)
#Based on the count obtain we will plot our graph.
plt.figure(figsize=(50,8))
ax1 = plt.subplot(121, aspect='equal')
df.plot(kind='pie', y = 'count', ax=ax1, autopct='%1.1f%%',startangle=90, shadow=False, labels=df['Make'], legend = False, fontsize=10)
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/BigMartSalesData.csv')
#drop the column which are not require.
print(df.head())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/BigMartSalesData.csv')
#drop the column which are not require.
#print(df)
year2011=df[(df['Year']== 2011)]
#print (year2011)
sales_2011_month = year2011.groupby('Month').sum()['Amount']
print(sales_2011_month.min())

plt.plot(sales_2011_month.index,sales_2011_month.values)
plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.show()

plt.bar(sales_2011_month.index,sales_2011_month.values,color="red") # Change the color and play
plt.xlabel("Sales in Euro")
plt.ylabel("Month Number")
plt.title("Sales Per Month in Year 2011")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/BigMartSalesData.csv')
#drop the column which are not require.
#print(df)
year2011=df[(df['Year']== 2011)]
#print (year2011)
sales_2011_month = year2011.groupby('Month').sum()['Amount']
print(sales_2011_month.min())

sales_country_wise = year2011.groupby('Country').sum()['Amount']
plt.title("Country Wise Contribution For 2011")
plt.pie(sales_country_wise.values,labels=sales_country_wise.index,autopct='%1.1f%%')
plt.show()# Answer: UK --83.5 %# Enhancement --Play With Parameters  shadow=True, startangle=90 etc in plt.pie and see how different the chart looks# Assignment 4: Plot Scatter Plot for the invoice amounts and see the concentration of amount# In which range most of the invoice amounts are concentrated ?sales_invoice_wise = sales_2011.groupby('InvoiceNo').sum()['Amount']print(sales_invoice_wise)plt.scatter(sales_invoice_wise.values,sales_invoice_wise.values)plt.grid(True)

sales_invoice_wise = year2011.groupby('InvoiceNo').sum()['Amount']
print(sales_invoice_wise)
plt.scatter(sales_invoice_wise.values,sales_invoice_wise.values)
plt.grid(True)
plt.show()