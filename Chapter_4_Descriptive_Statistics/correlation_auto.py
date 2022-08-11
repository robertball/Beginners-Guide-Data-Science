import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import webbrowser, os

font = {'size' :10}
matplotlib.rc('font', **font)


path = 'auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None, names = ['mpg', 'cylinders', 'displacement','horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'], na_values='?')

#mpg_data.info()

# plot correlated values using charts:
#plt.rcParams['figure.figsize'] = [16, 6]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))

#ax=ax.flatten()

colors=['#f35134', '#243AB5', '#243AB5']
j=0

ax.set_ylabel('Miles per Gallon (MPG)')
ax.scatter(mpg_data['horsepower'], mpg_data['mpg'],  alpha=0.5, color=colors[j])
ax.set_xlabel('Horsepower (hp)')
ax.set_title('Example Exponential Distribution')
#ax.set_ylim(bottom=0)

#plt.show()
plt.savefig('Ball-Rague-Fig4.14.eps', bbox_inches='tight')

