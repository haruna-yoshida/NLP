import matplotlib
import numpy as np
import matplotlib.pyplot as plt
print(matplotlib.rcParams['font.family'])

s = np.sin(np.pi*np.arange(0.0, 10.0, 0.05))
t = plt.plot(s, color="r")
plt.title("TESTグラフ")
plt.show()