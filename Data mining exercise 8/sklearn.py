# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:59:44 2021

@author: bisho
"""

import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

data=pd.read_csv("exercise8_infile1.csv")

kmeans_m = KMeans(n_clusters=3, random_state= 0).fit(data)
centroids = kmeans_m.cluster_centers_
data['kmean'] = kmeans_m.labels_ 

# plt.scatter(data['d1'], data['d2'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
# plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
# plt.show()

print(f'Centroid 1: {kmeans_m.cluster_centers_[0]}')
print(f'Number of points in Cluster 1: {len(data[data.kmean == 0])}')
print('Cluster 1:')
print(data[data.kmean == 0][['d1', 'd2', 'd3']].values.tolist())
print()
print(f'Centroid 2: {kmeans_m.cluster_centers_[1]}')
print(f'Number of points in Cluster 2: {len(data[data.kmean == 1])}')
print('Cluster 2:')
print(data[data.kmean == 1][['d1', 'd2', 'd3']].values.tolist())
print()
print(f'Centroid 3: {kmeans_m.cluster_centers_[2]}')
print(f'Number of points in Cluster 3: {len(data[data.kmean == 2])}')
print('Cluster 3:')
print(data[data.kmean == 2][['d1', 'd2', 'd3']].values.tolist()) 

print('means for the three clusters are:')

print(kmeans.cluster_centers_)

print('Using the clustering model to predict clusters now.')

print('kmeans.predict( [ [8,8,8], [19,19,19], [31,31,31]] ) returns: ')

print(kmeans.predict( [ [8,8,8], [19,19,19], [31,31,31]] ) )