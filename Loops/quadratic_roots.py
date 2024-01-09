'''Write a program to find roots of quadratic equation'''
import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
if(d>=0):
    root1=(-b+(math.sqrt(d)))/2*a
    root2=(-b-(math.sqrt(d)))/2*a
    print("First root is: ",root1)
    print("Second root is: ",root2)
else:
    print("Roots dont exist. !")
