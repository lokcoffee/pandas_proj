import pandas as pd

data = {
    "Name": ["Jack", "Sarah", "Mike", "David"],
    "Age": [24, 30, 21, 29],
    "Gender": ["M", "F", "M", "M"]
}

df = pd.DataFrame(data)
"""
    Name  Age Gender
0   Jack   24      M
1  Sarah   30      F
2   Mike   21      M
3  David   29      M
"""
print(df)

df_filtered=df.loc[df["Gender"] == "M"]
"""
    Name  Age Gender
0   Jack   24      M
2   Mike   21      M
3  David   29      M
"""
print(df_filtered)