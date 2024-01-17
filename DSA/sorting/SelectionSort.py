def SelectionSort(ls):
    counter=0
    for i in range(len(ls)-1):
        counter+=1
        minIndex=i
        for j in range(i+1,len(ls)):
            if ls[j]<ls[minIndex]:
                minIndex=j
        ls[i],ls[minIndex]=ls[minIndex],ls[i]
        print(*ls)
    print(counter)

ls=list(map(int,input().split()))
SelectionSort(ls)
print(*ls) 