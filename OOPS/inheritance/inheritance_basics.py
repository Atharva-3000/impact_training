class x:
    a=1000
    def __init__(self):
        self.b=2000
    def m1(self):
        print("in m1.")
class y(x):
    c=3000
    def __init__(self):
        self.d=4000
        super().__init__()
    def m2(self):
        print("in m2.")
    def display(self):
        print(x.a)
        print(self.b)
        self.m1()
        print(y.c)
        self.m2()
        print(self.d)
y1=y()
y1.display()