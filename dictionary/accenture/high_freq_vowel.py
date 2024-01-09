x=input("Enter your string: ")
x=x.lower()
d={p:x.count(p) for p in ['a','e','i','o','u']}
m=max(d.values())
for p,q in d.items():
    if(q==m):
        print(p,"with frequency of",q)