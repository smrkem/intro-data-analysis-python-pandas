import time, pandas as pd
from helpers import SOURCES_PATH, get_quandl_df

# print(SOURCES_PATH)

# We already have a pickle from the building_a_dataset script
HPI_Data = pd.read_pickle(SOURCES_PATH + 'US_STATES_HPI_percent_change.pickle')

# print(HPI_Data.tail())
#
# Get Benchmark HPI
# HPI_Benchmark = get_quandl_df('FMAC/HPI_USA', 'USA_AVE', percent_change=True)
# Save it this time
# HPI_Benchmark.to_pickle(SOURCES_PATH + 'US_STATES_HPI_BENCHMARK_{}.pickle'.format(time.strftime("%Y-%m-%d")))
HPI_Benchmark = pd.read_pickle(SOURCES_PATH + 'US_STATES_HPI_BENCHMARK.pickle')
# print(HPI_Benchmark.tail(10))

HPI_Data2 = HPI_Data.join(HPI_Benchmark)

print(HPI_Data2.head())

# And lets save the whole thing:
HPI_Data2.to_pickle(SOURCES_PATH + 'US_HPI.pickle')

