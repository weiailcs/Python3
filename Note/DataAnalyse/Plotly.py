# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

tools.set_credentials_file(username='chunibyo.wly', api_key='kjcebxiY2SZfb2KyPbsX')

# https://www.cnblogs.com/feffery/p/9293745.html

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)

'''创建仿真数据'''
N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

'''构造trace0'''
trace2 = go.Scatter(
    x=random_x,
    y=random_y0,
    mode='markers',
    name='markers'
)

'''构造trace1'''
trace3 = go.Bar(
    x=random_x,
    y=random_y1,
    # mode='lines+markers',
    # name='lines+markers'
)

'''构造trace2'''
trace4 = go.Scatter(
    x=random_x,
    y=random_y2,
    mode='lines',
    name='lines'
)

data = [trace0, trace1, trace2, trace3, trace4]
py.plot(data, filename='basic-line.html')
