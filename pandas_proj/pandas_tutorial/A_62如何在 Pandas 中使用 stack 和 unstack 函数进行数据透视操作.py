import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Year": [2018, 2019, 2020],
    "Sales": [100, 200, 300]
}
df = pd.DataFrame(data)

"""
      Name  Year  Sales
0    Alice  2018    100
1      Bob  2019    200
2  Charlie  2020    300
"""
print(df)

df.set_index("Year", inplace=True)
"""
         Name  Sales
Year                
2018    Alice    100
2019      Bob    200
2020  Charlie    300
"""
print(df)

stacked =df.stack()
"""
Year       
2018  Name       Alice
      Sales        100
2019  Name         Bob
      Sales        200
2020  Name     Charlie
      Sales        300
dtype: object
"""
print(stacked)

unstacked = stacked.unstack()
"""
         Name Sales
Year               
2018    Alice   100
2019      Bob   200
2020  Charlie   300
"""
print(unstacked)