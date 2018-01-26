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
summary = abalone.describe()
#print(summary)

# Normalize the data to have mean=0 and std=1
abaloneNormalized = abalone.iloc[:,1:9]
#print "head\n", abaloneNormalized.head()

# 2 methods to normalize the data
# 1. normalized_df=(df-df.min())/(df.max()-df.min())
# 2. normalized_df=(df-df.mean())/df.std()

# 1. normalized_df=(df-df.min())/(df.max()-df.min())
df = abalone.copy()
df = df.iloc[:, 1:9] # exclude the first column because it contains string
print df.columns

result = df.copy()
for feature_name in df.columns:
    max_value = df[feature_name].max()
    min_value = df[feature_name].min()
    result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
print result



# 2. normalized_df=(df-df.mean())/df.std()


'''
#box plot the real-valued attributes
#convert to array for plot routine
fig = figure()

ax = fig.add_subplot(2,1,1)
boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))

ax = fig.add_subplot(2,1,2)
boxplot(array4)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))

show()

'''


