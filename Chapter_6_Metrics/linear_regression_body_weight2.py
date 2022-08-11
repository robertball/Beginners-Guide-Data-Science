import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error

weight = [204.4, 204.8, 203.4, 203.2, 203.2, 203.0, 202.8, 202.0, 202.2, 200.2, 202.2, 202.4, 202.2, 200.6, 200.4, 200.6, 200.8, 200.8, 199.2, 199.6, 200.0, 198.8, 199.2, 200.8, 198.4, 201.0, 199.4, 200, 199.8, 199, 199.8, 198.6, 199.4, 197.6, 198.6, 198.2, 198.8, 196.8, 198.8, 198.6, 197.6, 198.4, 198.4, 197.8, 196.6, 197, 196.2, 199.2, 197.8, 197.2, 196.4, 196.6, 197.6, 196, 198.6, 196.2, 198, 195.8, 195.8, 197.2, 196.2, 195.6]
index = [x for x in range(len(weight))]

fit = np.polyfit(index, weight, 1)
fit_fn_1 = np.poly1d(fit) 

fit = np.polyfit(index, weight, 2)
fit_fn_2 = np.poly1d(fit) 

fit = np.polyfit(index, weight, 3)
fit_fn_3 = np.poly1d(fit) 

fit = np.polyfit(index, weight, 4)
fit_fn_4 = np.poly1d(fit) 

# create a grid of four plots
fig, axs = plt.subplots(2, 2)

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

axs[0,0].plot(index, weight, 'ro-')
axs[0,0].plot(fit_fn_1(index), '--k')
axs[0,0].set(xlabel='Day on diet', ylabel='Weight (lbs.)')
axs[0,0].set_title('1-degree polynomial')
axs[0,0].text(0.6, 0.95, 'MSE=%.4s'%mean_squared_error(weight, fit_fn_1(index)), transform=axs[0,0].transAxes, fontsize=14, verticalalignment='top', bbox=props)

axs[0,1].plot(index, weight, 'ro-')
axs[0,1].plot(fit_fn_2(index), '--k')
axs[0,1].set(xlabel='Day on diet', ylabel='Weight (lbs.)')
axs[0,1].set_title('2-degree polynomial')
axs[0,1].text(0.6, 0.95, 'MSE=%.4s'%mean_squared_error(weight, fit_fn_2(index)), transform=axs[0,1].transAxes, fontsize=14, verticalalignment='top', bbox=props)

axs[1,0].plot(index, weight, 'ro-')
axs[1,0].plot(fit_fn_3(index), '--k')
axs[1,0].set(xlabel='Day on diet', ylabel='Weight (lbs.)')
axs[1,0].set_title('3-degree polynomial')
axs[1,0].text(0.6, 0.95, 'MSE=%.4s'%mean_squared_error(weight, fit_fn_3(index)), transform=axs[1,0].transAxes, fontsize=14, verticalalignment='top', bbox=props)

axs[1,1].plot(index, weight, 'ro-')
axs[1,1].plot(fit_fn_4(index), '--k')
axs[1,1].set(xlabel='Day on diet', ylabel='Weight (lbs.)')
axs[1,1].set_title('4-degree polynomial')
axs[1,1].text(0.6, 0.95, 'MSE=%.4s'%mean_squared_error(weight, fit_fn_4(index)), transform=axs[1,1].transAxes, fontsize=14, verticalalignment='top', bbox=props)

fig.suptitle('Body Weight Fluctuations During a Diet')
plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.35, 
                    hspace=0.35)
import matplotlib
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 6)
#plt.rcParams['text.usetex'] = True
#plt.rc('font', size=7) #controls default text size
#plt.show()
#plt.style.use('plot_style.txt')
plt.savefig('Ball-Rague-Fig6.6.eps', bbox_inches='tight')

