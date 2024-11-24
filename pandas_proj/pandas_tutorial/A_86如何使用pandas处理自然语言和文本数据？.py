import pandas as pd

"""
lower()/upper()
strip()
split()
contains()
replace()
extract()
"""

data = pd.read_csv("../../data/中国大学综合排名.csv")

print(data)

data["英文名称"] = data["英文名称"].str.lower()

print(data)

result = data["省市"].str.contains("北京")

print(result)