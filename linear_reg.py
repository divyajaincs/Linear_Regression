from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
x=np.array([112,154,245,269,298,303,347,387,400,450,560])
y=np.array([1100,1140,1200,1245,1300,1400,1450,1480,1550,1600,1640])
slope,intercept,r_values,p_values,std_err=stats.linregress(x,y)
plt.plot(x,y,'ro',color='black')
plt.xlabel('size of houses')
plt.ylabel('prices')
plt.axis([0,600,0,1700])
plt.plot(x,x*slope+intercept,'b')
plt.plot()
plt.show()
nx=250
ny=nx*slope+intercept
print(ny)

