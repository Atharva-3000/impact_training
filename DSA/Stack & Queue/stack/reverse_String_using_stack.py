class stack:
    def __init__(self):
        self.stack=[]
        self.stack2=[]
    def push(self,data):
        self.stack.append(data)
    def display(self):
        print(self.stack)
    def rev(self):
        while self.stack:
            self.stack2.append(self.stack.pop())
        print("Reversed stack is: ")
        for i in self.stack2:
            print(i,end="" )
        
s=input("Enter the string: ")
p1=stack()
for i in s:
    p1.push(i)
print()
p1.rev()