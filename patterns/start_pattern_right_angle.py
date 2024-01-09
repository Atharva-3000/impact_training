'''Write a program to print a stars of right angled triangle'''
'''
n = int(input("Enter the height of the Star: "));
for i in range (0,n):
    for j in range (0,i+1):
        print("*",end=" ")
    print()
'''


'''Write a program to print a stars of right angled triangle but opposite'''
'''
for i in range(n,-1,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

'''
'''Write a program to print a stars of right angled triangle but opposite angle'''
'''
for i in range(1,n):
    print((n-i)*" ",end=" ")
    print(i*"*")


list1=[1,2,3,4,5,6,7]
ansList=[]
for i in range (0,len(list1)):
    if(list1[i]%2==0):
        ansList.append(list1[i])
print(ansList)
'''
'''write a program to take the sides of a triangle as an input and check whether is is right angled or not'''
'''
a=int(input("Enter the height of the triangle: "))
b=int(input("Enter the width of the triangle: "))
c=int(input("Enter the hypotenuse of the triangle: "))

if((c*c)==((a*a)+(b*b))):
    print("It is a right angled triangle !")
else:
    print("It is NOT a right angled triangle")
'''
'''write a program to get the h and b of a triangle and get are'''
a=int(input("Enter the Height of the triangle: "))
b=int(input("Enter the Width of the triangle: "))
print(a*b*0.5)

