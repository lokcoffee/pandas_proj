import pandas as pd
import matplotlib.pyplot as plt
"""
lower()/upper()
strip()
split()
contains()
replace()
extract()
"""

data = pd.read_csv("../../data/中国大学综合排名.csv")

print(data.describe())

plt.boxplot(data["升/降"])
plt.show()