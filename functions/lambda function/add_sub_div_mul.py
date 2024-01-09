#wap to perform addition subtraction, div and mul using single function and lambda
# def calc(a,b,s):
#     r=s(a,b)
#     return r
# s1=calc(10,20,lambda a,b:a+b)
# s2=calc(10,20,lambda a,b:a-b)
# print(s1)
# print(s2)


l=lambda a,b:[a+b,a-b,a*b,a/b]
x,y,z,r=l(10,20)
print(x,y,z,r)