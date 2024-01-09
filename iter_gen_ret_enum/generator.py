l=[1,2,3,4,5,6]
r=enumerate(l)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))

x=[1,2,3,4,5,6]   #start count from 5
r=enumerate(x,5)
# print(next(r))
# print(next(r))
# print(next(r))
# print(next(r))
for p,q in r:
    print(p,q)