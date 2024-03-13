a=int(input("Speed of the first car: "))
b=int(input("Speed of the second car: "))
d=int(input("Distance between the two cars: "))
n1=0
n2=0
c=0
while (n1>n2):
    if(a>b):
        c=-1
        break
    else:
        n1+=a
        n2+=b
        c+=1
print(c)