"""
to_uppercase()
to_lowercase()
strip()
replace()
contains()
startswith()
endswith()
"""

import pandas as pd

data = {
    "Name": ["Tom,Lee", "Mary,Smith", "Jack,Wang"],
    "Address": ["Beijing,China", "New York,USA", "Shanghai,China"]
}

df = pd.DataFrame(data)
"""
         Name         Address
0     Tom,Lee   Beijing,China
1  Mary,Smith    New York,USA
2   Jack,Wang  Shanghai,China
"""
print(df)


df[["First Name", "Last Name"]] = df["Name"].str.split(",", expand=True)
df[["City", "State"]] = df["Address"].str.split(",", expand=True)

"""
         Name         Address First Name Last Name      City  State
0     Tom,Lee   Beijing,China        Tom       Lee   Beijing  China
1  Mary,Smith    New York,USA       Mary     Smith  New York    USA
2   Jack,Wang  Shanghai,China       Jack      Wang  Shanghai  China
"""
print(df)