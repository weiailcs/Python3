# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('data.png', 0)
n, m = img.shape
# (981, 1697, 3)
print(img.dtype)
# uint8

cv2.imshow("GrayScale", img)
cv2.imwrite('output.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
