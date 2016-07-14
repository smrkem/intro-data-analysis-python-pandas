import os, pandas as pd, quandl, pickle
from quandl.errors.quandl_error import LimitExceededError
import matplotlib.pyplot as plt
from matplotlib import style
# style.use('fivethirtyeight')
style.use('ggplot')
API_KEY = os.environ.get('QUANDL_API_KEY')


# HPI_data = pd.read_pickle('../sources/US_STATES_HPI.pickle')
# def get_quandl_df(label, newlabel, percent_change=False):
#     df = quandl.get(label, authtoken=API_KEY)
#     df.rename(columns={'Value': newlabel}, inplace=True)
#     if percent_change:
#         df[newlabel] = (df[newlabel] - df[newlabel][0]) / df[newlabel][0] * 100.0
#     return df


HPI_data = pd.read_pickle('../sources/US_STATES_HPI_percent_change.pickle')

# HPI_Benchmark = get_quandl_df('FMAC/HPI_USA', 'USA_AVE', percent_change=True)

# print(HPI_Benchmark.head(4))

# Columns:
# print(HPI_data['TX'].head())
# HPI_data['TX2'] = HPI_data['TX'] * 2
# print(HPI_data[['TX','TX2']].head())

# Plotting all the data
# =====================
# HPI_data.plot()
# plt.legend().remove()
# plt.show()


# Converting data to percent change data
# 1. rewrite the get__data function to optionally convert to percent change
# 2. Get us average HPI and assemble the data



# 3. Configure the plots
# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1),(0,0))

# HPI_data.plot(ax=ax1)
# HPI_Benchmark.plot(ax=ax1, color='k', linewidth=3)

# 4. show
# plt.legend().remove()
# plt.show()



# HPI_State_Correlations = HPI_data.corr()
# print(HPI_State_Correlations.head())
# print(HPI_State_Correlations.describe())








# def get_state_abbrevs(start_index=0, stop_index=None):
#     fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#     return fifty_states[0][0][1+start_index:stop_index]
#
#
# def get_initial_state_data(percent_change=False):
#     states = get_state_abbrevs()
#     initial_state = ''
#     last_state = ''
#     main_df = pd.DataFrame()
#     for abbv in states:
#         print("FMAC/HPI_" + abbv)
#         try:
#             df = quandl.get('FMAC/HPI_{}'.format(abbv), authtoken=API_KEY)
#             df.rename(columns={'Value': abbv}, inplace=True)
#             last_state = str(abbv)
#             if percent_change:
#                 df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
#             if main_df.empty:
#                 initial_state = str(abbv)
#                 main_df = df
#             else:
#                 main_df = main_df.join(df)
#         except LimitExceededError:
#             file_name = "{0}_to_{1}_HPI.pickle".format(initial_state, last_state)
#             print("Query failed after {}. Pickling...".format(last_state))
#             pickle_out = open(file_name, 'wb')
#             pickle.dump(main_df, pickle_out)
#             pickle_out.close()
#             break
#     return main_df
#
# HPI_data = get_initial_state_data(percent_change=True)
# print(HPI_data.tail())
# HPI_data.to_pickle('../sources/US_STATES_HPI_percent_change.pickle')

