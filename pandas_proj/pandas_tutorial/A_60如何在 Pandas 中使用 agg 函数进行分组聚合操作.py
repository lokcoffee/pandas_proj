import pandas as pd

data = {
    "column": ["A", "A", "B", "B"],
    "other_column": [1, 2, 3, 4]
}
df = pd.DataFrame(data)

"""
  column  other_column
0      A             1
1      A             2
2      B             3
3      B             4
"""
print(df)

grpby=df.groupby("column")
"""
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x00000223A799A3F0>
"""
print(grpby)

result = grpby.agg({"other_column": "sum"})
"""
        other_column
column              
A                  3
B                  7
"""
print(result)
