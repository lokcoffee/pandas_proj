import pandas as pd

from sklearn.preprocessing import StandardScaler

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


scaler=StandardScaler().fit(df)
df_std=scaler.transform(df)
"""
[[-1.41421356 -1.41421356 -1.41421356]
 [-0.70710678 -0.70710678 -0.70710678]
 [ 0.          0.          0.        ]
 [ 0.70710678  0.70710678  0.70710678]
 [ 1.41421356  1.41421356  1.41421356]]
"""
print(df_std)


### CANT understand
