__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

from matplotlib.pyplot import figure, show, savefig


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#calculate correlations between real-valued attributes

corMat = DataFrame(rocksVMines.corr())

print "Correlation matrix haed\n", corMat.head()
print "Correlation matrix shape\n", corMat.shape

#visualize correlations using heatmap

fig = figure()
ax = fig.add_subplot(1,2,1)
plot.pcolor(corMat)
plot.colorbar()
ax.set_title ('pcolor plot')
#plot.show()

# Extended by Duc
ax = fig.add_subplot(1,2,2)
plot.imshow(corMat, cmap='hot', interpolation='nearest')
plot.colorbar()
ax.set_title("imshow heatmap plot")
savefig('heatmap_plot.pdf', pdi=1000)
show()

