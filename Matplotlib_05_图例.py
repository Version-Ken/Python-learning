import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x**2 + 1
y2 = x*2 + 1

plt.figure()

# 设置显示坐标轴的范围
plt.xlim((-2, 2))
plt.ylim((-2, 8))

plt.xlabel('This is x')
plt.ylabel('This is y')

l2, = plt.plot(x, y2, color='red', linestyle='--', linewidth=2.0, label='y2')
l1, = plt.plot(x, y1, label='y1')
plt.legend(handles=[l1, l2, ], labels=['aaa', 'bbb'], loc='best')
plt.show()
