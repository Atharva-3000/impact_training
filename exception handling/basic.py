print("Begin")
a=int(input("Enter a: "))
try:
    b=int(input("Enter b: "))
    c=a/b
    print(c)
except(ZeroDivisionError):
    print("Second number cannnot be zero.")
print("End")