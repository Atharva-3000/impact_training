#wap to use properties of one class into another using has a relationship

class x:
    a=1000
    def __init__(self):
        self.b=2000
    def m1(self):
        print("in m1")
class y:
    c=3000
    def __init__(self):
        self.d=4000
    def m2():
        print("in m2")
    def display(self):
        print(y.c)
        print(self.d)
        y.m2()
        self.m2()
        x1=x()
        print(x1.a)
        print(x1.b)
        x1.m1()
y1=y()
y1.display()