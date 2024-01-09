n=int(input("Enter the lenght of your list: "))
ls=list(map(int,input().split()))[:n]
d={p:ls.count(p) for p in ls}
l=[]
for p,q in d.items():
    if(p==q):
        l.append(p)
if(len(l)>1):
    print(*l)
else:
    print("-1")   