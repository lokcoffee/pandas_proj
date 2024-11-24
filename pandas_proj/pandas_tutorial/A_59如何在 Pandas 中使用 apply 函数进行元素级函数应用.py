import pandas as pd

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6]
}
df = pd.DataFrame(data)
"""
   A  B
0  1  4
1  2  5
2  3  6
"""
print(df)


def multiple_b_2(x):
    return x * 2

result = df.apply(multiple_b_2)
"""
   A   B
0  2   8
1  4  10
2  6  12
"""
print(result)
