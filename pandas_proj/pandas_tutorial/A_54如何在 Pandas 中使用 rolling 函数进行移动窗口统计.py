import pandas as pd

import numpy as np

ser = pd.Series(np.random.randn(10))

"""
0   -0.200201
1   -1.326069
2    0.768766
3    0.264875
4   -1.481533
5    0.268241
6   -0.499389
7    0.120706
8   -2.131314
9   -1.381279
dtype: float64
"""
print(ser)

rolling_window=ser.rolling(window=3)
rolling_mean=rolling_window.mean()
"""
0         NaN
1         NaN
2   -0.252501
3   -0.097476
4   -0.149297
5   -0.316139
6   -0.570894
7   -0.036814
8   -0.836666
9   -1.130629
dtype: float64

"""
print(rolling_mean)

# cant understand