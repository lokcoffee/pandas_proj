import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("../../data/中国大学综合排名.xlsx")

print(data)

x = data["排名"]
y = data["国际竞争力"]

plt.plot(x, y)

# 设置字体
plt.rcParams["font.sans-serif"]="SimHei"
# 取消使用unicode符号
plt.rcParams["axes.unicode_minus"] = False
plt.title("排名与国际竞争力趋势图")
plt.xlabel("排名")
plt.ylabel("国际竞争力")

plt.show()
