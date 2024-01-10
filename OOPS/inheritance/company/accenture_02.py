class Parent:
    def add(self):
        self.a = int(input("Enter a: "))
        self.b = int(input("Enter b: "))
        print("Sum is: ", self.a + self.b)
class Child(Parent):
    def sub(self):
        self.add()
        print("Sub is: ", self.a - self.b)
c1 = Child()
c1.sub()