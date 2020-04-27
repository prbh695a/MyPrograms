import pandas as pd
import numpy as np
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/HollywoodMovies.csv')
questmovie=df[(df['Story']=="Quest")]
#print(questmovie)
movie=questmovie[(questmovie['RottenTomatoes']==questmovie['RottenTomatoes'].max())]
data=movie[0:1]
print(data['Movie'].values,data['RottenTomatoes'].values)

import pandas as pd
import numpy as np
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/HollywoodMovies.csv')
print(df.columns)
questmovie=df.groupby('Genre').count()
print (questmovie.index)
print (questmovie.size)
max=0
for key,value in questmovie.iterrows():
    print(key,value)

import pandas as pd
import numpy as np
df = pd.read_csv('/Users/prateekb/Downloads/Dataset/911.csv')
zipcode=df
df.drop(columns=['lat','lng','desc','title','timeStamp','twp','addr','e'])
print("---------------------")
print(df.head())