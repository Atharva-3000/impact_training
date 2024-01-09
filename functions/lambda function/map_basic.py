def sq(n):
    return n*n
l=[1,2,3,4,5]
r=tuple(map(sq,l))
print(r)

l=[1,2,3,4,5]
r=tuple(map(lambda x:x*x,l))
print(r)

s=["abc","ABC","rqt"]
r=tuple(map(lambda x: x.upper(),s))
print(r)