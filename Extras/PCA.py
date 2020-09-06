import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
cData=pd.read_csv("cancer.csv")
cData.drop(['Unnamed: 32'],axis=1,inplace=True)
cData.drop(['id'],axis=1,inplace=True)
cData['diagnosis']=cData['diagnosis'].map({'M':1,'B':0})
#corr=cData.corr()
#plt.figure(figsize=(14,14))
#sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
#plt.show()

#sns.boxplot(x='diagnosis',y='radius_mean',data=cData)
indepVar=['radius_mean', 'texture_mean', 'perimeter_mean','area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean','concave points_mean', 'symmetry_mean', 'fractal_dimension_mean','radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se','compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se','fractal_dimension_se', 'radius_worst', 'texture_worst','perimeter_worst', 'area_worst', 'smoothness_worst','compactness_worst', 'concavity_worst', 'concave points_worst','symmetry_worst', 'fractal_dimension_worst']
X=cData.loc[:,indepVar].values

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_scaled=sc.fit_transform(X)

pd.DataFrame(X_scaled,columns=indepVar).head()

from sklearn.decomposition import PCA
pcaModel=PCA()
pcaC=pcaModel.fit_transform(X_scaled)
pcaModel.explained_variance_ratio_

plt.figure(figsize=(14,14))
df=pd.DataFrame({'Var':pcaModel.explained_variance_ratio_,
                 'PC':['PC1','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9','PC10',
                       'PC11','PC12','PC13','PC14','PC15','PC16','PC17','PC18','PC19','PC20',
                       'PC21','PC22','PC23','PC24','PC25','PC26','PC27','PC28','PC29','PC30']})
sns.barplot(x='PC',y='Var',data=df)


from sklearn.decomposition import PCA
pcaModel=PCA(n_components=4)
pcaC=pcaModel.fit_transform(X_scaled)
pcaModel.explained_variance_ratio_
XPC=pd.DataFrame(pcaC,columns=['PC1','PC2','PC3','PC4'])
corr=XPC.corr()
plt.figure(figsize=(6,6))
sns.heatmap(corr,annot=True,square=True,cmap='coolwarm')
plt.show()

Y=cData['diagnosis']
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(XPC,Y,test_size=.2,random_state=42)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
ld=LinearDiscriminantAnalysis()
X_lda=ld.fit_transform(X_scaled,Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X_lda,Y,test_size=.2,random_state=42)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(X_train,Y_train)
Y_pred=lr.predict(X_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,Y_pred)
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,Y_pred))