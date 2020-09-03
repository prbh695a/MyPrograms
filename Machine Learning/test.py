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