import os, pandas as pd, quandl, pickle
from quandl.errors.quandl_error import LimitExceededError

API_KEY = os.environ.get('QUANDL_API_KEY')


def get_state_abbrevs(start_index=0, stop_index=None):
    fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fifty_states[0][0][1+start_index:stop_index]


def get_initial_state_data():
    states = get_state_abbrevs()
    initial_state = ''
    last_state = ''
    main_df = pd.DataFrame()
    for abbv in states:
        print("FMAC/HPI_" + str(abbv))
        try:
            df = quandl.get('FMAC/HPI_{}'.format(str(abbv)), authtoken=API_KEY)
            df.rename(columns={'Value': str(abbv)}, inplace=True)
            last_state = str(abbv)
            if main_df.empty:
                initial_state = str(abbv)
                main_df = df
            else:
                main_df = main_df.join(df)
        except LimitExceededError:
            file_name = "{0}_to_{1}_HPI.pickle".format(initial_state, last_state)
            print("Query failed after {}. Pickling...".format(last_state))
            pickle_out = open(file_name, 'wb')
            pickle.dump(main_df, pickle_out)
            pickle_out.close()
            break
    return main_df


# fiddy_states = get_initial_state_data()
# file_name = "US_STATES_HPI.pickle"
# print('pickling...')
# pickle_out = open(file_name, 'wb')
# pickle.dump(fiddy_states, pickle_out)
# pickle_out.close()

HPI_data = pd.read_pickle('sources/US_STATES_HPI.pickle')
print(HPI_data.tail())

# HPI_data.to_pickle('sources/US_STATES_HPI.pickle')

# df = quandl.get('FMAC/HPI_AK', authtoken=API_KEY)
# print(df.head())

# fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# returns a list of dataframes gotten from tables in the html

# The DataFrame
# print(fifty_states[0])

# The column or series
# print(fifty_states[0][0])
# states = get_state_abbrevs()
# main_df = pd.DataFrame()
# for abbv in states:
#     print("FMAC/HPI_" + str(abbv))
#     df = quandl.get('FMAC/HPI_{}'.format(str(abbv)), authtoken=API_KEY)
#     df.rename(columns={'Value': str(abbv)}, inplace=True)
#     if main_df.empty:
#         main_df = df
#     else:
#         main_df = main_df.join(df)
#
# print(main_df.tail())

# first_states = get_state_abbrevs(stop_index=10)
# first_states = get_state_abbrevs()
# print(first_states)
# for abbv in first_states:
#     print(abbv)

