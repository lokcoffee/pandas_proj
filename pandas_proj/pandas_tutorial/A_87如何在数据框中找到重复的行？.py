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

drop_rows=data.duplicated()
drop_rows=data.duplicated(subset=["学校名称", "总分"])

print(drop_rows)
