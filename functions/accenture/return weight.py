# n=input()
# base=1
# l=[]
# for i in n:
#     if(ord(i)-65==0):
#         l.append('1')
#     else:
#         s='1'
#         s.join(10**(ord(i)-65))
#         l.append(s)
# l=int(l)

def weight(p):
    w=10**(ord(p)-ord('A'))
    return w

d=input("Enter the string: ")
s=0
for p in d:
    r=weight(p)
    s=s+r
print(s)