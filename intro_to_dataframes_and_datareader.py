import pandas as pd
from pandas_datareader import data as web
import datetime
import plotting.pyplot as plt
import numpy as np
from plotting import style
style.use('ggplot')

web_stats = {
                'Day':[1,2,3,4,5,6],
                'Visitors': [43, 53, 34, 45, 64, 34],
                'Bounce_Rate': [65, 72, 62, 64, 54, 66]
             }

# Define the data frame. Optionally set index.
df = pd.DataFrame(web_stats)
df.set_index('Day', inplace=True)

# print(df.tail(3))
# print(df['Visitors'])
# print(df.Bounce_Rate)
# print(df[['Visitors','Bounce_Rate']])

# print(df['Visitors'].tolist())
# print(np.array(df))

# df.reset_index(inplace=True)
# my_array_data = np.array(df)
# print(my_array_data)
# new_df = pd.DataFrame(my_array_data)
# print(new_df)


## Pandas io.data

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 21)

df = web.DataReader("QCOM", "yahoo", start, end)
print(df.tail())
