import numpy as np
import pylab as pl

labels = ["Frogs", "Hogs", "Dogs", "Logs"]
sizes = [10, 20, 25, 45]
colors = ["yellow", "red", "green", "black"]
explode = [0, 0.1, 0, 0.1]
fig = pl.figure()
ax = fig.gca()
# 以下绘制4个饼图，分别放置在4个不同角度
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, \
       autopct="1.1f%%", shadow=True, startangle=90, radius=0.25, center=[0.5, 0.5], frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, \
       autopct="%1.1f%%", shadow=True, startangle=90, radius=0.25, center=[0.5, 1.5], frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, \
       autopct="1,1f%%", shadow=True, startangle=90, radius=0.25, center=[1.5, 0.5], frame=True)
ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors, \
       autopct="1.1f%%", shadow=True, startangle=90, radius=0.25, center=[1.5, 1.5], frame=True)
ax.set_xticks([0, 2])
ax.set_yticks([0, 2])
ax.set_xticklabels(["0", "1"])
ax.set_yticklabels(["0", "1"])
ax.set_aspect("equal")
pl.show()
