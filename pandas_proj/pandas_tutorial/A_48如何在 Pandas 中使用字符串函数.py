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
    "Name": ["Alex", "Bob", "Charlie", "David", "emily"],
    "City": ["AUSTIN", "HoUSTON", "DALLAS", "Austin", "houston"]
}

df = pd.DataFrame(data)
"""
      Name     City
0     Alex   AUSTIN
1      Bob  HoUSTON
2  Charlie   DALLAS
3    David   Austin
4    emily  houston
"""
print(df)

df["City"] = df["City"].str.strip().str.lower().str.replace("houston", "Houston")
"""
      Name     City
0     Alex   austin
1      Bob  Houston
2  Charlie   dallas
3    David   austin
4    emily  Houston
"""
print(df)