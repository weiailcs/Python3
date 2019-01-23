# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly.plotly as py
from plotly import tools
import plotly.graph_objs as go

# tools.set_credentials_file(username='chunibyo.wly', api_key='kjcebxiY2SZfb2KyPbsX')
#
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")
#
# data = [go.Bar(x=df.School, y=df.Gap)]

# py.plot(data)
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = go.Data([trace0, trace1])

py.plot(data, filename='basic-line')