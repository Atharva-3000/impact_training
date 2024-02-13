# n=int(input("Enter n: "))
# a=0
# b=1
# print(a,b,end=' ')
# c=a+b
# while(c<=n):
#     print(c,end=' ')
#     a=b
#     b=c
#     c=a+b
    
#wap to find 5th term in fibonacci serioes using iterative approach

def fib(n):
    a=0
    b=1
    if n<0: return print("Invalid Term")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        for p in range(2,n+1):
            c=a+b
            a=b
            b=c
        return b
f=fib(5) 
print(f)           