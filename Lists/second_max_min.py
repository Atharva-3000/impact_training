# l=[1,6,1,5,2,6]
# mi=l[0]
# ma=l[len(l)-1]
# l.sort()
# if(l[0]==l[1]):
#     mi=l[2]
# if(l[len(l)-1]==l[len(l)-2]):
#     ma=l[len(l)-3]
# print(ma,mi)

n=int(input())
l=list(map(int,input().split()))[:n]
print(l)
l.sort()
print("max 1: ", l[-1])
c=l.count(l[-1])
c2=l.count(l[0])
d=l[-(c+1)]
d2=l[c2]
print("Second max: ",d)
print("Second min: ",d2)