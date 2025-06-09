import numpy as np
import pylab as pl

x = np.random.random(50)
y = np.random.random(50)
pl.scatter(x, y, s=x * 100, c='r', marker='*')
pl.show()
