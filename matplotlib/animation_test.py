import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animation_func(i): #参数i为第i帧
    line.set_ydata(np.sin(x+i/10)) #把y轴的data更新为其他数据
    return line, #打逗号为了把返回值改为列表，即返回[line,None]

def init(): # 设置初始值
    line.set_ydata(np.sin(x)) #把y轴的data更新为其他数据
    return line,

# frames:动画重复次数
# init_func：动画最开始时的样子
# interval:隔多少毫秒更新一次
# blit：更新整张图(True)还是只更新变化了的图(False),Mac用blit必须为True，不然报错
ani = animation.FuncAnimation(fig=fig,func=animation_func,frames=100,init_func=init,interval=20,blit=False)
plt.show()