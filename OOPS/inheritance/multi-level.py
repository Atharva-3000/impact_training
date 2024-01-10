class person:
    def insert(self):
        self.name="Atharva"
        self.add="Ratlam"
class employee(person):
        def insert1(self):
            self.id=259
class salaried_employee(employee):
    def __init__(self):
        self.sal=500000
    def display(self):
        self.insert()
        self.insert1()
        print(self.name,self.add,self.sal,self.id)
s1=salaried_employee()
s1.display()