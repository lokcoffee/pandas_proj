
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

bool_idx = df["Age"] > 25
"""
0    False
1     True
2    False
Name: Age, dtype: bool
"""
print(bool_idx)

sub = df[bool_idx]
"""
Name: Age, dtype: bool
  Name  Age           City
1  Bob   34  San Francisco
"""
print(sub)

