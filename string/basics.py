s="Good morning all"
r=s.split()
print(r)
for p in r:
    print(p)
s=["Python","ML", "DS","AI"]
r="-".join(s)
print(r)
r=" ".join(s)
print(r)
s="guntur vijayawada"
print(s.count('a'))
print(s.index('a'))
print(s.index('a',11,14))
print(s.index('a',14))  #gives error if not found
print(s.find('a'))    #returns -1 if not found
print(s.rfind('a'))
print(s.rfind('a',12,15))
print(s.startswith('a'))
print(s.endswith('a'))
print(s.replace('a','v'))
s="Modi is pm of india"
print(s.replace('Modi','Rahul'))
# print(s)
s=" gujarat vadodara "
print(s.strip())
s="KRIshna"
print(s.center(11,"#"))
print(s.center(12,"@"))   #extra one on the left
print(s.swapcase())