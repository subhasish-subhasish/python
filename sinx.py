import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,4*np.pi,0.1) 
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,x,z)
plt.title("Sin(x) & Cos(x) plot")
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.legend(['sin(x)', 'cos(x)'])
plt.xlim(0,4*np.pi)

plt.show()


