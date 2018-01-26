__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, plot, scatter, show
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

#calculate correlations between real-valued attributes
dataRow2 = rocksVMines.iloc[1,0:60]
dataRow3 = rocksVMines.iloc[2,0:60]

#plt.scatter(dataRow2, dataRow3)


#plt.xlabel("2nd Attribute")
#plt.ylabel(("3rd Attribute"))
#plt.show()

dataRow21 = rocksVMines.iloc[20,0:60]
dataRow151 = rocksVMines.iloc[150,0:60]
dataRow201 = rocksVMines.iloc[200,0:60]


#plt.scatter(dataRow2, dataRow21)

#plt.xlabel("2nd Attribute")
#plt.ylabel(("21st Attribute"))
#plt.show()

# extended by Duc
# Show all plots in one panel. Subplot

fig = figure()
ax = fig.add_subplot(2, 2, 1)
plt.scatter(dataRow2, dataRow3)
plt.xlabel("2nd Attribute")
plt.ylabel(("3rd Attribute"))
ax.set_title("Rock: Row2 vs Row3")

ax = fig.add_subplot(2, 2, 2)
plt.scatter(dataRow2, dataRow21)
ax.set_title("Row2 vs Row21")
plt.xlabel("2nd Attribute")
plt.ylabel(("Rock: 21st Attribute"))


ax = fig.add_subplot(2, 2, 3)
plt.scatter(dataRow2, dataRow151)
plt.xlabel("2nd Attribute")
plt.ylabel(("151st Attribute"))
ax.set_title("Mine: Row2 vs Row151")


ax = fig.add_subplot(2, 2, 4)
plt.scatter(dataRow2, dataRow201)
plt.xlabel("2nd Attribute")
plt.ylabel(("201st Attribute"))
ax.set_title("Mine: Row2 vs Row201")

show()



