import pandas as pd
import numpy as np
data = {
    "A":[np.nan, 1, 3, 5],
    "B":["a", "b", np.nan, np.nan]
}

df = pd.DataFrame(data)
"""
A    1
B    2
dtype: int64
"""
print(df.isnull().sum())