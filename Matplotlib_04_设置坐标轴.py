import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)

plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# 设置x坐标和y坐标的值的范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# x轴和y轴的标签（不支持中文）
plt.xlabel("aaa")
plt.ylabel("bbb")

# 设置x轴的坐标为-1到2,分为4段
new_ticks = np.linspace(-1, 2, 4)
print(new_ticks)
plt.xticks(new_ticks)

# 是y坐标的刻度值对应与一个标签评价等级。。。
# 加了$使得字体变斜体
plt.yticks([-2, -1, 0, 1, 2],
           [r'$bad$', r'$normal$', r'$good:\alpha$', r'$very\ good$', 'very very good'])

# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()
