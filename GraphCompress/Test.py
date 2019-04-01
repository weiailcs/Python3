# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

vector = [x for x in range(30)]

block_size = int(np.sqrt(len(vector)))
dp = [0] * (block_size + 5)

print(block_size)

for i in range(len(vector)):
    print('#'+str(i))
    for j in range(i // block_size * block_size, i):
        print(str(j), end=' ')
    print('')
