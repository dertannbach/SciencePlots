import matplotlib.pyplot as plt
import numpy as np

# 多列堆叠柱状图
tick_label = ["A", "B", "C", "D"]
y = [67, 94, 46, 17]   # left, train
y1 = [48, 67, 37, 13]  # right, train
y2 = [33, 6, 2, 8]     # bilateral, train

y3 = [16, 23, 11, 4]   # left, validation
y4 = [10, 16, 9, 3]  # right, validation
y5 = [10, 2, 1, 2]     # bilateral, validation

y6 = [8, 11, 10, 1]   # left, test
y7 = [11, 10, 6, 7]  # right, test
y8 = [13, 0, 5, 3]     # bilateral, test

x = np.arange(4)
bar_width = 0.3  # 条形宽度
c1 = '#B3CDE0'
c2 = '#F1A7C1'
c3 = '#C1D9A0' # 颜色设置
plt.bar(x, y, bar_width, color=c1, label='x1')
plt.bar(x, y1, bar_width, bottom=y,  # 堆叠
        color=c2, label='x2', alpha=0.5)
plt.bar(x, y2, bar_width, bottom=[sum(x) for x in zip(y, y1)],
        color=c3, label='x3', alpha=0.5)

plt.bar(x + bar_width, y3, bar_width,  align="center", color=c1)
plt.bar(x + bar_width, y4, bar_width, bottom=y3,  # 堆叠
        color=c2, alpha=0.5)
plt.bar(x + bar_width, y5, bar_width, bottom=[sum(x) for x in zip(y3, y4)],
        color=c3, alpha=0.5)

plt.bar(x + 2 * bar_width, y6, bar_width,  align="center", color=c1)
plt.bar(x + 2 * bar_width, y7, bar_width, bottom=y6,  # 堆叠
        color=c2, alpha=0.5)
plt.bar(x + 2 * bar_width, y8, bar_width, bottom=[sum(x) for x in zip(y6, y7)],
        color=c3, alpha=0.5)

plt.xticks(x + bar_width / 2, tick_label)
plt.xlabel("Type", fontsize=15)
plt.ylabel("Number", fontsize=15)
plt.legend()
plt.show()

