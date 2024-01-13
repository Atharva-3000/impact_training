from abc import *
class car(ABC):
    def __init__(self, regno):
        self.regno = regno
    def openTank(self):
        print("Fil the fuel tank with Reg no as",self.regno)
    def steering(self):
        pass
    def braking(self):
        pass
class Maruti(car):
    def steering(self):
        print("Maruti uses manual steering")
    def braking(self):
        print("Maruti uses hydraulic brakes")
class Santro(car):
    def steering(self):
        print("Santro uses power steering")
    def braking(self):
        print("Santro uses gas brakes")
class GTR(car):
    def steering(self):
        print("GTR uses e steering")
    def braking(self):
        print("GTR uses ceramic brakes")

m1 = Maruti("MH 12 AB 1234")
m1.openTank()
m1.steering()
m1.braking()
print()
s1 = Santro("MH 12 XY 1234")
s1.openTank()
s1.steering()
s1.braking()
print()
g1 = GTR("MH 12 CD 1234")
g1.openTank()
g1.steering()
g1.braking()