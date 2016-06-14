import pandas as pd
import os
import quandl

API_KEY = os.environ.get('QUANDL_API_KEY')

df = quandl.get('FMAC/HPI_AK', authtoken=API_KEY)
print(df.head())
