a=10
def m1():
    print(a)
    # a=a+10    will throw error when updating the global variable via a function
    print(d)
m1()