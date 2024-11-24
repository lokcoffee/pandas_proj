import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

data = {
    "x": np.random.randint(1, 10, 10),
    "y": np.random.randint(1, 10, 10)
}

df = pd.DataFrame(data)

df.plot(kind="scatter", x="x", y="y")

print(df)
plt.show()