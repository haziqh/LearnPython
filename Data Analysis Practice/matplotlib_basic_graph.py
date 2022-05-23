import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.linspace(0,2*np.pi,100)
y = np.sin(x)
plt.plot(x,y)
plt.show()