__author__ = 'mike_bowles'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url,header=None, prefix="V")

'''
Can not use header = True. It will give the following error message:
TypeError: Passing a bool to header is invalid. 
Use header=None for no header or header=int or list-like of ints to specify the row(s) making up the column names
'''

#print head and tail of data frame
print "head\n", (rocksVMines.head())
print "tail\n", (rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()
print "print summary of data frame"
print(summary)
