import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 5, 10)

df = web.DataReader('6098.hk', 'yahoo', start, end)
df2 = web.DataReader('6049.hk', 'yahoo', start, end)
# print(df.head())
# df.to_csv('hsidata.csv')

fig = plt.figure(figsize = [14, 6])

ax1 = fig.add_subplot(121, ylabel = '6098')
df['Close'].plot(ax = ax1, color = 'r', lw = 2)

ax2 = fig.add_subplot(122, ylabel = '6049') # 11 means 1x1 chart, 12 means 1x2, the 3rd 1 means the no. of chart in this set
df2['Close'].plot(ax = ax2, color = 'b', lw = 2)


plt.show()
