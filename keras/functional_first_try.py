# 层对象接收张量为参数，返回一个张量
# 输入时张量，输出也是张量的一个框架就是一个模型，通过Model定义
# 这样的模型可以被像Keras的Sequential一样被训练

from keras.layers import Input, Dense
from keras.models import Model

inputs = Input(shape=(784, ))
x = Dense(64, activation='rule')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)
model = Model(inputs=inputs, outputs=predictions)

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(data, labels)