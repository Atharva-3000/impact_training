# Write a program to read list elements from user with or without the for loop
# l1=list(map(int,input("Start entering elements space-seperated: ").split()))
# Based on predefined size
# size=int(input(("Enter the size of the list: ")))
# l2=list(map(int,input("Start entering elements space-seperated: ").split()))[:size]
# print(l1)
# print(l2)

# using for loop
l3=[]
size1= int(input("Enter the size of the list: "))
for i in range(size1):
    # val=int(input("Enter element {i}").format(i))
    val=int(input())
    l3.append(val)
print(*l3)