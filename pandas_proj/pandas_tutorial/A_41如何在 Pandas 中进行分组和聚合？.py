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

grpby=df.groupby(["Name"])["Score"].agg(["mean", "max", "min", "count"])
"""
      mean  max  min  count
Name                       
Jack  92.5   95   90      2
Mary  80.0   85   75      2
Tom   75.0   80   70      2
"""
print(grpby)