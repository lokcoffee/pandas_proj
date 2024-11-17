import pandas as pd

df = pd.DataFrame({
    "Product": [
        "A", "B", "C",
        "A", "B", "C",
        "A", "B", "C"],
    "SalesDate": [
        "2022-01-01", "2022-01-01", "2022-01-01",
        "2022-01-02", "2022-01-02", "2022-01-02",
        "2022-01-03", "2022-01-03", "2022-01-03"
    ],
    "SalesAmount": [
        100, 200, 150, 50, 75, 125, 300, 250, 200
    ]
})

"""
  Product   SalesDate  SalesAmount
0       A  2022-01-01          100
1       B  2022-01-01          200
2       C  2022-01-01          150
3       A  2022-01-02           50
4       B  2022-01-02           75
5       C  2022-01-02          125
6       A  2022-01-03          300
7       B  2022-01-03          250
8       C  2022-01-03          200
"""
print(df)

df_pivot = df.pivot_table(index="Product", columns="SalesDate", values="SalesAmount", aggfunc="sum")
"""
SalesDate  2022-01-01  2022-01-02  2022-01-03
Product                                      
A                 100          50         300
B                 200          75         250
C                 150         125         200
"""
print(df_pivot)