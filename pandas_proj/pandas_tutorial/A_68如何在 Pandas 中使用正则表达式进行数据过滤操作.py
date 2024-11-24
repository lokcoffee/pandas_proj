import pandas as pd

data = {
    "Name": ["Alex", "Bob", "Charlie", "David", "emily"],
    "Age": [25, 30, 35, 40, 45],
    "Email": ["alex@gmail.com", "bob@yahoo.com", "charlie@hotmail.com", "david@gmail.com", "emily@hotmail.com"]
}

df = pd.DataFrame(data)

"""
      Name  Age                Email
0     Alex   25       alex@gmail.com
1      Bob   30        bob@yahoo.com
2  Charlie   35  charlie@hotmail.com
3    David   40      david@gmail.com
4    emily   45    emily@hotmail.com
"""
print(df)

data_1 = df[df["Email"].str.contains("gmail")]
"""
    Name  Age            Email
0   Alex   25   alex@gmail.com
3  David   40  david@gmail.com
"""
print(data_1)

data_2 = df[df["Email"].str.contains("gmail|hotmail", case=False)]
"""
      Name  Age                Email
0     Alex   25       alex@gmail.com
2  Charlie   35  charlie@hotmail.com
3    David   40      david@gmail.com
4    emily   45    emily@hotmail.com
"""
print(data_2)
