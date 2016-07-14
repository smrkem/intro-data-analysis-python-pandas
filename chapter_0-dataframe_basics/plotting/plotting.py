import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 21)

df = web.DataReader("ASNA", "yahoo", start, end)
print(df.tail())

df['High'].plot()
plt.legend()
plt.show()

