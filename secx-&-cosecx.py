import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.1) 

y = 1 / np.cos(x)
z = 1 / np.sin(x)

plt.plot(x,y,x,z)
plt.title("Sec(x) & Cosec(x) plot")
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sec(x) and cosec(x)')
plt.legend(['sec(x)', 'cosec(x)'])
plt.xlim(0,4*np.pi)
plt.ylim(-10,10)

plt.show()
