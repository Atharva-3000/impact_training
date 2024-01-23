#wap tp print prime number between 1 to 100 using nested while.
i=2
l=[]
while(i<101):
    c=0
    q=1
    while(q<=i):
        if(i%q==0):
            c+=1
        q+=1
    if(c==2):
        l.append(i)
    i+=1
print(l)
print(len(l))