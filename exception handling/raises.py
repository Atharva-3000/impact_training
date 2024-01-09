#after withdraw operation if the balance is less than 1500 rupees, raise the error

balance=4000
def withdraw(amount):
    global balance
    if(balance-amount<=1500):
        raise ValueError
    else:
        print(balance-amount)
try:
    amount=int(input("Enter amount: "))
    withdraw(amount)
except(ValueError):
    print("Maintain min balalnce of 1500 rupees.")
    print("Operation halted !")