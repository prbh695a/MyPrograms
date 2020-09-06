import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
oData=pd.read_excel("Online_Retail.xlsx")
#print(oData.head())
oData['Description']=oData['Description'].astype(str)
oData['Description']=oData['Description'].map(lambda x:x.strip(' '))
oData['Description']=oData['Description'].map(lambda x:x.strip('?'))

oData['InvoiceNo']=oData['InvoiceNo'].astype(str)
oData=oData[~oData['InvoiceNo'].str.contains('C')]

oData_France=oData[oData['Country']=='France']
oData_France_groupby=oData_France.groupby(['InvoiceNo','Description'])['Quantity'].sum().unstack().fillna(0)
def encode_units(x):
    if x<=0:
        return 0
    else:
        return 1
oData_France_groupby=oData_France_groupby.applymap(encode_units)

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
oData_France_groupby.drop(['POSTAGE'],inplace=True,axis=1)
frequent_itemset=apriori(oData_France_groupby,min_support=.1,use_colnames=True)

rules=association_rules(frequent_itemset,metric='confidence',min_threshold=.9)
print(rules)
rules=rules[rules['lift']>1]
print(rules)
