# class x:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
# class y(x):
#     def __init__(self, a):
#         self.a=a
#         print(self.a*self.a)
#         super().__init__(10,5)
# y1=y(20)

class bx:
    def __init__(self,p):
        self.p=p
    def __add__(self, other):
        d=self.p+other.p
        return d
class by:
    def __init__(self,p):
        self.p=p
    def __str__(self):
        return str(self.p)
b1=bx(200)
b2=by(100)
print(b1+b2)