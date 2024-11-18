import pandas as pd


data = {
    "A": [1, 2, None, 4],
    "B": [5, None, 7, 8],
    "C": [9, 10, 11, None]
}
df = pd.DataFrame(data)
"""
     A    B     C
0  1.0  5.0   9.0
1  2.0  NaN  10.0
2  NaN  7.0  11.0
3  4.0  8.0   NaN
"""
print(df)


df_dropna=df.dropna()
"""
     A    B    C
0  1.0  5.0  9.0
"""
print(df_dropna)

df_dropna_col=df.dropna(axis=1)
"""
Empty DataFrame
Columns: []
Index: [0, 1, 2, 3]
"""
print(df_dropna_col)

df_dropna_colB=df.dropna(subset=["B"])
"""
     A    B     C
0  1.0  5.0   9.0
2  NaN  7.0  11.0
3  4.0  8.0   NaN

"""
print(df_dropna_colB)