from pandas_datareader import data as web
import datetime


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 21)

df = web.DataReader("ASNA", "yahoo", start, end)
print(df.tail())

df2 = web.DataReader("ASNA", 'google', start, end)
print(df2.tail())
