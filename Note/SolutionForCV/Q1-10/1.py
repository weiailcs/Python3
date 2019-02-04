# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Q.1: Channel Swapping

img = cv2.imread('imori.jpg')
img_copy = img.copy()

B = img[:, :, 0].copy()
G = img[:, :, 1].copy()
R = img[:, :, 2].copy()
# BGR

img[:, :, 0] = R
img[:, :, 1] = G
img[:, :, 2] = B
# RGB

cv2.imshow('Solution1', img)
cv2.imshow('Solution2', cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
# show

cv2.waitKey(0)
cv2.destroyAllWindows()
