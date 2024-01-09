# def even(n):
#     return n%2==0
# l=list(range(10,31))
# n=list(filter(even,l))
# print(n)

# #with lambda with filter
# l=list(range(10,31))
# r=list(filter(lambda x: x%2==0,1))
# print(r)
def pos(i):
    if(i>=0):
        return i

l=list(range(-6,5))
r=list(filter(pos,l))
print(r)