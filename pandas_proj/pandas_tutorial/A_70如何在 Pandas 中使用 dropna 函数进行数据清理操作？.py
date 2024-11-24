import pandas as pd
import numpy as np

data = {
    "Name": ["Alex", np.nan, "Charlie", "David", "emily"],
    "Age": [25, 30, 35, 40, np.nan],
    "Email": ["alex@gmail.com", np.nan, "charlie@hotmail.com", "david@gmail.com", "emily@hotmail.com"]
}

df = pd.DataFrame(data)
"""
      Name  Age                Email
0     Alex   25       alex@gmail.com
1      NaN   30                  NaN
2  Charlie   35  charlie@hotmail.com
3    David   40      david@gmail.com
4    emily   45    emily@hotmail.com
"""
print(df)

df.dropna(axis="index", how="any", inplace=True)
"""
      Name   Age                Email
0     Alex  25.0       alex@gmail.com
2  Charlie  35.0  charlie@hotmail.com
3    David  40.0      david@gmail.com
"""
print(df)
