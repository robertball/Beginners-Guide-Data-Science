import random
import matplotlib.pyplot as plt

x1 = []
y1 = []
y2 = []
random.seed(13)  # set seed to be able to recreate image

for i in range(100):
    x = random.randint(-40, 40)
    x1.append(x)
    y1.append(random.randint(-40, 40))
    y2.append(x + random.randint(-15, 15))

ax1 = plt.subplot(121, aspect=1)
ax1.scatter(x1, y1)
ax1.set_title('Completely Random')

ax2 = plt.subplot(122, aspect=1)
ax2.scatter(x1, y2)
ax2.set_title('Pattern')

#plt.show()
plt.savefig('Ball-Rague-Fig8.10.eps', bbox_inches='tight')

