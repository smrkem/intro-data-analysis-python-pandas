import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

# Define some data points with a clear outlier / bad data
bridge_height = {'meters': [10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}

df = pd.DataFrame(bridge_height)
print(df)

# Method 1: Get rolling std for each value and compare to
# some constant times the df std.
# ========================================================
# df['std'] = df.rolling(window=2, center=False).std()

# print(df.describe())
# metres_std = df.describe()['meters']['std']
# print(metres_std)

# df = df[(df['std'] < 1.5 * metres_std)]
# print(df)

# This results in losing data points 0, 5 and 6.
# 0 - because the std is NaN
# 5,6 - because the std is greater than 1.5 times the sets std

# The only real outlier is data point 5.


# Method 2: Lose the data point that is X standard units or
# greater away from the mean
# ========================================================
# standard_deviation = df.describe()['meters']['std']
# mean = df.describe()['meters']['mean']
# print(standard_deviation, mean)

# std_unit_threshold = 2
# lower_bound = mean - (std_unit_threshold * standard_deviation)
# upper_bound = mean + (std_unit_threshold * standard_deviation)
# print(lower_bound, upper_bound)


# df = df[(df['meters'] < upper_bound )]
# print(df)
# df.plot()


# Method 3: Let's look at the z-scores. This is similar to
# method 2
# ========================================================
standard_deviation = df.describe()['meters']['std']
mean = df.describe()['meters']['mean']
df['z-score'] = (df['meters'] - mean) / standard_deviation
# print(df)

# Any z score outside of -2.5, 2.5 gets deleted:
df = df[(df['z-score'] < 2.5)]
df['meters'].plot()
print(df)



plt.legend()
plt.show()