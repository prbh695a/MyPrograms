import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
def topN(column,N=""):
    colNumpy = column.dropna().to_numpy()
    unique, counts = np.unique(colNumpy, return_counts=True)
    totalcol = dict(zip(unique, counts))
    # print(totaltwp)
    sortedtotalcol = sorted(totalcol.items(), key=lambda x: x[1], reverse=True)
    # print(sortedtwp)
    #print("Top {} with values".format(N))
    keylist = []
    valuelist = []

    for key, value in sortedtotalcol[:N]:
        print("{} and its count {}".format(key, value))
        keylist.append(key)
        valuelist.append(value)
    return keylist,valuelist

df = pd.read_csv('/Users/prateekb/Downloads/Dataset/911.csv',delimiter=',')
#Question1
print("\nTop 10 ZipCodes")
elist,_=topN(df['zip'],10)
if (19446 and 19090) in elist:
    print("19446 and 19090 exist in top 10")
else:
    print("19446 and 19090 doesnt exist in top 10")

#Question2
print("\nTop 4 Township")
elist,_=topN(df['twp'],4)
for i in ["LOWER POTTSGROVE", "NORRISTOWN", "HORSHAM", "ABINGTON"]:
    if i not in elist:
        print("{} doesnt exist in top 4 twp".format(i))

#Question3
print("\nTop 2 Reasons")
df['reason']=df['title'].str.extract(r"(.*):")
elist,_=topN(df['reason'],2)

#Question4
keylist,valuelist=topN(df['reason'],3)
plt.bar(keylist,valuelist)
plt.show()
print("Horizontal bar chart")
plt.barh(keylist,valuelist)
plt.show()

#Question5
days = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
df['timeStamp'] = df['timeStamp'].dropna()
df['date']=pd.to_datetime(df['timeStamp'])
df['day']= df['date'].dt.dayofweek.apply(lambda x: days[x])
reason = df.groupby(['reason','day'])['day'].count()
max=reason[reason==reason.values.max()]
stre=str(max.index[0]).replace(')',"").split(",")
print("\nThe day with maximum call for EMS is {} with value {}".format(stre[1].strip(" "),reason.values.max()))

#Question6
plt.figure(figsize=(12,8))
ax = sns.countplot(x="day", hue="reason", data=df)
print("Traffic calls were lowest on Sunday")

#Question7
df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
plt.figure(figsize=(12,8))
ax = sns.countplot(x="month", hue="reason", data=df)
for p in ax.patches:
    ax.annotate('{:.2f}'.format(p.get_height()), (p.get_x()+0.15, p.get_height()+1))
print("June has the highest number of firecalls with 3773")

#Question8
#displaying first 100 to save time
subdf=df[(df['reason'] == "Traffic")]
map=folium.Map(location=[subdf['lat'].mean(),subdf['lng'].mean()],zoom_start=6)
i=0
for row in subdf.iterrows():
    prop = str(row[1]['reason'])
    lat = row[1]['lat']
    lon = row[1]['lng']
    folium.Marker(location=[lat, lon], marker_color='red', popup=prop).add_to(map)
    i=i+1
    if(i==100):
        break

map.save("map.html")
print("Map done")
