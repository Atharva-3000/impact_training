'''
f=0
f=1
f-f(n-2)+f(n-1)
f(2)=f(0)+f(1)
0+1=1
f(3)=f(1)+f(2)
1+1=2
'''

def fib(n):
    if n<=1:
        return n
    return fib(n-2)+fib(n-1)
print(fib(7))