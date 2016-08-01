import pandas as pd
from helpers import get_quandl_df, SOURCES_PATH

mortg_30yr_df = get_quandl_df('FMAC/MORTG', 'MORTG_30YR', trim_start='1975-01-01', percent_change=True)

# the dataframe is sampled at start of month. All our other data is end of month.
# print(mortg_30yr_df.head())

# let's resample to day (for some reason it doesn't actually need the fillna line)
mortg_30yr_df = mortg_30yr_df.resample('D').mean()
# mortg_30yr_df.fillna(method='ffill', inplace=True)
mortg_30yr_df = mortg_30yr_df.resample('M').mean()

# print(mortg_30yr_df.head())

HPI_Data = pd.read_pickle(SOURCES_PATH + 'US_HPI.pickle')
# print(HPI_Data.head())


US_HPI_M30 = HPI_Data.join(mortg_30yr_df)
# print(US_HPI_M30.head())

# Examine the correlation b/w mortg and HPI. We'd expect a pretty strong negative correlation.
print(US_HPI_M30.corr()['MORTG_30YR'])
