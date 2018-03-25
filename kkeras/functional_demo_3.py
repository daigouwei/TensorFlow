# 卷积层的残差连接
import keras
from keras.layers import Conv2D, Input

# input tensor foe a 3-channel 256x256 image
x = Input(shape=(256, 256, 3))
# 3x3 conv with 3 output channels(same ad input channels)
y = Conv2D(3, (3,3), padding='same')(x)
# this return x+y
z = keras.layers.add([x, y])