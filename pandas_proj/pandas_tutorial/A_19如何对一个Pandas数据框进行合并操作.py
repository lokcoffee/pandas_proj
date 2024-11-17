
import pandas as pd


pd.set_option("display.unicode.east_asian_width", True)

df1 = pd.DataFrame({
    "编号":["mr001", "mr002", "mr003"],
    "语文":[110, 105, 109],
    "数学":[101, 89, 129],
    "英语":[99, 115, 139],
})

df2 = pd.DataFrame({
    "编号":["mr001", "mr002", "mr003", "mr004"],
    "物理":[104.5, 117, 98, 141],
})

df_merge = pd.merge(df1, df2, on="编号", how="left")
"""
    编号  语文  数学  英语   物理
0  mr001   110   101    99  104.5
1  mr002   105    89   115  117.0
2  mr003   109   129   139   98.0
"""
print(df_merge)

concat_df = pd.concat([df1, df2], axis=0)

"""
0  mr001    NaN    NaN    NaN  104.5
1  mr002    NaN    NaN    NaN  117.0
2  mr003    NaN    NaN    NaN   98.0
3  mr004    NaN    NaN    NaN  141.0
"""
print(concat_df)