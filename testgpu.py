# 该文件用于测试tensorflow能否成功调用GPU加速
import tensorflow as tf

print(tf.device('/gpu:0'))
