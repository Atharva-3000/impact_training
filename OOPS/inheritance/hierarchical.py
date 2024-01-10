class student:
    def insert(self):
        self.name = input("Enter Name: ")
        self.roll = input("Enter Roll No: ")
        self.add = input("Enter Address: ")
class DS(student):
    def __init__(self):
        self.s1=int(input("Enter sub1: "))
        self.s2=int(input("Enter sub2: "))
    def display(self):
        self.insert()
        print(self.name,self.roll,self.add,self.s1,self.s2)
class ML(student):
    def __init__(self):
        self.s3=int(input("Enter sub1: "))
        self.s4=int(input("Enter sub2: "))
    def display(self):
        self.insert()
        print(self.name,self.roll,self.add,self.s3,self.s4,self.s3)
d1=DS()
d1.display()
m1=ML()
m1.display()
