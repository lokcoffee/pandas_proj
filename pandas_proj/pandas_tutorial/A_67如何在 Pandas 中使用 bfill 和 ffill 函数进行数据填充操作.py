import pandas as pd
import numpy as np

data = {

    "A": [1, 2, np.nan, 4, 5],
    "B": [1, 2, 3, np.nan, 5]
}

df = pd.DataFrame(data)
"""
     A    B
0  1.0  1.0
1  2.0  2.0
2  NaN  3.0
3  4.0  NaN
4  5.0  5.0
"""
print(df)

df_bfill = df.bfill()
"""
     A    B
0  1.0  1.0
1  2.0  2.0
2  4.0  3.0
3  4.0  5.0
4  5.0  5.0
"""
print(df_bfill)

df_fill = df.ffill()
"""
     A    B
0  1.0  1.0
1  2.0  2.0
2  2.0  3.0
3  4.0  3.0
4  5.0  5.0
"""
print(df_fill)