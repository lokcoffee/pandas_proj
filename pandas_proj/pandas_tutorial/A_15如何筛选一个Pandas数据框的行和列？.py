import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

sub = df.loc[df["Age"] > 25, ["Name", "Age"]]
"""
  Name  Age
1  Bob   34
"""
print(sub)

sub = df.loc[df["Name"] == "Bob", ["Name", "Age"]]
"""
  Name  Age
1  Bob   34
"""
print(sub)

sub = df.iloc[[1], [0, 1]]
"""
  Name  Age
1  Bob   34
"""
print(sub)

sub = df.iloc[1, 0:2]
"""
Name    Bob
Age      34
Name: 1, dtype: object
"""
print(sub)