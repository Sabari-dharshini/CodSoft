

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#load the iris flower dataset
df_flower=pd.read_csv('/content/IRIS.csv')
df_flower.head()

df_flower.isna().sum()

df_flower.shape

#DATA PREPROCESSING

df_flower.dropna(inplace=True)
df_flower.describe()

df_flower.info()

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df_flower['species']=le.fit_transform(df_flower['species'])
df_flower.head()

df_flower.info()

#VISUALIZING OUR DATASET

sns.histplot(x='species',data=df_flower,palette="set2")
plt.show()

sns.histplot(data=df_flower,x=df_flower.sepal_length,color='purple')

sns.histplot(data=df_flower,x=df_flower.sepal_width,color='red')

sns.histplot(data=df_flower,x=df_flower.petal_length,color='purple')

sns.histplot(data=df_flower,x=df_flower.petal_width,color='green')



#split the datset into features and labels
X=df_flower.drop('species',axis=1)
Y=df_flower['species']

#split the dataset into training and training sets
X_test,X_train,Y_test,Y_train=train_test_split(X,Y,test_size=0.2,random_state=42)

#Train a K-nearest neighbor clasifiers on training data
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train,Y_train)

df_flower.columns

#predict the species for the test data
y_pred=classifier.predict(X_test)

#Calculate the accuracy of the model
accuracy=accuracy_score(Y_test,y_pred)
print("Accuracy:",accuracy)
