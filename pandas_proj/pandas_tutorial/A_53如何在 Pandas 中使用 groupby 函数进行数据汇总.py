from itertools import groupby

import pandas as pd

data = {
    "Year": [2018, 2018, 2019, 2019, 2020, 2020],
    "Month": [1, 2, 1, 2, 1, 2],
    "Sales": [100, 200, 300, 400, 500, 600]
}


df = pd.DataFrame(data)

"""
   Year  Month  Sales
0  2018      1    100
1  2018      2    200
2  2019      1    300
3  2019      2    400
4  2020      1    500
5  2020      2    600
"""
print(df)


grpby=df.groupby(["Year", "Month"])
result = grpby.sum()
"""
            Sales
Year Month       
2018 1        100
     2        200
2019 1        300
     2        400
2020 1        500
     2        600
"""
print(result)