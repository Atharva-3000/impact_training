n = int(input("Enter the number: "))
count=0
while(n>=1):
    divisor=1
    for i in range(n-1,0,-1):
        if(n%i==0):
            divisor=i
            break
    n-=divisor
    count+=1
print(count)