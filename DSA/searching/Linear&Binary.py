def linear_search(ls, key):
    for i in range(len(ls)):
        if ls[i] == key:
            print("Element found at index: ",end=" ")
            return i
    return -1

def binary_search(ls,key):
    low=0
    high=len(ls)-1
    while(low<=high):
        mid=(low+(high-low)//2)
        if(ls[mid]==key):
            return mid
        elif(key>ls[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1

ls=list(map(int, input("Enter values separated by space: ").split()))
print(linear_search(ls, int(input("Enter value to search: "))))
ls=sorted(ls)
print(ls)
print(binary_search(ls, int(input("Enter value to search: "))))