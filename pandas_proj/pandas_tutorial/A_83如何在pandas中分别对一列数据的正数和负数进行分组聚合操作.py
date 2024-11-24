import pandas as pd

data = {
    "values": [1, -2, 3, -4, 5]
}

df = pd.DataFrame(data)
"""
   values
0       1
1      -2
2       3
3      -4
4       5
"""
print(df)

df["positive"] = df["values"] > 0
df["negative"] = df["values"] < 0

result = df.groupby(["positive", "negative"]).agg({"values": "sum"})
"""
                   values
positive negative        
False    True          -6
True     False          9
"""
print(result)

