#write a program to read name, roll no and 3 subject marks, if he is passed, calculate the grade of the student

name=input("Enter your name: ")
roll=int(input("Enter your roll no: "))
s1=int(input("Enter the marks of subject 1: "))
s2=int(input("Enter the marks of subject 2: "))
s3=int(input("Enter the marks of subject 3: "))
print("Details entered are :", "Name: ",name,"| Roll no: ",roll,"| Subject Marks: ",s1,s2,s3)
if(s1>=35 and s2>=35 and s3>=35):
    avg=(s1+s2+s3)/3
    if(avg>=60):
         print("Secured A")
    elif(avg>=50):
        print("Secured B")
    elif(avg>=35):
        print("Secured C")
else:
    print("Failed, grade is not possible !")
        
