import pandas as pd

data = {

    "A": [1.0, 2.0, 3.0],
    "B": ['4', '5', '6']
}

df = pd.DataFrame(data)
"""
     A  B
0  1.0  4
1  2.0  5
2  3.0  6
"""
print(df)

df["B"] = df["B"].astype(float)
"""
A    float64
B    float64
dtype: object
"""
print(df.dtypes)