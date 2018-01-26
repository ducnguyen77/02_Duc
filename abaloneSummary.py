__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot
from matplotlib.pyplot import figure, show, savefig

target_url = ("http://archive.ics.uci.edu/ml/machine-"
              "learning-databases/abalone/abalone.data")
#read abalone data
abalone = pd.read_csv(target_url,header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight',
                   'Shucked weight', 'Viscera weight', 'Shell weight',
                   'Rings']


print(abalone.head())
print(abalone.tail())

#print summary of data frame
summary = abalone.describe()
print(summary)

# Boxplot for a data frame using pandas module
DataFrame.boxplot(abalone, column=None, rot = 20, fontsize = 10, grid = True)
#savefig("Box_Plot_DataFrame.pdf", pdi=1000)
plot.show()

# Plotting
fig = figure()

#box plot the real-valued attributes
#convert to array for plot routine
array = abalone.iloc[:,1:9].values
ax = fig.add_subplot(3,1,1)
boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
#show()

#the last column (rings) is out of scale with the rest
# - remove and replot
array2 = abalone.iloc[:,1:8].values
ax = fig.add_subplot(3,1,2)
boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
#show()

#removing is okay but renormalizing the variables generalizes better.
#renormalize columns to zero mean and unit standard deviation
#this is a common normalization and desirable for other operations
# (like k-means clustering or k-nearest neighbors
abaloneNormalized = abalone.iloc[:,1:9]


for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:,i:(i + 1)] = (
                    abaloneNormalized.iloc[:,i:(i + 1)] - mean) / sd  # (y-mean)/sd

array3 = abaloneNormalized.values


ax = fig.add_subplot(3,1,3)
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))

#savefig("Box_Plot.pdf", pdi=1000)

show()