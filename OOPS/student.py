#wap to develop a student class with all contructor, static, non static and everything etc etc
# name, 3 sub marks, roll no and address
#input, display, result?pass:fail
class student:
    def __init__(self):
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll no: "))
        self.address = input("Enter address: ")
        self.sub1 = int(input("Enter marks of sub1: "))
        self.sub2 = int(input("Enter marks of sub2: "))
        self.sub3 = int(input("Enter marks of sub3: "))
    def display(self):
        print("Name: ",self.name)
        print("Roll no: ",self.roll)
        print("Address: ",self.address)
        print("Marks of sub1: ",self.sub1)
        print("Marks of sub2: ",self.sub2)
        print("Marks of sub3: ",self.sub3)
    def results(self):
        if(self.sub1>=40 and self.sub2>=40 and self.sub3>=40):
            print(self.name+" has Passed with the grade of ")
            grade=(self.sub1+self.sub2+self.sub3)/3
            if(grade>80):
                print("A")
            elif(grade>60):
                print("B")
            elif(grade>40):
                print("C")
            else:
                print("D/Just Pass")
        else:
            print(self.name+" has Failed")
s=student()
s.display()
s.results()