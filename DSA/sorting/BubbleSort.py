def bubbleSort(ls):
    counter=0
    for i in range(len(ls)-1):
        counter+=1
        for j in range(len(ls)-1-i):
            if len(ls[j])>len(ls[j+1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
    print(counter)

# ls=list(map(int,input().split()))
# bubbleSort(ls)
# print(*ls)

la=["abc","a","hello"]
bubbleSort(la)
print(*la)