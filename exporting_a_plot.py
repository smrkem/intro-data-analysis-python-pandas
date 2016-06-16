import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import base64
from io import BytesIO


from matplotlib import style

style.use('fivethirtyeight')


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 21)

df = web.DataReader("ASNA", "yahoo", start, end)
print(df.tail())

df['High'].plot()
plt.legend()


# Exporting to a file
# plt.savefig('test.png')


# Exporting to a Data URI
sio = BytesIO()
plt.savefig(sio, format='png')
data = base64.encodebytes(sio.getvalue()).decode()
data_url = 'data:image/png;base64,{}'.format(data)
print('<img src="{}" />'.format(data_url), end="\n\n")


