import pandas as pd

df1 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55]
}, index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55]
}, index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'Low_tier_HPI': [50, 52, 50, 53]
}, index=[2001, 2002, 2003, 2004])

# Concatenation and Appending
# ============================
concat1 = pd.concat([df1, df2])
# print(concat1)

concat2 = pd.concat([df1, df2, df3])
# print(concat2)

df4 = df1.append(df2)
# print(df4)

df5 = df1.append(df3)
# print(df5)

s = pd.Series([78, 2, 49], index=['HPI', 'Int_rate', 'US_GDP_Thousands'])
df6 = df1.append(s, ignore_index=True)
# print(df6)


# Joining and Merging
# =============================
df3 = pd.DataFrame({
    'HPI': [80, 85, 88, 85],
    'Unemployment': [7, 8, 9, 6],
    'Low_tier_HPI': [50, 52, 50, 53]
}, index=[2001, 2002, 2003, 2004])

# print(pd.merge(df1, df2, on='HPI'))
# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
# print(joined)

ddf1 = pd.DataFrame({
    'Year': [2001, 2002, 2003, 2004],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50, 55, 65, 55]
})
ddf2 = pd.DataFrame({
    'Year': [2001, 2003, 2004, 2005],
    'Unemployment': [7, 8, 9, 6],
    'Low_tier_HPI': [50, 52, 50, 53]
})

merged = pd.merge(ddf1, ddf2, on='Year')
merged.set_index('Year', inplace=True)
# print(merged)

merged1 = pd.merge(ddf1, ddf2, on='Year', how='left')
merged1.set_index('Year', inplace=True)
print(merged1)

merged2 = pd.merge(ddf1, ddf2, on='Year', how='right')
merged2.set_index('Year', inplace=True)
print(merged2)

merged3 = pd.merge(ddf1, ddf2, on='Year', how='outer')
merged3.set_index('Year', inplace=True)
print(merged3)
