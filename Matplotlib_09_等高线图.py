import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)
# 做出等高线的图
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# 画出等高线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=0.5)

# 在等高线上标出数值
plt.clabel(C, inline=True, fontsize=10)

plt.show()

