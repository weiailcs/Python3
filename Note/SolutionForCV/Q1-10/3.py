# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Q.3: Binarization

img = cv2.imread('imori.jpg').astype(np.float)
img_copy = img.copy().astype(np.uint8)

B = img[:, :, 0].copy()
G = img[:, :, 1].copy()
R = img[:, :, 2].copy()

Gray = 0.2126 * R + 0.7152 * G + 0.0722 * B
Gray = Gray.astype(np.uint8)
# 2GrayImage

BinaryImage = Gray
BinaryImage[BinaryImage < 128] = 0
BinaryImage[BinaryImage >= 128] = 255
# 2BinaryImage

cv2.imshow('solution1', BinaryImage)
cv2.imshow('solution2', cv2.cvtColor(Gray, cv2.THRESH_BINARY))

cv2.waitKey(0)
cv2.destroyAllWindows()
