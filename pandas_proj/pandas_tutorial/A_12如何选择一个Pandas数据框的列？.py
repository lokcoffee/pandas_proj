
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

"""
0      Alice
1        Bob
2    Charlie
Name: Name, dtype: object
"""
print(df["Name"])

"""
      Name           City
0    Alice       New York
1      Bob  San Francisco
2  Charlie         London
"""
print(df[["Name", "City"]])

"""
0      Alice
1        Bob
2    Charlie
Name: Name, dtype: object
"""
print(df.iloc[:,0])

"""
      Name  Age           City
0    Alice   21       New York
1      Bob   34  San Francisco
2  Charlie   23         London
"""
print(df.iloc[:,0:3])

"""
   Age           City
0   21       New York
1   34  San Francisco
2   23         London
"""
print(df.iloc[:,1:3])