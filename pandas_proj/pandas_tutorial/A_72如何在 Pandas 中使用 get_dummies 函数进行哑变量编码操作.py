import pandas as pd

data = {
    "color": ["red", "blue", "green", "red", "blue"]
}

df = pd.DataFrame(data)

print(df)

dummies = pd.get_dummies(df["color"])

df = pd.concat([df, dummies], axis=1)
"""
   color   blue  green    red
0    red  False  False   True
1   blue   True  False  False
2  green  False   True  False
3    red  False  False   True
4   blue   True  False  False
"""
print(df)