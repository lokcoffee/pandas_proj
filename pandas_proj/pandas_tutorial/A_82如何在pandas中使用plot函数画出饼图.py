import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {

    "A": [1, 2, 3, 4],
    "B": [4, 3, 2, 1]
}

df = pd.DataFrame(data, index=["a", "b", "c", "d"])
"""
   A  B
a  1  4
b  2  3
c  3  2
d  4  1
"""
print(df)

df.plot(kind="pie", y="A")

plt.show()