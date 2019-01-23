# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

tools.set_credentials_file(username='chunibyo.wly', api_key='kjcebxiY2SZfb2KyPbsX')

import scipy.optimize as opt

f = lambda x: np.cos(x) - x

x = np.linspace(-5, 5, 10000)
y = f(x)
x_0 = opt.bisect(f, -5, 5)
# f(a),f(b)必须异号

plt.subplot(211)
plt.plot(x, y)
plt.scatter(x_0, f(x_0))
plt.axhline(0)

plt.subplot(212)
f = lambda x: 1 - np.sin(x) / x
xmin = opt.basinhopping(f, 3, stepsize=5).x
x = np.linspace(-5, 5, 10000)
y = f(x)
plt.plot(x, y)
plt.scatter(xmin, f(xmin))

plt.show()


def g(X):
    x, y = X
    return (x - 1) ** 4 + 5 * (y - 1) ** 2 - 2 * x * y


fig, ax = plt.subplots(figsize=(6, 4))
x_, y_ = np.linspace(-1, 4, 100)
X,Y=np.meshgrid(x_,y_)
plt.show()
