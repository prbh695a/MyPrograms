import pandas as pd
df=pd.read_excel("/Users/prateekb/Downloads/MyPrograms/Certification/WIP/Machine Learning/Recommendation/Online_Retail.xlsx")
df=df.drop(['StockCode','InvoiceDate'],axis=1)
df.head()

pd.set_option('display.max_row', 10000)
pd.Series(df['Description'].unique())

df['Description']=df['Description'].astype(str)
df['Description']=df['Description'].map(lambda x : x.strip('?'))
df['Description']=df['Description'].map(lambda x : x.strip(' '))

df['InvoiceNo']=df['InvoiceNo'].astype(str)
df['InvoiceNo']=df[~df['InvoiceNo'].str.contains('C')]

df_France=df[df['Country']=='France']
df_France_gb=df_France.groupby(['InvoiceNo','Description'])['Quantity'].sum().unstack().fillna(0)


def encode_units(x):
    if x <= 0:
        return 0
    else:
        return 1


df_France_gb = df_France_gb.applymap(encode_units)

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
frequentItems=apriori(df_France_gb,min_support=0.1,use_colnames=True)

rules=association_rules(frequentItems,metric='confidence',min_threshold=.95)
rules[rules['lift']>1]