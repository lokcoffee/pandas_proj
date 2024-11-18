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

grpby=df.groupby(["Name", "Subject"]).mean()
"""
              Score
Name Subject       
Jack English   95.0
     Math      90.0
Mary English   75.0
     Math      85.0
Tom  English   70.0
     Math      80.0
"""
print(grpby)


