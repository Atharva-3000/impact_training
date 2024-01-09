n=int(input("Enter the size of your input: "))
values = list(map(int, input("Enter the values you want to enter (separated by space):").split(" ")))[:n]
cycle=int(input("Enter cyclic number: "))
d=values[-cycle:]+values[:-cycle]
print(*d)  #IMPORTANT
