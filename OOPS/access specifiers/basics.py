class employee:
    __cname="Parul"  #private
    def __init__(self, name, idd, sal, dep):
        self.name = name
        self._idd = idd  #protected
        self._sal = sal  #protected
        self.dep = dep
    # PUBLIC  
    def __display(self):   #private
        # print(self.name, self.idd, self.sal, self.dep)
        print("Name: ", self.name)
        print("ID: ", self._idd)
    def display(self):
        self.__display()
class geeks(employee):
    def __init__(self, name, idd, sal, dep):
        super().__init__(name, idd, sal, dep)
    def display(self):
        self._display()
        print("Salary: ", self._sal)
        print("Department: ", self.dep)    
        
# e1=employee("Atharva",259,500000,"CSE")
e1=employee("Atharva",259,500000,"CSE")
print(e1._idd)
# print(e1.__display()) won't work
e1.display()