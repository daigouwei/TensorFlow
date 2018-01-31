import tensorflow as tf
import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot = True)

# 设置变量
x = tf.placeholder("float", [None, 784]) #x只是一个占位符，用于输入n张图片
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# 定义模型
y = tf.nn.softmax(tf.matmul(x,W)+b)

y_ = tf.placeholder("float", [None, 10]) #正确的打标签的输出
cross_entropy = -tf.reduce_sum(y_*tf.log(y)) #交叉熵，损失函数
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy) #梯度下降算法

# 初始化创建的变量并启动模型
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 开始训练模型
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x:batch_xs, y_:batch_ys})


# 评估模型
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x:mnist.test.images, y_: mnist.test.labels}))