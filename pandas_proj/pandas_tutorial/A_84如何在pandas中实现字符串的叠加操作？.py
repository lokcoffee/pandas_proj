import pandas as pd

data = {

    "A": ["hello", "world"],
    "B": ["pandas", "numpy"]
}

df = pd.DataFrame(data)
"""
       A       B
0  hello  pandas
1  world   numpy
"""
print(df)

df["C"] = df["A"]+df["B"]
"""
       A       B            C
0  hello  pandas  hellopandas
1  world   numpy   worldnumpy
"""
print(df)