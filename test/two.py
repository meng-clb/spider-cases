import numpy as np
import pylab as pl

x = np.arange(0, 2 * np.pi, 0.1)
y = np.cos(x)
pl.scatter(x, y)
pl.xlabel("x")
pl.ylabel("y")
pl.title("sin")
pl.show()
