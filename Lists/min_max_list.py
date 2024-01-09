'''WAP to read n values separated with "," and find the largest and smallest one among it'''
values =list(map(int,input("Enter your values (separated by comma): ").split(",")))
'''print(min(values), max(values))'''
first=-1
second=-1
for i in values:
    if(i>first):
        second=first
        first=i
    elif (i>second and i<first):
        second=i
print(second)
