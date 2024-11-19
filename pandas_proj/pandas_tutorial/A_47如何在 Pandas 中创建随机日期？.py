import pandas as pd
import numpy as np

start_date = "2020-01-01"
end_date = "2020-12-31"

date_range = pd.date_range(start=start_date, end=end_date, freq='D')
"""
DatetimeIndex(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04',
               '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08',
               '2020-01-09', '2020-01-10',
               ...
               '2020-12-22', '2020-12-23', '2020-12-24', '2020-12-25',
               '2020-12-26', '2020-12-27', '2020-12-28', '2020-12-29',
               '2020-12-30', '2020-12-31'],
              dtype='datetime64[ns]', length=366, freq='D')
"""
print(date_range)

sampled_dates = pd.Series(np.random.choice(date_range, size=10))
"""
0   2020-01-10
1   2020-08-16
2   2020-01-09
3   2020-04-03
4   2020-09-26
5   2020-06-09
6   2020-05-19
7   2020-02-07
8   2020-09-15
9   2020-01-07
dtype: datetime64[ns]
"""
print(sampled_dates)