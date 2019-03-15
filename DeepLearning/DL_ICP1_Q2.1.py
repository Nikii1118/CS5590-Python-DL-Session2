import pandas
from keras.models import Sequential
from keras.layers.core import Dense, Activation
#from sklearn.metrics import accuracy_score
# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
dataset = pd.read_csv("Breas Cancer.csv")
dataset["diagnosis"]= pd.Categorical(dataset["diagnosis"])
dataset["diagnosis"]=dataset["diagnosis"].cat.codes
dataset=dataset.values
# print(dataset)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(dataset[:,2:31], dataset[:,1],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(30, input_dim=29, activation='relu')) # hidden layer
my_first_nn.add(Dense(1, activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
#y_pred=my_first_nn.predict(X_test)
#print(y_pred)
#print(accuracy_score(y_pred,Y_test))
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
