import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = x**2
fig = plt.figure(figsize=(6,4))

plt.plot(x,y, 'r')

x = [-5,-4,-4.1,-3,-2,-2.2,-1,0,1,2,3,4,5,5.1,4.9,4.8,4.6,.1]
y = [25,18,16  ,9 , 6,4, 1,1,3,4,9,15,21,22,24,25.5,20,-.5]

plt.scatter(x,y)

#plt.axis('off')

#plt.show()
plt.savefig('Ball-Rague-Fig4.19.eps', bbox_inches='tight')

