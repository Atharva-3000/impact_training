# function without args, without return
# def even_odd():
#     n=int(input("Enter your number: "))
#     if(n%2==0):
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# # even_odd()
# d=even_odd
# d()

# function with args and without return
# def even_odd(n):
#     if(n%2==0):
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# # even_odd()
# d=even_odd
# d(4)

# function with args and with return
# def even_odd(n):
#     if(n%2==0):
#         return "even"
#     else:
#         return "odd"
# n=int(input("Enter the number: "))
# e=even_odd(n)
# if(e=="even"):
#     print(n,"is even.")
# else:
#     print(n,"is odd.")
    
def even_odd(n):
    if(n%2==0):
        return 1
    else:
        return 0
    
    
n=int(input("Enter the number: "))
e=even_odd(n)
if(e):
    print(n,"is even.")
else:
    print(n,"is odd.")