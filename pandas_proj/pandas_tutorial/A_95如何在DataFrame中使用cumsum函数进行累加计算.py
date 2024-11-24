import pandas as pd


data  = {
    "A": [1, 2, 3, 4, 5],
    "B": [100, 200, 300, 400, 500],
    "C": [1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(data)
"""
   A    B     C
0  1  100  1000
1  2  200  2000
2  3  300  3000
3  4  400  4000
4  5  500  5000
"""
print(df)

cumulative_sum=df.cumsum(axis=1)
"""
   A    B     C
0  1  101  1101
1  2  202  2202
2  3  303  3303
3  4  404  4404
4  5  505  5505
"""
print(cumulative_sum)

cumulative_sum=df.cumsum(axis=0)
"""
    A     B      C
0   1   100   1000
1   3   300   3000
2   6   600   6000
3  10  1000  10000
4  15  1500  15000
"""
print(cumulative_sum)