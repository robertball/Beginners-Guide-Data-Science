import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

df = pd.read_csv('iris.csv')
print(df)
virginica = df[df['class'] == 'Iris-virginica'] # filter to only one species
setosa = df[df['class'] == 'Iris-setosa'] # filter to only one species
versicolor = df[df['class'] == 'Iris-versicolor'] # filter to only one species


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 5))

sepal1 = sorted(virginica['sepal_length'].tolist())
sepal_pdf1 = norm.pdf(sepal1, np.mean(sepal1), np.std(sepal1))

sepal2 = sorted(setosa['sepal_length'].tolist())
sepal_pdf2 = norm.pdf(sepal2, np.mean(sepal2), np.std(sepal2))

sepal3 = sorted(versicolor['sepal_length'].tolist())
sepal_pdf3 = norm.pdf(sepal3, np.mean(sepal3), np.std(sepal3))

ax1.plot(sepal1,sepal_pdf1,'-o')
ax1.hist(sepal1, density=True)  # 'density' normalizes the histogram to 1.0 using the PDF
ax1.set_xlabel("Sepal Length (cm) for Iris-Virginica")
#ax1.set_ylabel("Probability Density")
ax1.yaxis.set_visible(False)

ax2.plot(sepal2,sepal_pdf2,'-o')
ax2.hist(sepal2,density=True)  # 'density' normalizes the histogram to 1.0 using the PDF
ax2.set_xlabel("Sepal Length (cm) for Iris-Setosa")
#ax2.set_ylabel("Probability Density")
ax2.yaxis.set_visible(False)

ax3.plot(sepal3,sepal_pdf3,'-o')
ax3.hist(sepal3,density=True)  # 'density' normalizes the histogram to 1.0 using the PDF
ax3.set_xlabel("Sepal Length (cm) for Iris-Versicolor")
#ax3.set_ylabel("Probability Density")
ax3.yaxis.set_visible(False)
plt.suptitle("Histogram of sepal length with normal distribution plotted")
#plt.show()  
plt.savefig('Ball-Rague-Fig4.10.eps', bbox_inches='tight')

