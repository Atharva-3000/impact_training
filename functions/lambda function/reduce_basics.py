from functools import reduce
# l=[1,2,3,4,5]
# r=reduce(lambda a,b:a+b,l)
# print(r)



l=[12,315,9,17,21,25,1]
mi=reduce(lambda a,b: a if a>b else b,l)
ma=reduce(lambda a,b: a if a<b else b,l)
print(mi,ma)