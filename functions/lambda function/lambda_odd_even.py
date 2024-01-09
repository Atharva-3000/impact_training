s=lambda x:x%2==0   #even
a=lambda x:x%2!=0   #odd
l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
r=[p for p in l if(s(p))]
q=[p for p in l if(a(p))]
print(r)
print(q)