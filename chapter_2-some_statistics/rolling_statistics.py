import matplotlib.pyplot as plt
import pandas as pd


HPI_data = pd.read_pickle('../sources/US_HPI.pickle')
fig = plt.figure()
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0), sharex=ax1)


# Get a rolling average for 12 months:
# ====================================
# HPI_data['NY_12MMA_old'] = pd.rolling_mean(HPI_data['NY'], 12) # old way
# HPI_data['NY_12MMA'] = HPI_data['NY'].rolling(window=12, center=False).mean()

# print(HPI_data[['NY', 'NY_12MMA', 'NY_12MMA_old']].tail(10))

# Plot stuff:
# HPI_data[['NY', 'NY_12MMA']].plot(ax=ax1)


# Get a rolling standard deviation for 12 months:
# ===============================================
# HPI_data['NY_12MSTD_old'] = pd.rolling_std(HPI_data['NY'], 12) # old way
# HPI_data['NY_12MSTD'] = HPI_data['NY'].rolling(window=12, center=False).std()

# print(HPI_data[['NY', 'NY_12MSTD', 'NY_12MSTD_old']].tail(9))
# print(HPI_data[['NY', 'NY_12MSTD']].tail(9))


# Nice, but standard deviation is a totally different scale. plotting the two normally isn't helpful

# Plot stuff:
# HPI_data[['NY', 'NY_12MSTD']].plot(ax=ax1)

# So we graph it on a different graph.
# HPI_data['NY_12MSTD'].plot(ax=ax2)


# Get a rolling correlation b/w NY and the US Benchmark for 12 months:
# ===============================================
HPI_data['NY_12MCOR_TO_MEAN'] = pd.rolling_corr(HPI_data['NY'], HPI_data['USA_AVE'], 12)

print(HPI_data[['NY', 'USA_AVE', 'NY_12MCOR_TO_MEAN']])
HPI_data['NY'].plot(ax=ax1, label='NY_HPI')
HPI_data['USA_AVE'].plot(ax=ax1, label='US_AVE')
HPI_data['NY_12MCOR_TO_MEAN'].plot(ax=ax2, label='NY-US_AVE-Correlation')
ax1.legend(loc=2)

plt.legend(loc=4)
plt.show()
