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

df.interpolate(method="linear", inplace=True)
"""
     A    B
0  1.0  1.0
1  2.0  2.0
2  3.0  3.0
3  4.0  4.0
4  5.0  5.0
"""
print(df)
