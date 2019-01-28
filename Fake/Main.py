# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
# import plotly
# from plotly import tools
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# tools.set_credentials_file(username='chunibyo.wly', api_key='kjcebxiY2SZfb2KyPbsX')

x = np.arange(200)
y = np.arange(0.0, 200.0, 1.0, float)
cnt = 1

while cnt < 180:
    for i in range(int(np.random.randint(1, 15))):
        y[cnt] = (np.abs(np.cos(x[cnt])) + 1) * np.random.randint(5) + np.random.randint(5) + 1
        cnt = cnt + 1

for i in range(180):
    if i % 13 == 0:
        y[i] = 7

plt.xlim(0, 180)
plt.ylim(0, 15)
plt.scatter(x, y)
plt.savefig('14.png')
plt.show()
