import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


plt.figure()
# 方法一
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
# ax1.plot([1, 2], [1, 2])
# ax1.set_title('ax1_title')
#
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
# ax2.set_title('ax2_title')
#
# ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
# ax3.set_title('ax3_title')
#
# ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
# ax4.set_title('ax4_title')
#
# ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
# ax5.set_title('ax5_title', loc="center")

# 方法二
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0, :])
ax2 = plt.subplot(gs[1, 0:2])
ax3 = plt.subplot(gs[1:3, 2:3])
ax4 = plt.subplot(gs[2, 0:1])
ax5 = plt.subplot(gs[2, 1:2])

plt.show()

