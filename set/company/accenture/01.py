#aabccde---->a2b1c2d1e1
s=input()
r=set(s)
l=list(r)
l.sort()
ans=""
for p in l:
    # print(p,"=",s.count(p))
    ans=ans+str(p)
    ans=ans+str(s.count(p))
print(ans)