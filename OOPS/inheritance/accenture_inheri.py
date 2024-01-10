#wap with class name Cicle constructed by radius and two methods which will compute the area and the perimeter of the circle

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
c = Circle(5)
print(c.area())
print("{:.2f}".format(c.perimeter()))