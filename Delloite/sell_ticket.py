# Given N is the number of prime number to be printed including 2 and 5, and K is the last digit of the prime number. Print a list L in ascending order of first N prime numbers that end with digit K and include 2 and 5.

N=int(input())
K=int(input())
i=2
l=[]
t=[]
if(N>=2):
    t.append(2)
    t.append(5)
while(len(l)<N):
    c=0
    q=1
    while(q<=i):
        if(i%q==0):
            c+=1
        q+=1
    if(c==2 and i%10==K):
        l.append(i)
    i+=1
t.extend(l)
print(t)