def insertionSort(arr):
    for p in range(1,len(l)):
        key=l[p]
        q=p-1
        while((q>=0) and (key<l[q])):
            l[q+1]=l[q]
            q=q-1
        l[q+1]=key
        print(*l)
    return l

l=[5,4,1,2,3]
print("Before sorting: ",*l)
insertionSort(l)
print("After sorting: ",*l)