# find the leader
n=int(input("Enter the size of your list: "))
l=list(map(int,input().split()))
leader=[]
for i in range (len(l)):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            break
    else:
        leader.append(l[i])
if(len(leader)>0):
    print("Sum of the leaders are: ",sum(leader))
else:
    print("-1")
# print("The sum of the leader is: ", sum)
