import pandas as pd

data = {
    "Name": ["Tom", "Tom", "Mary", "Mary", "Jack", "Jack"],
    "Subject": ["Math", "English", "Math", "English", "Math", "English"],
    "Score": [80, 70, 85, 75, 90, 95]
}
df = pd.DataFrame(data)
"""
   Name  Subject  Score
0   Tom     Math     80
1   Tom  English     70
2  Mary     Math     85
3  Mary  English     75
4  Jack     Math     90
5  Jack  English     95
"""
print(df)


pivot=df.pivot(index="Name", columns="Subject", values="Score")
"""
Subject  English  Math
Name                  
Jack          95    90
Mary          75    85
Tom           70    80
"""
print(pivot)