#wap to find area of a rectangle
import math
class area:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def rect(self):
        print("Area is: ",l*b)
l=int(input("Enter Length: "))
b=int(input("Enter Breadth: "))
a=area(l,b)
a.rect()