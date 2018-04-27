import matplotlib.pyplot as plt
import numpy as np

n = 1024
# 生成随机数
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)

# for color value颜色的公式
T = np.arctan2(Y, X)

# 写入绘制散点图的参数
plt.scatter(X, Y, c=T, s=75, alpha=0.5)

# 设置查看坐标范围大小
plt.xlim((-3, 3))
plt.ylim((-3, 3))

# 去除边框的刻度,就是参数设置为空
plt.xticks(())
plt.yticks(())

plt.show()

