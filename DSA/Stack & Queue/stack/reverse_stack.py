# from collections import deque
# s=deque()
# q=deque()
# s.append(10)
# s.append(20)
# s.append(30)
# s.append(40)
# print(*s)
# while len(s)>0:
#     q.append(s.pop())
# print("Reversed stack is: ")
# print(*q)


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
        print(*self.stack2)
        
p1=stack()
p1.push(10)
p1.push(20)
p1.push(30)
p1.push(40)

p1.display()
print()
p1.rev()