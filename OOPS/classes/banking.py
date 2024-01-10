#wap to create a banking application with static, non-static and local variables, constructor and non static methods given:
#1 before withdrawing if bal<2000 dont perform the transaction
#2 before withdrawing check the balance properly(suff funds are aval or not)

class bank:
    def __init__(self):
        self.accno=int(input("Enter account number: "))
        self.name=input("Enter name: ")
        self.add = input("Enter your Address: ")
        self.balance=int(input("Enter balance: "))
    def display(self):
        print("Account Number: ",self.accno)
        print("Name: ",self.name)
        print("Address: ",self.add)
        print("Balance: ",self.balance)
    def check_bal(self):
        print("Balance: ",self.balance)
    def deposit(self):
        amt=int(input("Enter amount to deposit: "))
        self.balance+=amt
        print("Balance: ",self.balance)
    def withdraw(self):
        self.amt=int(input("Enter amount to withdraw: "))
        if(self.balance>2000 and self.amt<self.balance):
            print("Successfully withdrawed")
            self.balance-=self.amt
            print("Remaining Balance: ",self.balance)
        else:
            print("Insufficient Balance, first deposit money !")

b=bank()
b.display()
b.check_bal()
b.deposit()
b.withdraw()  

a=bank()
a.display()
a.check_bal()
a.deposit()
a.withdraw()         