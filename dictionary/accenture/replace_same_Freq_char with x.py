#wap to replace the characters with same frequency one with lower ascii value with t
# s=input("String: ")
# c=input("Character: ")
# d={p:s.count(p) for p in s}
# ans=[]
# m=max(d.values())
# for p,q in d.items():
#     if(q==m):
#         ans.append(p)
# stringAns = ''.join(sorted(ans))
# print(stringAns)
# for p,q in d.items():
#     if(p==stringAns[0]):
#         d[p]=c
# print(d)

s=input("String: ")
c=input("Character: ")
d={p:s.count(p) for p in s}
m=max(d.values())
l=[]
for p,q in d.items():
    if(m==q):
        l.append(p)
l.sort()
res=''
for p in s:
    if(p==l[0]):
        res=res+c
    else:
        res=res+p
print(res)