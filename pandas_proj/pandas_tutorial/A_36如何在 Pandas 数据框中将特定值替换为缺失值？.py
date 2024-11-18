import pandas as pd

data = {
    "A": [1, 2, 3, 4, 5],
    "B": ["a", "b", "c", "d", "e"],
    "C": [0, 1, 2, 3, 4]
}
df = pd.DataFrame(data)
"""
   A  B  C
0  1  a  0
1  2  b  1
2  3  c  2
3  4  d  3
4  5  e  4
"""
print(df)

df=df.replace(3, pd.NaT)
"""
     A  B    C
0    1  a    0
1    2  b    1
2  NaT  c    2
3    4  d  NaT
4    5  e    4
"""
print(df)

