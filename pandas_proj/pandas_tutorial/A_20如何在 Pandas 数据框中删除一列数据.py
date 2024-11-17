import pandas as pd

data = {
    "name": ["Jack", "Sarah", "Mike", "David"],
    "age": [24, 30, 21, 29],
    "height": [175, 165, 180, 173]
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

df.drop("height", axis=1, inplace=True)
"""
    name  age
0   Jack   24
1  Sarah   30
2   Mike   21
3  David   29
"""
print(df)
