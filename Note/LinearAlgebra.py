# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

A = np.mat([[1, 2], [3, 4]])
# np.array的运算符效果和np.matrix不一样
np.linalg.inv(A) * A - np.eye(2)
# [[ 2.22044605e-16  4.44089210e-16] [ 0.00000000e+00 -2.22044605e-16]]

A = np.mat([[1, -2, 1], [0, 2, -8], [-4, 5, 9]])
B = np.mat([[0], [8], [-9]])
np.reshape(np.linalg.solve(A, B), [1, 3])
# [[29. 16.  3.]]

A = np.mat([[3, -2], [1, 0]])
eign_values, eign_vector = np.linalg.eig(A)
# eignvalues: [2. 1.]
# eignvectors: [[0.89442719 0.70710678]
#               [0.4472136  0.70710678]]
for i in range(len(eign_values)):
    print(np.dot(A, eign_vector[:, i]))
    print(np.dot(eign_values[i], eign_vector[:, i]))
    print(np.dot(A, eign_vector[:, i]) - np.dot(eign_values[i], eign_vector[:, i]) <= 0.0001, end="\n\n")
