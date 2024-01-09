d1={"Name":"Atharva","id":259,"dept":"CSE","Salary":50000000}
d2={"Name":"Meet","id":269,"dept":"CSE-AI","Salary":100000000}
d3={"Name":"Dainik","id":101,"dept":"CSE-BC","Salary":50000}
# print(d1,d2,d3)
sal1=d1.get("Salary")
print(sal1)
for p in d1.keys():
    print(p)
for q in d1.values():
    print(q)
for p,q in d1.items():
    print(p,q)
for s in d1.items():
    print(s)      #will return in tuple form
for z in d1.items():
    print(z[0],z[1])    #similar to * printing without quotes and brackets
r=sorted(list(d1.keys()))
print(r)    #returns a list of all the keys