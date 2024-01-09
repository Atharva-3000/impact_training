n=int(input("Enter the size of your list: "))
l=list(map(int,input().split()))[:n]
l.sort()
ans=[]
for i in range(len(l)//2):
    ans.append(l[i])
    ans.append(l[-(i+1)])
if(len(ans)%2!=0):
    ans.append(l[len(l)//2])
print(ans)