import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Tom", "Jerry", "Mickey", "Minnie", "Donald"],
    "Age": [25, 23, 28, 27, 26],
    "Score": [80, 90, 75, 85, 95]
}

df = pd.DataFrame(data)

print(df)

df.plot(kind="bar", x="Name", y="Score")
plt.show()