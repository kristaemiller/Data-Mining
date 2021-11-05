# -*- coding: utf-8 -*-
"""
Krista Miller
Yash Murthy
Data mining exercise 8 part 1
"""

import pandas as pd
import numpy as np 
import random as rd

dataset= pd.read_csv('exercise8_infile1.csv')
dataset.describe()

X= dataset.values

m=X.shape[0]
n=X.shape[1]
n_iter= 100

K=3 #NUM OF CLUSTERS

Centroids=np.array([]).reshape(n,0)

for i in range(K):
    rand=rd.randint(0,m-1)
    Centroids=np.c_[Centroids,X[rand]]

Output={}

EuclidianDistance=np.array([]).reshape(m,0)
for k in range(K):
    tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
    EuclidianDistance=np.c_[EuclidianDistance,tempDist]
C=np.argmin(EuclidianDistance,axis=1)+1

Y={}
for k in range(K):
    Y[k+1]=np.array([]).reshape(3,0)
for i in range(m):
    Y[C[i]]=np.c_[Y[C[i]],X[i]]
     
for k in range(K):
    Y[k+1]=Y[k+1].T
    
for k in range(K):
     Centroids[:,k]=np.mean(Y[k+1],axis=0)

for i in range(n_iter):
     #step 2.a
    EuclidianDistance=np.array([]).reshape(m,0)
    for k in range(K):
        tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
        EuclidianDistance=np.c_[EuclidianDistance,tempDist]
    C=np.argmin(EuclidianDistance,axis=1)+1
     #step 2.b
    Y={}
    for k in range(K):
        Y[k+1]=np.array([]).reshape(3,0)
    for i in range(m):
        Y[C[i]]=np.c_[Y[C[i]],X[i]]

    for k in range(K):
        Y[k+1]=Y[k+1].T

    for k in range(K):
        Centroids[:,k]=np.mean(Y[k+1],axis=0)
    Output=Y

Output
print(Output)

print("number of points in cluster 1: ", len(Output[1]))
print("number of points in cluster 2: ", len(Output[2]))
print("number of points in cluster 3: ", len(Output[3]))
