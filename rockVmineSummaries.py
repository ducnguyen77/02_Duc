__author__ = 'mike_bowles' # Modified by Duc Nguyen
import urllib2
import sys
import pandas as pd
from pandas import DataFrame
import numpy as np

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")
data = urllib2.urlopen(target_url)
print "data type: ", type(data)

myfile = data.readline()
print myfile

print "myfile length", len(myfile)
test = myfile.strip().split(",")
print "test file", test
print "lenght test file", len(test)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
    #split on comma
    row = line.strip().split(",")
    xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])))

# extend the code by Duc

print "type of xlist", type(xList)
# converting a list to a dataframe
df = DataFrame(xList)
print "data shape", df.shape

print "data frame df head \n", df.head()

# The last column
last_cl = df[60]
#print last_cl
print"unique name: \n ", pd.unique(last_cl) # checking the unique of the last column


# write data to a csv file
#df.to_csv('data.csv', index = True)

colMean = np.mean(df)
print "Col mean \n", colMean
