'''i=30
while(i<51):
    if(i%2!=0):
        print(i,end=" ")
    i=i+1
'''

#wap to find the sum of a number
'''n=int(input("Enter your number: "))
temp=n
s=0
while(temp!=0):
    n=temp%10
    s+=n
    temp=temp//10
print(s)
'''

#wap to check palindrome or not
'''n=int(input("Enter your number: "))
temp=n
s=0
while(temp!=0):
    digit=temp%10
    total=s*10+digit
    s=total
    temp=temp//10
if(total==n):
    print("Palindrome")
else:
    print("Not Palindrome")
    '''

#wap for desired number
n=int(input("Enter your number: "))
temp=n
place=0
s=0
count=0
while(n!=0):
    n=n//10
    count=count+1
print(count)
while(count!=0):
    digit=temp%10
    s+=(digit**count)
    count=count-1
print(s)
    
    
