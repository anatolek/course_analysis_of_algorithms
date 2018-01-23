#! /usr/bin/python3
#import math

import numpy as np
np.set_printoptions(threshold=np.nan)

data = np.loadtxt("1000_100.txt", skiprows=0)
data = data[np.s_[:,1:]]

person = 951
person2 = 178

data = data[:,np.argsort(data[person-1])]

x = np.shape(data)[1]
y = np.shape(data)[0]


for i in range(y):
    count = 0
    one = data[np.s_[i:i+1:]].reshape(x)
    k1 = 0
    k2 = x
    while k1 < (k2-1):
        suma = 0
        for j in range(k1, k2):
            if one[k1] > one[j]:
                count += 1
        suma += count
        k1 += 1
    if i == person2-1:
        print (i+1,"-",suma)