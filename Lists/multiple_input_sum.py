'''Read  a program to read n values at a time and print it's sum'''
values = list(map(int, input("Enter the values you want to enter (separated by space):").split()))
print("Entered values:", values)
print("Sum:", sum(values))
