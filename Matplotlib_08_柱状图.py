import matplotlib.pyplot as plt
import numpy as np

# 产生 0 1 2 3 4 5 6 7 8 9 十个数
X = np.arange(1, 10)
Y1 = X
Y2 = X

plt.bar(X, Y1, facecolor='#9999ff', edgecolor='white')
# 负号代表下降
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 显示数据
for x, y in zip(X, Y1):
    plt.text(x - 0.1, y + 0.2, '%d' % y)

for x, y in zip(X, Y2):
    plt.text(x - 0.1, -y - 0.85, '%d' % -y)

plt.show()
