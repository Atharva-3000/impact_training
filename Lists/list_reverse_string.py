#sort single number to sorted as string
n=int(input("Enter you number: "))
l=list(map(int,str(n)))
l.sort(reverse=True)
print(l)
r=list(map(str,l))
print(''.join(r))
