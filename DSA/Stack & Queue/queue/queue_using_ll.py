class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=None
        
        self.c=4
    def isempty(self):
        if(self.head==None):
            return True
        else: 
            return False
    def push(self,data):
        if(self.head==None):
            self.head=Node(data)
            self.c=self.c+1
        else:
            temp=self.head
            if(self.head is None):
                self.head=Node(data)
                self.c=self.c+1
            else:
                temp=self.head
                ne=Node(data)
                self.c=self.c+1
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
        if(self.c==0):
            print("Stack is empty ")
        else:
            prev=self.head
            temp=self.head.next
            while(temp.next):
                temp=temp.next
                prev=prev.next
            prev.next=None
            print("Deleted element is: ",temp.data)
    def isfull(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        if(count==self.c):
            return True
        else:
            return False
s1=Stack()
s1.push(12)
s1.push(34)
s1.push(24)
s1.push(45)
s1.display() 
print() 
s1.pop()
s1.display()
print()
print(s1.isfull())
s1.push(45)
print(s1.isfull())