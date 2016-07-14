import pandas as pd

# df = pd.read_csv('sources/zill-7706-mlp.csv')
# print(df.head(10))

# df.set_index('Date', inplace=True)
# print(df.head())
# df.to_csv('sources/from_zill-7706-mlp.csv')

# df = pd.read_csv('sources/from_zill-7706-mlp.csv', index_col=0)
# print(df.head())

# df.columns = ['Austin HPI']
# print(df.head())

# df.to_csv('sources/from_zill-7706-mlp_noheaders.csv', header=False)
# df = pd.read_csv('sources/from_zill-7706-mlp_noheaders.csv', names=['Date','Austin MLP'], index_col=0)
# print(df.head())

# df.to_html('sources/from_zill-7706-mlp.html')

df = pd.read_csv('sources/from_zill-7706-mlp_noheaders.csv', names=['Date','Austin MLP'])
print(df.head())

df.rename(columns={'Austin MLP': '77006_HPI'}, inplace=True)
print(df.head())
