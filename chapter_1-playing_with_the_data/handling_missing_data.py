import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('../sources/US_STATES_HPI_percent_change.pickle')
NY1yr = HPI_data['NY'].resample('A').mean()

# NY1yr only has data points for each year, HPI_data does for every month.

# Let's combine them:
HPI_data['NY1yr'] = NY1yr
print(HPI_data[['NY', 'NY1yr']].tail(25))

# One column has a value for every row, but NY1yr has only
# one value every 12th row. We could:

# 1. Delete all rows except the ones with values in both:
# HPI_data.dropna(inplace=True)

# 2. Fill empty rows in the NY1yr col, using either the value before or after
# HPI_data.fillna(method='ffill', inplace=True)
HPI_data.fillna(method='bfill', inplace=True)

# 3. Fill empty rows in the NY1yr col with a specific value - useful when outliers can be ignored
# HPI_data.fillna(value=-999999, inplace=True)

print(HPI_data[['NY', 'NY1yr']].tail(25))
HPI_data[['NY', 'NY1yr']].plot(ax=ax1)










plt.legend()
plt.show()


