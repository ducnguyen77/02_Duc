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

result1 = df.copy()
for feature_name in df.columns:
    max_value = df[feature_name].max()
    min_value = df[feature_name].min()
    result1[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
print result1.head()

# 2. normalized_df=(df-df.mean())/df.std()
result2 = df.copy()
for i in range(8):
    dfMean = df.iloc[i].mean()
    dfStd = df.iloc[i].std()
    result2.iloc[:, i:(i+1)] = (result2.iloc[:, i:(i+1)] - dfMean)/dfStd
print result2.head()

# Cach nay la trong sach ho lam
abaloneNormalized = abalone.iloc[:,1:9]
for i in range(8):
    mean = summary.iloc[1, i]
    sd = summary.iloc[2, i]
    abaloneNormalized.iloc[:,i:(i + 1)] = (
                    abaloneNormalized.iloc[:,i:(i + 1)] - mean) / sd  # (y-mean)/sd

result3 = abaloneNormalized.values
result3 = DataFrame(result3)
result3.columns = df.columns

result4 = df.apply(lambda x: x.max() - x.min())
print "\nresult4\n", result4


#box plot the real-valued attributes
#convert to array for plot routine
fig = figure()

ax = fig.add_subplot(3,1,1)
ax.margins(.1)
DataFrame.boxplot(result1, grid = True)
#plot.xlabel("Attribute Index")
ax.xaxis.set_visible(False)
plot.ylabel(("Quartile Ranges 1)"))
fig.suptitle("Box plot of Normalization Data", color = 'red', size=20)

ax = fig.add_subplot(3,1,2)
DataFrame.boxplot(result2, grid = True)
#plot.xlabel("Attribute Index")
ax.xaxis.set_visible(False)
plot.ylabel(("Quartile Ranges 2"))

ax = fig.add_subplot(3,1,3)
DataFrame.boxplot(result3, column=None, rot = 10, fontsize = 10, grid = True)
plot.xlabel("Attribute Index", size = 20, color = 'blue')
plot.ylabel(("Quartile Ranges 3"))

savefig("BoxPLot_DataNormalization.pdf", pdi = 2000)

show()







