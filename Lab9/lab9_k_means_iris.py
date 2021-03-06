# -*- coding: utf-8 -*-
"""Lab9_K-means_IRIS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jrTD85Ncf42B9x_LgvsdG7wJ_-81inKJ
"""

import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
irisdata = pd.read_csv(url, names=colnames)
irisdata.head()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
iris =   pd.read_csv("Iris.csv") 
print(iris.head())

iris.plot(kind="scatter", x="SepalLengthCm",   y="SepalWidthCm")
plt.show()



import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

colnames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
irisdata = pd.read_csv(url, names=colnames)

irisdata.head()

irisdata['Class'] = pd.Categorical(irisdata["Class"])
irisdata["Class"] = irisdata["Class"].cat.codes

X = irisdata.values[:, 0:4]
y = irisdata.values[:, 4]
from sklearn.cluster import KMeans

# Number of clusters
kmeans = KMeans(n_clusters=3)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_

kmeans.cluster_centers_

kmeans.labels_

plt.scatter(X[:, 0], X[:, -1])

plt.title('cluster centroids')
plt.show()

from sklearn.metrics import silhouette_score
print(silhouette_score(X, kmeans.labels_))