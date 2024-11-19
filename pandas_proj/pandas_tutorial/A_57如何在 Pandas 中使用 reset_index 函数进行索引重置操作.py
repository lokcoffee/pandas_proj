import pandas as pd

data = {
    "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
    "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
    "C": [1, 2, 3, 4, 5, 6, 7, 8],
    "D": [8, 7, 6, 5, 4, 3, 2, 1]
}

df = pd.DataFrame(data)
"""
     A      B  C  D
0  foo    one  1  8
1  bar    one  2  7
2  foo    two  3  6
3  bar  three  4  5
4  foo    two  5  4
5  bar    two  6  3
6  foo    one  7  2
7  foo  three  8  1
"""
print(df)

indexed = df.set_index(["A", "B"])
"""
           C  D
A   B          
foo one    1  8
bar one    2  7
foo two    3  6
bar three  4  5
foo two    5  4
bar two    6  3
foo one    7  2
    three  8  1
"""
print(indexed)
reseted = indexed.reset_index()
"""
     A      B  C  D
0  foo    one  1  8
1  bar    one  2  7
2  foo    two  3  6
3  bar  three  4  5
4  foo    two  5  4
5  bar    two  6  3
6  foo    one  7  2
7  foo  three  8  1
"""
print(reseted)