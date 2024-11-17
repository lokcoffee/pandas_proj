# 10 如何查看一个Pandas数据框的数据摘要统计信息？

import pandas as pd
df = pd.DataFrame({"A":[1,2,3,4,5],
                   "B":[2.1, 4.2, 6.3, 8.4, 10.5],
                   "C":["a", "b", "a", "b", "a"]
})

"""
   A     B  C
0  1   2.1  a
1  2   4.2  b
2  3   6.3  a
3  4   8.4  b
4  5  10.5  a
"""

print(df)

suf = df.describe()
"""
              A          B
count  5.000000   5.000000
mean   3.000000   6.300000
std    1.581139   3.320392
min    1.000000   2.100000
25%    2.000000   4.200000
50%    3.000000   6.300000
75%    4.000000   8.400000
max    5.000000  10.500000
"""
print(suf)