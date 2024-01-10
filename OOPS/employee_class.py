#create employee class with basic emploee details like employee name, employee id, address and salary, create three objects, college name can be common or static

class employee:
    company_name="Parul University"
    def __init__(self, employee_name, employee_id, address, salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.address = address
        self.salary = salary
    def display(self):
        print("Company Name: ",employee.company_name,"\n","Employee Name: ", self.employee_name,"\n","Employee ID: ",self.employee_id, "\n","Address: ",self.address, "\n","Salary: ",self.salary)

N=int(input("Enter number of employees: "))
i=1
while(i<=N):
    employee_name=input("Enter Employee Name: ")
    employee_id=input("Enter Employee ID: ")
    address=input("Enter Address: ")
    salary=int(input("Enter Salary: "))
    e1=employee(employee_name, employee_id, address, salary)
    e1.display()
    print("***************************************************")
    i+=1