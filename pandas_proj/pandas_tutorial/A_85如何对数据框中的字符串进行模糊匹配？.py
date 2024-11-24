import pandas as pd

data = {
    "Name": ["Tom", "Tom", "Mary", "Mary", "Jackie", "Jackie"],
    "Subject": ["Math", "English", "Math", "English", "Math", "English"],
    "Score": [80, 70, 85, 75, 90, 95]
}

df = pd.DataFrame(data)

matched_rows=df["Name"].str.contains("o|e")

result = df[matched_rows]
"""
     Name  Subject  Score
0     Tom     Math     80
1     Tom  English     70
4  Jackie     Math     90
5  Jackie  English     95
"""
print(result)