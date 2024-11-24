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

df.to_json("../../data/data.json", orient="records")
df.to_json("../../data/data_split.json", orient="split")

df.to_json("../../data/data_tables.json", orient="table")
df.to_json("../../data/data_index.json", orient="index")
df.to_json("../../data/data_values.json", orient="values")