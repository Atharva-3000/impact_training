def palin(p):
    r=p[::-1]
    if(r!=p):
        return False
        
d=int(input("Enter the number: "))
l=list(map(str,input().split()))[:d]
flag=True
for p in l:
    a=palin(p)
    if(a==False):
        flag=False
        break
if(flag):
    print("YES")
else:
    print("NO")