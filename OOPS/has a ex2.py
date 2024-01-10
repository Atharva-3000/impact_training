#wap to create two classes one is student, other one is find result class create student object in main and pass it to find result class, make static method in find result class to find result of student by accessing prperties of student from the student object passsed to result class

class Student:
    def __init__(self, name, rollno, marks1, marks2, marks3):
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        
    def display(self):
        print("Name is:",self.name, "\nRoll No is:",self.rollno, "\nMarks are: " ,self.marks1, self.marks2, self.marks3)
class FindResult:
    def find(student):
        if (student.marks1+student.marks2+student.marks3)/3 > 35:
            print("Result is Pass")
        else:
            print("Result is Fail")
student = Student("Atharva", 1, 99,98,97)
student.display()
FindResult.find(student)