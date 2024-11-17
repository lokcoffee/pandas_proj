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


df.set_index("name", inplace=True)
"""
       age  height
name              
Jack    24     175
Sarah   30     165
Mike    21     180
David   29     173
"""
print(df)


new_df = df.loc["Sarah": "David"]
"""
       age  height
name              
Sarah   30     165
Mike    21     180
David   29     173
"""
print(new_df)