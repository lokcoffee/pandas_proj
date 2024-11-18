import pandas as pd
import numpy as np

data = {
    "A": [1, 2, np.nan, 4],
    "B": [5, np.nan, 7, 8]
}
df = pd.DataFrame(data)
"""
     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  8.0
"""
print(df)


df.fillna(value=0, inplace=True)
"""
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  8.0
"""
print(df)

df = pd.DataFrame(data)
df.ffill(inplace=True)
"""
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  8.0
"""
print(df)

df = pd.DataFrame(data)
df.bfill(inplace=True)
"""
     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  8.0
"""
print(df)