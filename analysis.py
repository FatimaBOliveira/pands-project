# Analysis of Iris data set
# Author: Fatima Oliveira

    # Libraries

# Data frames.
import pandas as pd
# Numerical arrays.
import numpy as np
# Plotting.
import matplotlib.pyplot as plt


    # Loading the data

# For this I downloaded the Iris data set from URL in: https://archive.ics.uci.edu/static/public/53/iris.zip.
# I extracted the files from zip file into my pands-project folder.
path = "./iris/"
logFilename = path + "iris.data"

# Column names given considering the file "iris.names", in section 7 the attributes of each variable.
colNames= ("sepal_length_cm",
    "sepal_width_cm", 
    "petal_length_cm", 
    "petal_width_cm", 
    "class" 
)

# Load the data set in this python script.
df = pd.read_csv(logFilename, names=colNames)


    # Summary of each variable

summary=df.describe()
summary.to_csv("Summary of each variable.txt", sep="\t", mode="w") # "w" will create txt file with the summary of the variables.


    # Histogram and bar charts

slen = df["sepal_length_cm"]
swid = df["sepal_width_cm"]
plen = df["petal_length_cm"]
pwid = df["petal_width_cm"]

# Histogram of variables together.

plt.hist(slen, label= "sepal length", color="cyan", histtype="step")
plt.hist(swid, label= "sepal width", color = "red", histtype="step")
plt.hist(plen, label= "petal length", color = "black", histtype="step")
plt.hist(pwid, label="petal width", color = "lime", histtype="step")
plt.title("Iris data set")
plt.xlabel("cm")
plt.ylabel("counts")
plt.legend()
plt.savefig("Histogram with variables together.png") # to save in the directory


# Separate histograms of each variable.

# Create a figure with each histogram.
fig, axes = plt.subplots(2,2, figsize=(10, 7))

# Define each histogram.
axes[0, 0].hist(slen, edgecolor = "cyan")
axes[0, 0].set_title("Sepal Length (cm)")
axes[0, 1].hist(swid, edgecolor = "red")
axes[0, 1].set_title("Sepal width (cm)")
axes[1, 0].hist(plen, edgecolor = "black")
axes[1, 0].set_title("Petal length (cm)")
axes[1, 1].hist(pwid, edgecolor = "lime")
axes[1, 1].set_title("Petal width (cm)")
plt.savefig("Histograms of each variable.png") 
plt.show()

# Bar chart - class of Iris.
s = df["class"]
values, counts = np.unique(s, return_counts=True)
plt.bar(values, counts, color=["green", "red","blue"])
plt.title("Class of Iris")
plt.savefig("Class of Iris bar chart.png")
plt.show()


    # Scatter plots and Pearson Correlation Coefficient

# Scatter plots

# Create a new figure with the scatter plots. 
fig, axs = plt.subplots(2, 3, figsize=(14, 7))

# Define each scatter plot.
axs[0, 0].scatter(slen, swid, edgecolors=["cyan","red"])
axs[0, 0].set_title("Sepal length and sepal width")
axs[0, 1].scatter(slen, plen, edgecolors=["cyan","black"])
axs[0, 1].set_title("Sepal length and petal length")
axs[0, 2].scatter(slen, pwid, edgecolors=["cyan","lime"])
axs[0, 2].set_title("Sepal length and petal width")
axs[1, 0].scatter(swid, plen, edgecolors=["red","black"])
axs[1, 0].set_title("Sepal width and petal length")
axs[1, 1].scatter(swid, pwid, edgecolors=["red","lime"])
axs[1, 1].set_title("Sepal width and petal width")
axs[1, 2].scatter(plen, pwid, edgecolors=["black","lime"])
axs[1, 2].set_title("Petal length and petal width")
plt.savefig("Scatter plots.png")
plt.show()

# Pearson Correlation Coefficient.

print(np.corrcoef(slen, swid))
print(np.corrcoef(slen, plen))
print(np.corrcoef(slen, pwid))
print(np.corrcoef(swid, plen))
print(np.corrcoef(swid, pwid))
print(np.corrcoef(plen, pwid))