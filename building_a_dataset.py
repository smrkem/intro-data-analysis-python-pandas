import pandas as pd
import os
import quandl

API_KEY = os.environ.get('QUANDL_API_KEY')

# df = quandl.get('FMAC/HPI_AK', authtoken=API_KEY)
# print(df.head())

fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# returns a list of dataframes gotten from tables in the html

# The DataFrame
# print(fifty_states[0])

# The column or series
# print(fifty_states[0][0])

for abbv in fifty_states[0][0][1:]:
    print("FMAC/HPI_" + str(abbv))
