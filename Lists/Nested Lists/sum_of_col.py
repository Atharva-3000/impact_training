#find row wise sum
l1=[[int(input("Enter Value: ")) for q in range(3)] for p in range(3)]
l3=[]
for i in range(3):
    sum=0
    for j in range(3):
       sum=sum+l1[j][i]
    l3.append(sum)
print(l3)