import pandas as pd

data = {
    "Name": ["Tom", "Mary", "Jack", "Tom", "Mary"],
    "Gender": ["M", "F", "M", "M", "F"]
}

df = pd.DataFrame(data)
"""
   Name Gender
0   Tom      M
1  Mary      F
2  Jack      M
3   Tom      M
4  Mary      F
"""
print(df)

factorized, _ = pd.factorize(df["Gender"])
df["Gender_Factor"] = factorized
"""
   Name Gender  Gender_Factor
0   Tom      M              0
1  Mary      F              1
2  Jack      M              0
3   Tom      M              0
4  Mary      F              1
"""
print(df)

