import pandas as pd
import numpy as np
from helpers import SOURCES_PATH

# Get our starting data
HPI_Plus = pd.read_pickle(SOURCES_PATH + 'HPI_PLUS_DATA.pickle')

# Convert to true percent change
HPI_Plus = HPI_Plus.pct_change()

# the first row which is now NaN due to pct_change, and there are some inf, -inf values
HPI_Plus.replace([np.inf, -np.inf], np.nan, inplace=True)
HPI_Plus.dropna(inplace=True)
# print(HPI_Plus.head())
# print(HPI_Plus.tail())

# What we have are a lot of 'features' of housing price index and other data
# If we want to use this data to predict, say whether US_AVE will go up or down,
# we'll need to define a label for that.

# Start by defining a column that is the future US_AVE_HPI
HPI_Plus['US_AVE_Future'] = HPI_Plus['USA_AVE'].shift(-1)
# and ditch the pesky trailing NaN
HPI_Plus.dropna(inplace=True)

# print(HPI_Plus[['USA_AVE', 'US_AVE_Future']])
# Now each US_AVE_Future value is the next month's USA_AVE value

# What we want is a label that we can predict which will tell us if the HPI is gonna go up or not


# Start be defining a simple function that takes current HPI and future HPI and returns 1 if it goes up
def is_increased(curr_val, future_val):
    return 1 if future_val > curr_val else 0

# now add a new column to the dataframe. This is our label that we will be predicting
HPI_Plus['label'] = list(map(is_increased, HPI_Plus['USA_AVE'], HPI_Plus['US_AVE_Future']))
print(HPI_Plus[['USA_AVE', 'US_AVE_Future', 'label']])

# Looks good, let's pickle!
HPI_Plus.to_pickle(SOURCES_PATH + 'prepped_US_HPI_Plus.pickle')


