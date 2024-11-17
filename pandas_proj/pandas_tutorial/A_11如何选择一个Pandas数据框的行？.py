
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

"""
      Name  Age           City
0    Alice   21       New York
1      Bob   34  San Francisco
2  Charlie   23         London
"""
print(df)

rec_1 = df.loc[0]
"""
Name       Alice
Age           21
City    New York
Name: 0, dtype: object
"""
print(rec_1)

rec_2 = df.loc[[0, 1]]
"""
    Name  Age           City
0  Alice   21       New York
1    Bob   34  San Francisco
"""
print(rec_2)

rec_3 = df.loc[[0, 2], ["Name", "City"]]
"""
      Name      City
0    Alice  New York
2  Charlie    London
"""
print(rec_3)