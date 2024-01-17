def bubbleSort(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-1-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]

ls=list(map(int,input().split()))
bubbleSort(ls)
print(*ls)