#wap to read 2*2 nested list elements for 2 matrices and perform the addition operation
l1=[[int(input("Enter Value: ")) for q in range(2)] for p in range(2)]
l2=[[int(input("Enter Value: ")) for q in range(2)] for p in range(2)]
c=[[0,0], [0,0]]
for i in range(2):
    for j in range(2):
        c[i][j]=l1[i][j]+l2[i][j]
# print(*c,end=" ")
for i in range(2):
    for j in range(2):
        print(c[i][j],end=" ")
    print()