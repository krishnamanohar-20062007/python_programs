#5.4 Create a 3D plot.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
z=np.linspace(0,1,100)
x=z*np.sin(20*z)
y=z*np.cos(20*z)
ax.plot3D(x,y,z,color='blue')
ax.set_title('3D Plot')
plt.show()
