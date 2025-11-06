#5.1
import matplotlib.pyplot as plt
import numpy as np
x=np.array([10,20,30,40,50])
y=np.array([20,30,40,50,60])
#line plot
plt.plot(x,y)
plt.title('Line Plot')
plt.show()
#scatter plot
plt.scatter(x,y)
plt.title('Scatter Plot')
plt.show()
#bar plot
x=np.array(['A','B','C','D','E'])
y=np.array([0,1,4,9,16])
plt.bar(x,y,color='yellow',edgecolor='lightgreen')
plt.title('Bar Plot')
plt.xlabel('category')
plt.ylabel('value')
plt.show()
