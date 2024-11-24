import pandas as pd

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df = pd.Series(data)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
print(data)

bins=[0, 3, 6, 10]

labels = ["low", "mid", "high"]
data_cut = pd.cut(data, bins=bins, labels=labels)

"""
['low', 'low', 'low', 'mid', 'mid', 'mid', 'high', 'high', 'high', 'high']
Categories (3, object): ['low' < 'mid' < 'high']
"""
print(data_cut)