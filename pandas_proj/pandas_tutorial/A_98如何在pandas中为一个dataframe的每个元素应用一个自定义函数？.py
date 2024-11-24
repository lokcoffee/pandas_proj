import pandas as pd


def double(x):
    return x * 2


data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}

df = pd.DataFrame(data)
"""
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
"""
print(df)

df = df.apply(double)
"""
   A   B   C
0  2   8  14
1  4  10  16
2  6  12  18
"""
print(df)
