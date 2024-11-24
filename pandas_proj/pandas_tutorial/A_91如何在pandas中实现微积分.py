import pandas as pd

data = {
    "time": [1, 2, 3, 4, 5],
    "value": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

print(df)


df["diff1"] = df["value"].diff()
df["diff2"] = df["diff1"].diff()
"""
   time  value  diff1  diff2
0     1     10    NaN    NaN
1     2     20   10.0    NaN
2     3     30   10.0    0.0
3     4     40   10.0    0.0
4     5     50   10.0    0.0
"""
print(df)

# CANT UNDERSTAND