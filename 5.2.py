#5.2 generating a subplot layout with various plot types (scatter,line,bar)
import matplotlib.pyplot as plt
import numpy as np
#data
x=np.linspace(0,10,90)
y=np.sin(x)
#creating subplots (2 rows, 2 columns)
fig,axs=plt.subplots(2,2,figsize=(10,10))
#line plot
axs[0,0].plot(x,y,color='orange')
axs[0,0].set_title('Line Plot')
#scatter plot
axs[0,1].scatter(x,y,color='blue')
axs[0,1].set_title('Scatter Plot')
#bar plot
axs[1,0].bar(x,y,color='green')
axs[1,0].set_title('Bar Plot')
#histogram
data=np.random.randn(1000)
axs[1,1].hist(data,bins=30,color='red',edgecolor='black')
axs[1,1].set_title('Histogram')
plt.tight_layout()
plt.show()
