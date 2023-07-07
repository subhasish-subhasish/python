import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.1)
y=np.sin(x)/np.cos(x)
z=np.cos(x)/np.sin(x)

plt.plot(x,y,x,z)
plt.title("Tan(x) & Cot(x) plot")
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('tan(x) and cot(x)')
plt.legend(['tan(x)', 'cot(x)'])
plt.xlim(0,4*np.pi)
plt.ylim(-10,10)

plt.show()