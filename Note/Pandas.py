# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
# 当我们设置相同的seed时，每次生成的随机数也相同，如果不设置seed，则每次生成的随机数都会不一样
a = np.random.randn(3, 4)
a[2][2] = np.nan
# [[ 0.49671415 -0.1382643   0.64768854  1.52302986]
#  [-0.23415337 -0.23413696  1.57921282  0.76743473]
#  [-0.46947439  0.54256004         nan -0.46572975]]
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header=", #1, #2, #3, #4")

df = pd.DataFrame(a)
#           0         1         2         3
# 0  0.496714 -0.138264  0.647689  1.523030
# 1 -0.234153 -0.234137  1.579213  0.767435
# 2 -0.469474  0.542560       NaN -0.465730
df.to_csv('pd.csv', float_format='%.2f', na_rep='NAN!')
