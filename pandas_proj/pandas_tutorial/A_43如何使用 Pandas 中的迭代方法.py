import pandas as pd

data = {
    "Name": ["Jack", "Sarah", "Mike", "David"],
    "Age": [24, 30, 21, 29],
    "Gender": ["M", "F", "M", "M"]
}
df = pd.DataFrame(data)
"""
    name  age  height
0   Jack   24     175
1  Sarah   30     165
2   Mike   21     180
3  David   29     173
"""
print(df)

"""
Name      Jack
Age         24
Gender       M
Name: 0, dtype: object
Name      Sarah
Age          30
Gender        F
Name: 1, dtype: object
Name      Mike
Age         21
Gender       M
Name: 2, dtype: object
Name      David
Age          29
Gender        M
Name: 3, dtype: object
"""
for index, rows in df.iterrows():
    print(rows)