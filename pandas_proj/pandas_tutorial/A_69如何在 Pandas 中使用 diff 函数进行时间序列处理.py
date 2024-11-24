import pandas as pd
import numpy as np

data = {
    "2020-01-01"
}

dates = pd.date_range("2023-01-01", periods=5)
ts = pd.Series(np.random.randn(len(dates)), dates)

"""
2023-01-01    1.198593
2023-01-02    0.020522
2023-01-03   -0.644288
2023-01-04    2.373533
2023-01-05   -1.003429
Freq: D, dtype: float64
"""
print(ts)

diff_ts=ts.diff()
"""
2023-01-01         NaN
2023-01-02   -1.178071
2023-01-03   -0.664810
2023-01-04    3.017821
2023-01-05   -3.376962
Freq: D, dtype: float64
"""
print(diff_ts)

diff2_ts = ts.diff().diff()
"""
2023-01-01         NaN
2023-01-02         NaN
2023-01-03    0.513261
2023-01-04    3.682631
2023-01-05   -6.394783
Freq: D, dtype: float64
"""
print(diff2_ts)



# CANT understand