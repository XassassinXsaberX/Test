import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure("1")
theta = np.linspace(-np.pi, np.pi, 200)
plt.plot(np.sin(theta), np.cos(theta))

fig = plt.figure("2")
plt.axis('equal')          # 使x軸、y軸間隔一致
plt.axis([-0.5,0.5,-1,1]) # 可以自己調整lim但不太有用...
plt.xlim(-0.5,0.5)        # 當你使用plt.axis的方法時，xlim、ylim都會失效
plt.plot(np.sin(theta), np.cos(theta))

fig = plt.figure("3")
plt.gca().set_aspect('equal', adjustable='box')   # 使x軸、y軸間隔一致
plt.xlim(-0.5,0.5)                               # 當你使用plt.axis的方法時，xlim、ylim都可使用
plt.plot(np.sin(theta), np.cos(theta))


plt.show()
