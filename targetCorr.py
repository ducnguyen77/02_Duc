__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from random import uniform
from matplotlib.pyplot import figure, plot, scatter, show
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#change the targets to numeric values
target = []
for i in range(208):
    #assign 0 or 1 target value based on "M" or "R" labels
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

    #plot rows of data as if they were series data

dataRow = rocksVMines.iloc[0:208,35]

fig = figure()
ax = fig.add_subplot(1,2,1)
plt.scatter(dataRow, target, s=50)

plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
ax.set_title("No unifrom added")

#
#To improve the visualization, this version dithers the points a little
# and makes them somewhat transparent
target = []
for i in range(208):
    #assign 0 or 1 target value based on "M" or "R" labels
    # and add some dither
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0 + uniform(-0.1, 0.1))
    else:
        target.append(0.0 + uniform(-0.1, 0.1))

    #plot rows of data as if they were series data
dataRow = rocksVMines.iloc[0:208,35]
ax = fig.add_subplot(1,2,2)
plt.scatter(dataRow, target, alpha=0.5, s=50)

plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
ax.set_title("Unifrom added")

print "dataRow35 min\n", dataRow.min()
print "dataRow35 Max\n", dataRow.max ()


show()

print "target values Rock", target[0:10]
print "target values Mine", target[200:205]




