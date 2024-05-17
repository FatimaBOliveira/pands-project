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

# Path to the raw data.
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

# Describe the data set.
summary=df.describe()

# Create a txt file with the summary.
summary.to_csv("Summary of each variable.txt", sep="\t", mode="w")


    # Histogram and bar charts

    ## Histogram of variables together.

# Call the attributes.
slen = df["sepal_length_cm"]
swid = df["sepal_width_cm"]
plen = df["petal_length_cm"]
pwid = df["petal_width_cm"]

# Create a histogram for each variable.
plt.hist(slen, label= "sepal length", color="cyan", histtype="step")
plt.hist(swid, label= "sepal width", color = "red", histtype="step")
plt.hist(plen, label= "petal length", color = "black", histtype="step")
plt.hist(pwid, label="petal width", color = "lime", histtype="step")

# Add a title.
plt.title("Iris data set")

# Add labels in the x and y axes.
plt.xlabel("cm")
plt.ylabel("counts")

# Add a legend.
plt.legend()

# Save the histogram as a png file in the directory.
plt.savefig("Histogram with variables together.png")

    ## Separate histograms of each variable.

# Create one figure with histograms of each attribute, individually.
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

# Save the figure generated and show it.
plt.savefig("Histograms of each variable.png") 
plt.show()

    ## Bar chart - class of Iris.

# Call the variable
s = df["class"]

# Get the values and counts for "class".
values, counts = np.unique(s, return_counts=True)

# Crate a bar chart.
plt.bar(values, counts, color=["green", "red","blue"])

# Add a tittle, y axis label, save the figure and show it.
plt.title("Class of Iris")
plt.ylabel("Counts")
plt.savefig("Class of Iris bar chart.png")
plt.show()


    # Scatter plots and Pearson Correlation Coefficient

    ## Scatter plots

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

# Save and show the plots.
plt.savefig("Scatter plots.png")
plt.show()

    ## Pearson Correlation Coefficient.

# Print the Pearson correlation results.
print(np.corrcoef(slen, swid))
print(np.corrcoef(slen, plen))
print(np.corrcoef(slen, pwid))
print(np.corrcoef(swid, plen))
print(np.corrcoef(swid, pwid))
print(np.corrcoef(plen, pwid))