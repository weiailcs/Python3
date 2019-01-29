# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import plotly
# from plotly import tools
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# tools.set_credentials_file(username='chunibyo.wly', api_key='kjcebxiY2SZfb2KyPbsX')

x = np.linspace(0.0, 100.0, 100)
y = np.linspace(0.0, 100.0, 100)
for i in range(100):
    if x[i] <= 17:
        y[i] = np.sin(x[i])
    else:
        y[i] = np.sin(x[i])

plt.plot(x, y)
plt.show()
