#! /usr/bin/python3
#import math
#password = sorted data[0] + the most frequent letter + sorted data[last]

import numpy as np

D = np.genfromtxt("anagrams.txt", dtype='str').tolist()
dic = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

def redixSort(data, dictionary, d):
    array = []
    for k in range(d-1,-1,-1):
        for i in range(len(dictionary)):
            for j in range(len(data)):
                if (dictionary[i] == data[j][k:k+1]):
                    array.append(data[j])
        #print (array[0])
        data = array
        array = []
    return data

def freq(data, dictionary):
    result = {}
    for i in range(len(dictionary)):
        count = 0
        for j in range(len(data)):
            for k in range(len(data[j])):
                if (dictionary[i] == data[j][k:k+1]):
                    count+=1
        #print(dictionary[i], '--', count)
        result.update({dictionary[i]: count})
    result = sorted(result.items(), key=lambda x: x[1])
    return result[-1][0]

sd = redixSort(D, dic, len(D[0]))
fl = freq(D, dic)
print(sd[0]+fl+sd[-1])

