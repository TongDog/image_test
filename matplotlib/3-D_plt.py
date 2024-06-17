# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



fig = plt.figure()
ax = Axes3D(fig)

X  = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
# print(X,Y)
R = np.sqrt(X**2+Y**2)

Z = np.sin(R)

# rstride:横向分割颜色的跨度
# cstride:纵向
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))

# 投影，zdir='z'指从z轴压下去，投影到xOy轴
# ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2,2)

plt.show()
# ax.imshow()