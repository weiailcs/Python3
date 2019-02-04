# For division
from __future__ import division

# Let's go ahead and start with some imports
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# For Visualization
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

# For reading stock data from yahoo
from pandas_datareader.data import DataReader

# For time stamps
from datetime import datetime

# The tech stocks we'll use for this analysis
tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Set up End and Start times for data grab
end = datetime.now()
start = datetime(end.year - 1, end.month, end.day)

# For loop for grabing yahoo finance data and setting as a dataframe

for stock in tech_list:
    # Set DataFrame as the Stock Ticker
    globals()[stock] = DataReader(stock, 'yahoo', start, end)

# Summary Stats
AAPL.describe()
