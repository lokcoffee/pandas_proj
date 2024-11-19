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


table=pd.pivot_table(df, values="Sales", index="Year", columns="Month", aggfunc="sum")
"""
Month    1    2
Year           
2018   100  200
2019   300  400
2020   500  600

"""
print(table)