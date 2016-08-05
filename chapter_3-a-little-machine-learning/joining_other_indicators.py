import pandas as pd
import quandl
from helpers import API_KEY, SOURCES_PATH


def get_quandl_df_generic(symbol, label, newlabel, percent_change=False, trim_start=None):
    df = quandl.get(symbol, authtoken=API_KEY, trim_start=trim_start)
    df.rename(columns={label: newlabel}, inplace=True)
    if percent_change:
        # percent change is (new - old) / old
        df[newlabel] = (df[newlabel] - df[newlabel][0]) / df[newlabel][0] * 100.0
    df = df[newlabel]
    df = df.resample('M').mean()
    return df


sp500_Data = get_quandl_df_generic(
    "YAHOO/INDEX_GSPC",
    "Adjusted Close",
    "sp500",
    percent_change=True,
    trim_start="1975-01-01"
)
# print(sp500_Data.head())

# Only finding GDP data monthly from 1990 :(
GDP_Data = get_quandl_df_generic(
    'EIA/STEO_GDPQXUS_M',
    'Value',
    'GDP',
    percent_change=True,
    trim_start='1975-01-01'
)
# print(GDP_Data.head(12))

# This unemployment rate is in percent, but should work out ok
us_unemployment = get_quandl_df_generic(
    "ECB/RTD_M_US_Y_L_UNETO_F",
    "Percent",
    "US_Unemployment",
    percent_change=True,
    trim_start='1975-01-01'
)
# print(us_unemployment.head(15))

# OK - time to pull it all together. This pickle has all state HPIs and the US_AVE
US_HPI = pd.read_pickle(SOURCES_PATH + 'US_HPI.pickle')

# And grab the 30yr mortgage rate from before:
US_30YR_MORTG = pd.read_pickle(SOURCES_PATH + 'US_MORTG_30YR.pickle')

# So putting them all together in one DF:
HPI_Plus_Data = US_HPI.join([US_30YR_MORTG, sp500_Data, GDP_Data, us_unemployment])
# print(HPI_Plus_Data.head())
# print(HPI_Plus_Data.tail())

# We have some NaN data (mainly from GDP) which will get dropped, but let's pickle the data pre_dropping first
HPI_Plus_Data.to_pickle(SOURCES_PATH + 'ALL_HPI_PLUS_DATA.pickle')

# Now we can drop na and look at the result
HPI_Plus_Data.dropna(inplace=True)
HPI_Plus_Data.to_pickle(SOURCES_PATH + 'HPI_PLUS_DATA.pickle')
print(HPI_Plus_Data.head())
print(HPI_Plus_Data.tail())
