import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [21, 34, 23],
    "City": ["New York", "San Francisco", "London"]
})

"""
数据框进行排序？.py 
      Name  Age           City
0    Alice   21       New York
1      Bob   34  San Francisco
2  Charlie   23         London
"""
print(df)

df_sort=df.sort_values("Age")
"""
      Name  Age           City
0    Alice   21       New York
2  Charlie   23         London
1      Bob   34  San Francisco
"""
print(df_sort)

df_sorted = df.sort_values("Age", ascending=False)
"""
      Name  Age           City
1      Bob   34  San Francisco
2  Charlie   23         London
0    Alice   21       New York
"""
print(df_sorted)

df_sorted = df.sort_values(["Age", "Name"])
"""
      Name  Age           City
0    Alice   21       New York
2  Charlie   23         London
1      Bob   34  San Francisco
"""
print(df_sorted)