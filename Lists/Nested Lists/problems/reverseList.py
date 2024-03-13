# reverse the given nested list, both the internal list and the order  of the row as well without revere function

s=[[1,2,3], [4,5,6], [7,8,9]]
d=[]
for p in s[::-1]:
    r=p[::-1]
    d.append(r)

print(d)

q=[p[::-1] for p in s[::-1]]
print(q)