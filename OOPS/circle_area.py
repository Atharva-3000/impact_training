#wap to find area of a circle
import math
class area:
    def __init__(self,r):
        self.r=r
    def cicle(self):
        print("Area is: ",(math.pi*self.r**2))
radius=int(input("Enter radius: "))
a=area(radius)
a.cicle()