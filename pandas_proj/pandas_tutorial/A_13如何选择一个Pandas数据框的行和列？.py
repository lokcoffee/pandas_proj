import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

sub = df.loc[[0, 2], ["Name", "Age"]]
"""
      Name  Age
0    Alice   21
2  Charlie   23
"""
print(sub)

sub = df.iloc[[0, 2], [0, 1]]
"""
      Name  Age
0    Alice   21
2  Charlie   23
"""
print(sub)