#input is a string is names and age
#arrange the keys in sorted values
#arrange values in sorted order
d={"raju":45,"anil":56,"zoo":34,"saritha":2,"bharathi":29,"krishna":32}
# a = sorted(d.items(), key=lambda x:x[1])
# b = sorted(d.items(), key=lambda x:x[0])
r=sorted(d.keys())
a=sorted(d.values())
e={}
f={}
for s in r:
    for p,q in d.items():
        if(s==p):
            e.update({p:q})
            break
for s in a:
    for p,q in d.items():
        if(s==q):
            f.update({p:q})
            break
print(e)
print(f)