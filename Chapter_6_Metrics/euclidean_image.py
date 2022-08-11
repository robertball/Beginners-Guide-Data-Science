import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.axis('off')
plt.axis('scaled')

plt.plot([0, 6.6], [6.6, 6.6], linestyle='dashed', c='black')
plt.plot([0, 6.6], [3.3, 3.3], linestyle='dashed', c='black')
plt.plot([6.6, 6.6], [0.0, 6.6], linestyle='dashed', c='black')
plt.plot([3.3, 3.3], [0.0, 3.3], linestyle='dashed', c='black')
# print('hi')

plt.ylim([-2, 10])  # set scale
plt.xlim([-2, 10])  # set scale

ax.annotate('', xytext=(0.0, -1.0), xy=(0.0, 10.0), arrowprops=dict(arrowstyle="->"))  # y-axis
ax.annotate('', xytext=(-1.0, 0.0), xy=(10.0, 0.0), arrowprops=dict(arrowstyle="->"))  # x-axis

ax.annotate('', xytext=(3.3, 3.3), xy=(6.55, 6.55), arrowprops=dict(arrowstyle="->"))
ax.annotate('$\it{p}$', xy=(3.20, 3.6))
ax.annotate('$\it{p_1}$', xy=(3.20, -0.55))
ax.annotate('$\it{p_2}$', xy=(-0.6, 3.20))
ax.annotate('$\it{q}$', xy=(6.45, 6.9))
ax.annotate('$\it{q_1}$', xy=(6.45, -0.5))
ax.annotate('$\it{q_2}$', xy=(-0.6, 6.6))
ax.annotate('$\it{(q_1 - p_1)}$', xy=(4.0, 2.7))
ax.annotate('$\it{(q_2 - p_2)}$', xy=(6.70, 5.0))

rectangle = plt.Rectangle((6.1, 3.3), 0.5, 0.5, facecolor='none', edgecolor='black')
plt.gca().add_patch(rectangle)

ax.annotate('$d(p,q)=\sqrt{(q_1-p_1)^2 + (q_2-p_2)^2}$', xy=(0.2, 8.5), fontsize=15)
#plt.show()
plt.style.use('plot_style.txt')
plt.savefig('Ball-Rague-Fig6.1.eps', bbox_inches='tight')

