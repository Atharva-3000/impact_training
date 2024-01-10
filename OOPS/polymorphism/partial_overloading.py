class x:
    def m1(self):
        print("In m1 with no para")
    def m1(self, a):
        print("In m1 with one para")
    def m1(self, a, b):
        print("In m1 with two para")
x1=x()
x1.m1(10,20)