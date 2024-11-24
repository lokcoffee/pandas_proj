import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(1000))
"""
0      0.138941
1      0.296109
2      0.433736
3     -0.459152
4      0.464535
         ...   
995   -0.567177
996   -2.567216
997   -1.148048
998   -0.070019
999    0.996750
Length: 1000, dtype: float64
"""
print(data)

bins = pd.qcut(data, q=4, labels=["bad", "average", "good", "excellent"])
"""
bad          250
average      250
good         250
excellent    250
Name: count, dtype: int64
"""
print(bins.value_counts())