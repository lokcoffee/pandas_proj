import pandas as pd

data1 = {
    "key": ["A", "B", "C", "D"],
    "value1": [1, 2, 3, 4]
}

data2 = {
    "key": ["A", "B", "C", "D"],
    "value2": [5, 6, 7, 8]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1)
print(df2)

df = df1.join(df2.set_index("key"), on="key", how="inner")
"""
  key  value1  value2
0   A       1       5
1   B       2       6
2   C       3       7
3   D       4       8

"""
print(df)
