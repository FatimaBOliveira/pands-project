# Analysis of Iris data set
#
# Author: Fatima Oliveira

# Data frames.
import pandas as pd
# Plotting.
import matplotlib.pyplot as plt
# Numerical arrays.
import numpy as np
 

 # load data from URL.
from urllib.request import urlretrieve
url = ("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
filename = "iris.csv" # I will give the name of the file loaded.
urlretrieve(url, filename)

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")


# Summary of each variable

a=df.describe()
a.to_csv('Summary of each variable.txt', sep='\t', index=False)
# https://saturncloud.io/blog/how-to-write-a-pandas-dataframe-to-a-txt-file/


# Histogram of each variable

slen = df["sepal_length"]
swid = df["sepal_width"]
plen = df["petal_length"]
pwid = df["petal_width"]


# https://matplotlib.org/stable/gallery/color/named_colors.html
plt.hist(slen, label= "sepal length", edgecolor = "black")
plt.hist(swid, label= "sepal width", edgecolor = "red")
plt.hist(plen, label= "petal length", edgecolor = "cyan")
plt.hist(pwid, label="petal width", edgecolor = "lime")
plt.title("Iris data set")
plt.legend()
plt.show()

s = df["species"]
plt.hist(s, label="species", edgecolor = "violet")
plt.legend()
plt.show()


'''
plt.savefig("Histogram.png") # to save plot in the directory
plt.show()

'''

# Scattter plot of each pair of variables



# Analysis