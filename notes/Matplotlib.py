# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 子图1
plt.subplot(311)
a = np.arange(16)
line = plt.plot(a, a ** 2, 'bs')
plt.setp(line, color='r', linewidth=0.1)
plt.ylabel('some numbers')

# 子图2
plt.subplot(312)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# 从正态分布中返回10000个样本值
plt.hist(x, bins=50, density=1, facecolor='g', alpha=.75)
# 绘制直方图
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.xscale('log')
# 对数轴
plt.grid(True)
# https://blog.csdn.net/u013230234/article/details/75451833
# https://blog.csdn.net/u012111465/article/details/79375897

plt.subplot(313)
data = [[0, 0.25], [0.5, 0.75]]
im = plt.imshow(data, cmap=plt.get_cmap('hot'), interpolation='nearest', vmin=0, vmax=1)
plt.colorbar(im)

plt.show()
