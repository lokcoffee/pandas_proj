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

df["weight_score"] = 0.4 * df["Score"] + 0.6 * 100
"""
   Name  Subject  Score  weight_score
0   Tom     Math     80          92.0
1   Tom  English     70          88.0
2  Mary     Math     85          94.0
3  Mary  English     75          90.0
4  Jack     Math     90          96.0
5  Jack  English     95          98.0
"""
print(df)

df["new_column_name"]="weight_score"
"""
   Name  Subject  Score  weight_score new_column_name
0   Tom     Math     80          92.0    weight_score
1   Tom  English     70          88.0    weight_score
2  Mary     Math     85          94.0    weight_score
3  Mary  English     75          90.0    weight_score
4  Jack     Math     90          96.0    weight_score
5  Jack  English     95          98.0    weight_score
"""
print(df)