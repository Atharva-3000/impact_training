l=list(map(int,input().split()))
d=int(input())
c=l.count(d)
for p in range(c):
    l.remove(d)
print(l)
