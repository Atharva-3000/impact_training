class x:
    def m1(self):
        print("in ml of x.")
class y:
    def m1(self):
        print("in ml of y.")
class z(x,y):
    def m2(self):
        print("in ml of z.")
z1=z()
z1.m1()