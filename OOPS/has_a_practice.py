#wap to implement 2 classes employee and test, now 
#  employee details are employee name, id and salary
# update the salary in the test class, then call display method
#create the object of employee class in main program and pass the object to any method defined in the test class

class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
    def display(self):
        print(self.name, self.id, self.salary)
class test: 
    def update(self):
        emp.salary = emp.salary + 1000
        emp.display()
        
emp=Employee("Atharva", 101, 1000000)
emp.display()
test.update(emp)