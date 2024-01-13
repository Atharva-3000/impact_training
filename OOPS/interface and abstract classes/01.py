#write an interface class called Vehicle with two bike and car with abstract methods in vehicle class and 2 methods in both bike and car called braking and steering

from abc import *
class Vehicle(ABC):
    def __init__(self,regno):
        self.regno=regno
    def braking(self):
        pass
    def steering(self):
        pass
class Bike(Vehicle):
    def braking(self):
        print("bike braking")
    def steering(self):
        print("bike Handle")
class Car(Vehicle):
    def braking(self):
        print("car braking")
    def steering(self):
        print("car steering")
b=Bike(1234)
b.braking()
b.steering()
c=Car(5678)
c.braking()
c.steering()