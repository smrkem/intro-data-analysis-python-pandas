import os, quandl

SOURCES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'sources') + '/'
API_KEY = os.environ.get('QUANDL_API_KEY')


def get_quandl_df(label, newlabel, percent_change=False):
    df = quandl.get(label, authtoken=API_KEY)
    df.rename(columns={'Value': newlabel}, inplace=True)
    if percent_change:
        # percent change is (new - old) / old
        df[newlabel] = (df[newlabel] - df[newlabel][0]) / df[newlabel][0] * 100.0
    return df

