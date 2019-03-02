import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('train.csv')

print(train.SalePrice.describe())

#Next, we'll check for skewness
print ("Skew is:", train.SalePrice.skew())
plt.hist(train.SalePrice, color='blue')
plt.show()
# normal distribution
target = np.log(train.SalePrice)
print ("Skew is:", target.skew())
plt.hist(target, color='blue')
plt.show()
# To plot Gaurage area vs Sales Price
var='GarageArea'
data= pd.concat([train['GarageArea'],train['SalePrice']], axis=1)
data.plot.scatter(x=var,y='SalePrice')
plt.show()

#outliers
GarageData=pd.concat([train['GarageArea']],axis=1, keys=['GaragData'])
train=train.drop((GarageData[GarageData['GaragData']<100]).index)
train=train.drop((GarageData[GarageData['GaragData']>1200]).index)

var='GarageArea'
data= pd.concat([train['GarageArea'],train['SalePrice']], axis=1)
data.plot.scatter(x=var,y='SalePrice')
plt.show()




