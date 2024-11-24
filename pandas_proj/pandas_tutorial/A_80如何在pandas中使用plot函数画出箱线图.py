import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "A": np.random.normal(0, 1, 5),
    "B": np.random.normal(2, 1, 5),
    "C": np.random.normal(3, 2, 5),
}

df = pd.DataFrame(data)
"""
          A         B         C
0  0.135716  2.652092  5.042439
1  0.586916  0.987911 -0.372162
2 -0.600845  2.313044  2.285626
3 -1.058028  2.483956  1.418614
4  2.306229  2.499044 -0.074388
"""
print(df)

df.plot.box()

plt.show()