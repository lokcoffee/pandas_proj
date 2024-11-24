import pandas as pd

data = {
    "Sex": ["M", "M", "F", "F", "M"],
    "Age": [23, 24, 22, 21, 23],
    "City": ["Beijing", "Shanghai", "Beijing", "Shanghai", "Beijing"],
    "Salary": [5000, 5500, 4500, 6000, 4800]
}
df = pd.DataFrame(data)

"""
  Sex  Age      City  Salary
0   M   23   Beijing    5000
1   M   24  Shanghai    5500
2   F   22   Beijing    4500
3   F   21  Shanghai    6000
4   M   23   Beijing    4800
"""
print(df)

result = pd.crosstab(index=df["Sex"], columns=df["City"], values=df["Salary"], aggfunc="mean")
"""
City  Beijing  Shanghai
Sex                    
F      4500.0    6000.0
M      4900.0    5500.0
"""
print(result)
