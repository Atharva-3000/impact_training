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
            
           
a=stack()
a.push(10)
a.push(20)
a.push(30)
a.push(40)
b=stack()
b.push(10)
b.push(20)
b.push(30)
b.push(40)
b.push(50)

c=stack()

c.push(10)
c.push(20)