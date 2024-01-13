from abc import *
class test(ABC):
    def operation(self):
        pass
class sub1(test):
    def operation(self,a):
        print(a*a)
class sub2(test):
    def operation(self,a):
        print(a**3)
class sub3(test):
    def operation(self,a ,b):
        print(a+b)
s1=sub1()
s1.operation(10)
s2=sub2()
s2.operation(5)
s3=sub3()
s3.operation(10,20)