# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Q.4: Binarization of Otsu
# https://zh.wikipedia.org/wiki/%E5%A4%A7%E6%B4%A5%E7%AE%97%E6%B3%95

img = cv2.imread("imori.jpg", 0)

ret1, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('result1', th1)
cv2.imshow('result2', th2)
cv2.imshow('result3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
