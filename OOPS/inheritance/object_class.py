# class x:
#     def m1(self):
#         print("in m1...")
# x1=x()
# p=x1.__str__()
# print(p)
# x1.m1()


class x:
    def m1(self):
        print("in m1.")
class y(x):
    def m2(self):
        print("in m2.")
print(x.__bases__)
print(y.__bases__)
y1=y()
y1.m1()
y1.m2()
p=y1.__hash__()
print(p)