import numpy as np
#np.set_printoptions(threshold=np.nan)
k = 0
def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]

def heapify(sqc,end,i):
    l=2*i+1
    r=l+1
    max=i
    print (k)
    if l < end and sqc[i] < sqc[l]:
        max = l
    if r < end and sqc[max] < sqc[r]:
        max = r
    if max != i:
        swap(sqc,i,max)
        heapify(sqc,end,max)

def heap_sort(sqc):
    end = len(sqc)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(sqc, end, i)
    for i in range(end-1, 0, -1):
        swap(sqc, i, 0)
        heapify(sqc, i, 0)
        print(i)

data = np.loadtxt("input_16_10000.txt", skiprows=1).tolist()
#heap_sort(data)
#print(data)

def func(l):
    size=len(l)
    for root in range((size//2)-1,-1,-1):
        root_val = l[root]             # save root value
        child = 2*root+1
        while(child<size):
            if child<size-1 and l[child]>l[child+1]:
                child+=1
            if root_val<=l[child]:     # compare against saved root value
                break
            l[(child-1)//2]=l[child]   # find child's parent's index correctly
            child=2*child+1
        l[(child-1)//2]=root_val       # here too, and assign saved root value
    return l