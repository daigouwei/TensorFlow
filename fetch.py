import tensorflow as tf

input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
intermed = tf.add(input2, input3)
mul = tf.multiply(input1, intermed)

init_op = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init_op)
    result = sess.run([mul, intermed])
    print(result)
