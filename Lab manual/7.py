import tensorflow as tf
import numpy as np
print("Starting...")
x = np.array([1, 2, 3, 4], dtype=float)
y = np.array([2, 4, 6, 8], dtype=float)
model = tf.keras.Sequential([
tf.keras.layers.Dense(1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=200, verbose=1)
print("Predicting...")

# import tensorflow as tf
# import numpy as np
# print("Starting...")
# x = np.array([1, 2, 3, 4], dtype=float)
# y = np.array([2, 4, 6, 8], dtype=float)
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(1, input_shape=[1])
# ])
# model.compile(optimizer='sgd', loss='mean_squared_error')
# model.fit(x, y, epochs=200, verbose=1)
# print("Predicting...")
# print(model.predict([5.0]))