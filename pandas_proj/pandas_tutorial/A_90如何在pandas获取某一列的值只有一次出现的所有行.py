import pandas as pd

data = {
    "A": ["a", "b", "c", "d", "a", "d"],
    "B": ["b", "c", "e", "f", "h", "g"]
}

df = pd.DataFrame(data)

value_counts=df["A"].value_counts()
"""
A
a    2
d    2
b    1
c    1
"""
print(value_counts)

result = df[df["A"].isin(list(value_counts[value_counts == 1].index))]
"""
Name: count, dtype: int64
   A  B
1  b  c
2  c  e
"""
print(result)


# CANT understand