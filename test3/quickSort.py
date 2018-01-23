#! /usr/bin/python3
#import math

import numpy as np

data = np.loadtxt("input__100.txt", skiprows=1).tolist()



def QS(arr,z):
    
    comparison = 0
    
    def Mediana(A,p,r):
        m_ind = (p+r)//2 
        if (len(A) < 2) or ((A[p] < A[r]) and (A[p] > A[m_ind])) or ((A[p] > A[r]) and (A[p] < A[m_ind])):
            m_ind = p
        elif ((A[r] < A[p]) and (A[r] > A[m_ind])) or ((A[r] > A[p]) and (A[r] < A[m_ind])):
            m_ind = r
        else:
            return m_ind        
        return m_ind
    
    def Reverse(A, z1, z2):
        a,b = A.index(A[z1]), A.index(A[z2])
        A[a],A[b] = A[b],A[a]
        return A
    
    def QuickSort(A,p,r,z):
        if p<r:
            if z == 'first':
                Reverse(A, p, r)
                q = Partition(A, p, r)
                QuickSort(A, p, q-1, z)
                QuickSort(A, q+1, r, z)
            elif z == 'mediana':
                Reverse(A, Mediana(A,p,r), r)
                q = Partition(A, p, r)
                QuickSort(A, p, q-1, z)
                QuickSort(A, q+1, r, z)
            elif z == 'last':
                q = Partition(A, p, r)
                QuickSort(A, p, q-1, z)
                QuickSort(A, q+1, r, z)
            else:
                return print ('The last parameter takes values "first", "last" or "mediana".')
        return A
    
    def Partition(A,p,r):
        x = A[r]
        i = p-1
        global comparison
        comparison = comparison + (r-p)
        for j in range(p,r):
            if A[j] <= x:
                i+=1
                a,b = A.index(A[i]), A.index(A[j])
                A[a],A[b] = A[b],A[a]
        d,c = A.index(A[i+1]),A.index(A[r])
        A[c],A[d] = A[d],A[c]
        return i+1
    
    QuickSort(data,0,len(data)-1,z)
    return data


QS(data,'last')
print (comparison)

QS(data,'first')
print (comparison)