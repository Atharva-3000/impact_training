# class x:
#     def m1(self):
#         print("in m1 of x")
#     def m2(self):
#         print("in m2 of x")
# class y(x):
#     def m2(self):
#         print("in m2 of y")
#         # super().m2()
#     def m3(self):
#         print("in m3 of y")
# class z(x):
#     def m1(self):
#         print("in m1 of z")
#     def m4(self):
#         print("in m4 of z")
# y1=y()
# y1.m2()
# y1.m1()
# y1.m3()

# class test:
#     def m8(self):
#         print("in m1 of test")
#     def __str__(self):
#         return "Python"
# x1=test()
# p=x1.__str__()
# print(p)

class x:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return self.name
x1=x("Python")
print(x1)
x2=x("ABC")
print(x2)
x3=x("MEMC")
print(x3)