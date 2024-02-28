#wap to read number from a user and check whether it is divisible and 5 or not
n=int(input("Enter your number: "))
if(n%3==0):
    if(n%5==0):
        print("Divisible by both 3 and 5")
    else:
        print("Divisible by only 3")
else:
    if(n%5==0):
        print("Divisible by only 5")
    else:
        print("Not divisible by any.")