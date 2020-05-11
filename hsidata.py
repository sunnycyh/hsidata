import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 5, 10)

df = web.DataReader('^hsi', 'yahoo', start, end)
print(df.head())
df.to_csv('hsidata.csv')