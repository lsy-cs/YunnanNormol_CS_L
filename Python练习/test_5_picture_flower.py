import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
r = 3
alpha_1 = np.arange(0, 2 * np.pi, 0.01)

x1 = r * np.cos(4 * alpha_1) * np.cos(alpha_1)
y1 = r * np.cos(4 * alpha_1) * np.sin(alpha_1)


alpha_2 = np.arange(0, 2 * np.pi, 0.1)

x2 = r * np.cos(4 * alpha_2) * np.cos(alpha_2)
y2 = r * np.cos(4 * alpha_2) * np.sin(alpha_2)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x1, y1, color='tab:blue')
plt.title('图 3.4 玫瑰线图案 (步长0.01)')
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.plot(x2, y2, color='tab:blue')
plt.title('图 3.5 步长增大的玫瑰线图案 (步长0.1)')
plt.axis('equal')


plt.tight_layout()
plt.show()
