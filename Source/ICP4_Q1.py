import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

iris= pd.read_csv('iris.csv')

print(iris.head()) #it automatically shows some top 5 rows of the dataset
print(iris.shape) #it tells us there are 5 coloumns and 150 rows
print(iris['class'].unique()) # this result give all the unique class name
print(iris.describe())


# dividing the dataset into training nad testing part
X=iris.drop('class', axis=1) # X represents all the attributes from data except class attribute in data
y= iris['class']

X_train, X_test, y_train, y_test= train_test_split(X,y,test_size= 0.3)
# to train the data
from sklearn.svm import SVC
Guassian= GaussianNB()  # we have use gaussian bayes theorm
Guassian.fit(X_train,y_train)
# to prdict the data
y_pred=Guassian.predict(X_test)
# Evaluating and algorithm
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

print("Accuracy : %0.2f:" ,accuracy_score(y_test,y_pred)) # finding accuracy score


