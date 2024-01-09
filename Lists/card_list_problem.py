#sort single number to sorted as string
n=int(input("Enter you cards: "))
l=list(map(int,str(n)))
l.sort()
if(l[0]==0):
      l[0],l[1]=l[1],l[0]
print(l)
r=list(map(str,l))
print(''.join(r))
