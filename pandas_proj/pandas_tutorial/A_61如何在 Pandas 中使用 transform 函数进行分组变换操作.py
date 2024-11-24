import pandas as pd

data = {
    "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
    "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
    "C": [1, 2, 3, 4, 5, 6, 7, 8],
    "D": [10, 20, 30, 40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

"""
     A      B  C   D
0  foo    one  1  10
1  bar    one  2  20
2  foo    two  3  30
3  bar  three  4  40
4  foo    two  5  50
5  bar    two  6  60
6  foo    one  7  70
7  foo  three  8  80
"""
print(df)

grpby=df.groupby("A")
data["C_mean"]=grpby["C"].transform(lambda x: x.mean())
data["D_mean"]=grpby["D"].transform(lambda x: x.mean())

"""
{'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': [1, 2, 3, 4, 5, 6, 7, 8], 'D': [10, 20, 30, 40, 50, 60, 70, 80], 'C_mean': 0    4.8
1    4.0
2    4.8
3    4.0
4    4.8
5    4.0
6    4.8
7    4.8
Name: C, dtype: float64, 'D_mean': 0    48.0
1    40.0
2    48.0
3    40.0
4    48.0
5    40.0
6    48.0
7    48.0
Name: D, dtype: float64}
"""
print(data)