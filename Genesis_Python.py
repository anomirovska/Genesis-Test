import pandas as pd
df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df
print("Data grouped by category:")
for item in df.groupby(['grps']):
    print(item)
print("Sum of the 3 biggest values in each group:")
print(df.sort_values(['vals'], ascending=False).groupby(['grps']).head(3).groupby(['grps']).sum())
