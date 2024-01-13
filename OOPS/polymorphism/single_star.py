# def d(*a):
#     print(a)
#     print(type(a))
#     print(sum(a))
# d(10,20,30)
# d(1,2,3,4,5)

def d(b, *a):
    print(a)
    print(b)
    print(sum(a)+b)
d(10,20,30)
d(1,2,3,4,5)