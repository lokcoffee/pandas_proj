import pandas as pd

data = {
    "name":["Alice", "Bob", "Charlie", "David"],
    "gender": ["F", "M", "F", "M"]
}

df = pd.DataFrame(data)

"""
      name gender
0    Alice      F
1      Bob      M
2  Charlie      F
3    David      M
"""
print(df)

mapping = {"M":0,'F':1}

df["gender"]=df["gender"].map(mapping)
"""
      name  gender
0    Alice       1
1      Bob       0
2  Charlie       1
3    David       0
"""
print(df)
"""
0    1
1    0
2    1
3    0
"""
print(df["gender"])