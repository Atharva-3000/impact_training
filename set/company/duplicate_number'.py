s=input()
r=set(s)
l=list(r)
l.sort()
for p in l:
    print(p,"=",s.count(p))