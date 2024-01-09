print("Begin")
try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(a/b)
except(ValueError):
    print("Input should be int!")
except(ZeroDivisionError):
    print("Second input should not be zero!")
finally:
    print("Yeah, finally always works!")
print("Ending...")