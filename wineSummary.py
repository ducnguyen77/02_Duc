#__author__ = 'mike_bowles'
import pandas as pd
#import numpy as np
from pandas import DataFrame
#from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-"
              "learning-databases/wine-quality/winequality-red.csv")

wine = pd.read_csv(target_url, header=0, sep=";")

print("type of data: \n", type(wine))
print(wine.head())

# generate statistical summarie
summary = wine.describe()
print(summary)

wineNormalized = wine
n_cols = len(wineNormalized.columns)

for i in range(n_cols):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    wineNormalized.iloc[:, i:(i + 1)] = \
        (wineNormalized.iloc[:, i:(i + 1)] - mean) / sd

array = wineNormalized.values
# boxplot(array)
DataFrame.boxplot(wineNormalized, rot=20, grid=True, fontsize=10)
plot.xlabel("Attribute Index")
plot.ylabel("Quartile Ranges - Normalized ")
plot.show()

print("Test deburg")
wine.tail()
type(wine)
DataFrame.boxplot(wineNormalized, rot=50, grid=True, fontsize=10)




