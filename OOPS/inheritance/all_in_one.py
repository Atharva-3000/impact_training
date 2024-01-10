# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Single inheritance
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Multilevel inheritance
class Bulldog(Dog):
    def guard(self):
        print(f"{self.name} is guarding.")

# Multiple inheritance
class Bird:
    def fly(self):
        print(f"{self.name} is flying.")

class Parrot(Bird, Animal):
    def talk(self):
        print(f"{self.name} is talking.")

# Hierarchical inheritance
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

# Creating objects
dog = Dog("Tommy")
dog.eat()
dog.sleep()
dog.bark()

bulldog = Bulldog("Spike")
bulldog.eat()
bulldog.sleep()
bulldog.bark()
bulldog.guard()

parrot = Parrot("Rio")
parrot.eat()
parrot.sleep()
parrot.fly()
parrot.talk()

cat = Cat("Whiskers")
cat.eat()
cat.sleep()
cat.meow()
