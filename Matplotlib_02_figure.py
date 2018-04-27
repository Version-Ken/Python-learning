import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = x ** 2 + 1
y2 = x * 2 + 1

plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(5, 5), facecolor="blue")
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=2.0, linestyle='--')

plt.show()