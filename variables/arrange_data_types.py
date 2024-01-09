l=[1,4,"Semantic","heyy",5,3,"Why?","Hello"]
n1=[]
n2=[]
for p in l:
    if(type(p)==int):
        n1.append(p)
    else:
        n2.append(p)
n1.sort(),n2.sort()
print(*n1,"\n",*n2)
