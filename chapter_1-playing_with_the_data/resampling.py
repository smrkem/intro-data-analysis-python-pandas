import os, pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
# get initial data
HPI_data = pd.read_pickle('../sources/US_STATES_HPI_percent_change.pickle')
# NY1yr = HPI_data['NY'].resample('A').mean()
NY1yr = HPI_data['NY'].resample('A').ohlc()
print(NY1yr.head())


HPI_data['NY'].plot(ax=ax1, label='Monthly NY HPI')
NY1yr.plot(ax=ax1, label='Yearly NY HPI')

plt.legend(loc=2)
plt.show()


