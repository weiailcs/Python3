# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# img = cv2.imread('data.png', cv2.IMREAD_GRAYSCALE)
#
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# https://blog.csdn.net/liangjiubujiu/article/details/80420555
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
# plt.show()
# methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
#            'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
#            'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# grid = np.random.rand(4, 4)
#
# fig, axes = plt.subplots(3, 6, figsize=(12, 6), subplot_kw={'xticks': [], 'yticks': []})
#
# fig.subplots_adjust(hspace=0.3, wspace=0.05)
#
# for ax, interp_method in zip(axes.flat, methods):
#     ax.imshow(grid, interpolation=interp_method, cmap='viridis')
#     ax.set_title(interp_method)
#
# plt.show()
