# For a single-input model with 2 classes (binary classification):
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

import numpy as np
data = np.random.random((1000, 100)) # 随机生成1000*100的值为0-1的矩阵
labels = np.random.randint(2, size=(1000, 1)) # 随机生成小于2的正整数1000*1的矩阵

model.fit(data, labels, epochs=10, batch_size=1)
