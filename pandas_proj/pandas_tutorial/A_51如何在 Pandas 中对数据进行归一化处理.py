import pandas as pd

from sklearn.preprocessing import MinMaxScaler

data = {
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

scaler = MinMaxScaler().fit(df)
df_non = scaler.transform(df)

"""
[[0.   0.   0.  ]
 [0.25 0.25 0.25]
 [0.5  0.5  0.5 ]
 [0.75 0.75 0.75]
 [1.   1.   1.  ]]
"""
print(df_non)

# cant understand