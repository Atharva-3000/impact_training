#write a program to print the prime numbers between 1 and 50
for p in range(1,51):
    c=0
    for q in range(1,p+1):
        if(p%q==0):
            c=c+1
    if(c==2):
        print(p,end=" ")

#                                                                   OR
