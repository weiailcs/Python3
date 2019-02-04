# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(1.0, 2.1, 0.1, float)
# [1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ]

a = np.array([1, 2.1, 3 / 2])
a = np.array((1, 2.1, 3 / 2))
# [1.  2.1 1.5]

b = np.argsort(a)
# [0 2 1]

np.dot(a, b)
# 5.7

np.eye(3, 4)
# 3行4列的单位矩阵，默认float

np.loadtxt('data.txt', unpack=True)
# 需要满足是一个矩阵

np.mean(a)
# 1.533332

np.median(a)
# 1.5

np.ones([2, 3])

c = np.reshape(a, [3, 1])
# [[1. ]
#  [2.1]
#  [1.5]]

np.save('test.npy', a)

np.where(a, 1, 2)
# [1 1 1]
np.where(a == 1.5, 1, 2)
# [2 2 1]
np.where(a > 1)
# (array([1, 2], dtype=int64),)
