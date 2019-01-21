# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(16)
a = np.where(a % 3 == 0, 1.0, -1.0)
print(a)

plt.hist(a, normed=True)
# 绘制直方图
# https://blog.csdn.net/u013230234/article/details/75451833
# https://blog.csdn.net/u012111465/article/details/79375897

plt.show()
