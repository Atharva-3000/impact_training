print("Begin")
try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(a/b)
except(ValueError):
    print("Input should be int: ")
print("end")