#wap to create employee class with e name, e id and e salary and initialise the properties through a constructor and return the values back to main program without using any non static or static methods

class Employee:
    def __init__(self):
        self.name =input("Enter your name: ")
        self.id = input("Enter your id: ")
        self.salary = int(input("Enter your salary: "))
    def __str__(self):
        d=self.name+" "+self.id+" "+str(self.salary)
        return d
t1 = Employee()
print(t1)