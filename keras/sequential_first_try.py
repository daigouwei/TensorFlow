from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# 定义模型
if False: # 一种定义模型的写法
    model1 = Sequential([
        Dense(32, units=784),
        Activation('relu'),
        Dense(10),
        Activation('softmax'),
    ])

if False: # 一种定义模型的写法
    model2 = Sequential()
    model2.add(Dense(32, input_shape=(784, None)))
    model2.add(Activation('relu'))
    model2.add(Dense(10))
    model2.add(Activation('softmax'))

if True: # 一种定义模型的写法，个人更倾向于这种写法，简单明了分层更清晰
    model = Sequential()
    model.add(Dense(32, activation='rule', input_shape=(784, None)))
    model.add(Dense(10, activation='softmax'))

# 编译：指定损失函数loss 优化器optimizer 指标列表metrics
model.compile(
    optimizer='rmsprop',
    loss = 'categorical_crossentropy',
    metrics = ['accuracy']
)

# 训练
data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))
model.fit(data, labels, epochs=10, batch_size=32)
