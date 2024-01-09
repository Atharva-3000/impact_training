s={}
print(type(s))
s=set()
print(type(s))
s={10,23,42,1}
print(s)
print(*s)
s={10,34,45,12,23,34}
print(s)
# print(s[2]) error!!!!!!!
s.add(35)
print(s)

s={1,2,3,4,5,6}
print(s.discard(7))   #doesnt give error
# print(s.remove(7))    #gives error

s.clear()
print(s)
s={1,2,3,4,5}
r={4,5,6,7,8}
print(s.pop())
print(s.intersection(r))