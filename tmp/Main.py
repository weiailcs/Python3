# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

for n in range(3, 105, 1):
    Matrix = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            if i == j:
                Matrix[i][j] = 3
            if i - j == 1:
                Matrix[i][j] = -1
            if i - j == -1:
                Matrix[i][j] = -1
    Matrix[0][n - 1] = Matrix[n - 1][0] = -1
    # print(Matrix)
    print('","', end="")
    print(int(np.linalg.det(Matrix) + 0.500), end="")

# a = np.arange(0, 110, 1, dtype=np.float64)
# a[0] = 1.0
# a[1] = 5.0
# for i in range(2, 101, 1):
#     a[i] = 3.0 * a[i - 1] + 2.0 - a[i - 2]
# for i in a:
#     print('","', end="")
#     print(int(i), end="")
