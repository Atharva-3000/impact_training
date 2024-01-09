# def power(p):
#     def pow(n):
#         return p**n
#     return pow
# # s=power(5)
# # p=s(4)
# # print(p)
# s=power(123)
# p=s(43)
# print(p)

def power(a):
    def pow(n):
        print (a*n)
    return pow
# s=power(5)
# p=s(4)
# print(p)
s=power('*')
p=s(43)