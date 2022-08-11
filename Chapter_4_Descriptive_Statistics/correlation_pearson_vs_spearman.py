# The Spearman correlation evaluates the monotonic relationship between two continuous or ordinal variables.
# What is 'monotonic': https://en.wikipedia.org/wiki/Monotonic_function

# The Pearson correlation evaluates the linear relationship between two continuous variables. A relationship is linear when a change in one variable is associated with a proportional change in the other variable.


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from scipy.stats import norm
import numpy as np


list1 = [x for x in range(30)]
list1 = [x for x in range(30)]

list2 = [x+5 for x in list1]

df1 = pd.DataFrame(list(zip(list1, list2)), columns =['X', 'Y']) 

list3 = [1,5,7,10,11,12,12.1,12.2,12.3,12.4,12.5,12.5,12.5,12.5,12.5,12.5,12.5,12.5,12.5,12.75,13,15,18,21,27,30,35,40,50,65]

list4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,13.5,14,14.25,14.5,14.25,14,13.5,13,12,11,10,9,8,7,6,5,4]

#list5 = [1,3,1,2,4,8,10,12,9,10,11,12,13,16,15,14,18,20,20,16,16,21,22,23,20,21,25,26,3,2]
np.random.seed(4444)
list5 = norm.rvs(size=30)
list6 = norm.rvs(size=30) + .6 * list5
print('Len of list5 is %s' % len(list5))
print('Len of list6 is %s' % len(list6))

print(f'min(list5) = {min(list5)}')
print(f'list6 = {list6}')


df2 = pd.DataFrame(list(zip(list1, list3)), columns =['X', 'Y']) 

df3 = pd.DataFrame(list(zip(list1, list4)), columns =['X', 'Y']) 

df4 = pd.DataFrame(list(zip(list5, list6)), columns =['X', 'Y']) 


fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,6))
#fig2.set_size_inches(24, 8)
plt.subplots_adjust(wspace=0.2)


line = lines.Line2D([0, 30], [5, 35], lw=2, color='red')  # first list are the X's and the second list are the Y's
ax[0][0].add_line(line)
df1.plot(kind='scatter', x='X', y='Y', ax=ax[0][0], title='Pearson: %s' % df1.corr(method='pearson').iloc[0,1] + ' Spearman: %s' % df1.corr(method='spearman').iloc[0,1])

line = lines.Line2D([0, 29], [1, 65], lw=2, color='red')  # first list are the X's and the second list are the Y's
ax[0][1].add_line(line)
df2.plot(kind='scatter', x='X', y='Y', ax=ax[0][1], title='Pearson: %s' % df2.corr(method='pearson').iloc[0,1].round(2) + ' Spearman: %s' % df2.corr(method='spearman').iloc[0,1].round(2))

#ax[1][0].add_line(line)
#df3.plot(kind='scatter', x='X', y='Y', ax=ax[1][0], title='Pearson: %s' % df3.corr(method='pearson').iloc[0,1].round(2) + ' Spearman: %s' % df3.corr(method='spearman').iloc[0,1].round(2))

line = lines.Line2D([-1.6, 14], [-1.8, 13.9], lw=2, color='red')  # first list are the X's and the second list are the Y's
ax[1][1].add_line(line)
df4.plot(kind='scatter', x='X', y='Y', ax=ax[1][0], title='Pearson: %s' % df4.corr(method='pearson').iloc[0,1].round(2) + ' Spearman: %s' % df4.corr(method='spearman').iloc[0,1].round(2))

list5 = np.append(list5, [14])
list6 = np.append(list6, [14])
print('Len of list5 is %s' % len(list5))
print('Len of list6 is %s' % len(list6))

df5 = pd.DataFrame(list(zip(list5, list6)), columns =['X', 'Y']) 

line = lines.Line2D([-1.6, 14], [-1.8, 13.9], lw=2, color='red')  # first list are the X's and the second list are the Y's
ax[1][0].add_line(line)
df5.plot(kind='scatter', x='X', y='Y', ax=ax[1][1], title='Pearson: %s' % df5.corr(method='pearson').iloc[0,1].round(2) + ' Spearman: %s' % df5.corr(method='spearman').iloc[0,1].round(2))

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.15, 
                    hspace=0.35)

#plt.show()
plt.savefig('Ball-Rague-Fig4.18.eps', bbox_inches='tight')
