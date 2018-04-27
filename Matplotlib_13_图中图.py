import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6]
y = [2, 3, 4, 5, 6, 7]
# 创建最大的那张图
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

# 创建一张小图....方法一
ax2 = fig.add_axes([0.2, 0.6, 0.2, 0.2])
ax2.plot(x, y, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title2')
# 方法二
plt.axes([0.6, 0.2, 0.2, 0.2])
plt.plot(y, x, 'g')
plt.xlabel('xx')
plt.ylabel('yy')
plt.title('666')


plt.show()


