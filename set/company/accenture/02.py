#sheena is a freelancer 
s=input()
r=set(s)
l=list(r)
l.sort()
for p in l:
     if(s.count(p)>1):
        print(p+"-"+str(s.count(p)),end=" ")