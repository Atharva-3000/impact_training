class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if(self.head==None):
            return True
        else: 
            return False
    def push(self,data):
        if(self.head==None):
            self.head=Node(data)
        else:
            temp=self.head
            if(self.head is None):
                self.head=Node(data)
            else:
                temp=self.head
                ne=Node(data)
                self.head=ne
                ne.next=temp
    def display(self):
        temp=self.head
        if(self.head is None):
            print("Stack is empty")
            return

        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
    def pop(self):
        temp=self.head
        if(self.isempty()):
            print("Stack is empty ")
        else:
            self.head=temp.next
            temp.next=None 
            print("The deleted element is: ",temp.data)


s1=Stack()
s1.push(12)
s1.push(34)
s1.push(24)
s1.push(45)
s1.display() 
print() 
s1.pop()
s1.display()