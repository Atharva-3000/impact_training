#wap to find factorial of a number using recursion.
def f(n):
    if n==0:
        return 1
    else:
        d=n*f(n-1)
    return d
s=f(5)
print(s)

#wap to find sum 1 to 5
def sum(n):
    s=0
    if(n==0):
        return 1
    else:
       return n+sum(n-1)
print(sum(7))