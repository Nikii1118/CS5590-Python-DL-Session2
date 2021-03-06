from keras import Sequential
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.utils import to_categorical

(train_images,train_labels),(test_images, test_labels) = mnist.load_data()
#display the first image in the training data
plt.imshow(train_images[0,:,:],cmap='gray')
plt.title('Ground Truth : {}'.format(train_labels[0]))
plt.show()

#process the data
#1. convert each image of shape 28*28 to 784 dimensional which will be fed to the network as a single feature
dimData = np.prod(train_images.shape[1:])
train_data = train_images.reshape(train_images.shape[0],dimData)
test_data = test_images.reshape(test_images.shape[0],dimData)

#convert data to float and scale values between 0 and 1
train_data = train_data.astype('float')
test_data = test_data.astype('float')
#scale data
train_data /=255.0
test_data /=255.0
#change the labels frominteger to one-hot encoding
train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

#creating network
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimData,)))
model.add(Dense(512, activation='relu'))
model.add(Dense(10, activation='softmax'))
#first, we save our training model and then I am loading it again.
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
#history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=20, verbose=1,
                  # validation_data=(test_data, test_labels_one_hot))

model.load_weights("mnist-model.h5")
#model.save("mnist-model.h5")
# I am taking random image from my test data at 130 and them I am predicting the image by reshaping it.
img =test_images[130]
print(img)
test_img= img.reshape((1,784))
img_class=model.predict_classes(test_img)
print(img_class)
prediction = img_class[0]
classname=img_class[0]
print("Class:",classname)
img=img.reshape((28,28))
plt.imshow(img)
plt.title(classname)
plt.show()


#