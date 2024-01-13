#employee class will take name and sal
# and attendance class will be passed name and days
#return o/p:sal*days
#can use magic methods
class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def __mul__(self,other):
        return self.sal*other.days
    
class attendance:
    def __init__(self,name,days):
        self.name=name
        self.days=days 
a1=employee("ram",20)
a2=attendance("shyam",25)
print(a1*a2)