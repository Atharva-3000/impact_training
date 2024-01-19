class  Node :
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLL:
    def __init__(self,size):
        self.head=None
        self.tail=None
        self.size=size
        
        
    def create(self):
        f=self.size
        print("You can enter ",f," nodes")
        while(f>0):
            d=int(input("enter the number to add in linked list: "))
            n=Node(d)
            if(self.head is None):
                self.head=n
                self.tail=n
                n.next=self.head
            else:
                self.tail.next=n
                n.next=self.head
                self.tail=n
            f-=1
            
    def reverse(self):
        prev,curr,nxt=self.tail,None,self.head
        while(nxt.next!=self.head):
            curr=nxt
            nxt=curr.next
            curr.next=prev
            prev=curr
            if(curr==self.head):
                break
        self.head=prev
                
            
    def display(self):
        if(self.head is None):
            print("empty")
        else:
            temp=self.head
            while(True):
                print(temp.data,end="-->")
                temp=temp.next
                if(temp==self.head):
                    break
            print(temp.data)
                
    def addAtBeg(self):
        d=int(input("enter the number to add at beginning: "))
        n=Node(d)
        n.next=self.head
        self.head=n
        self.tail.next=self.head
        self.size+=1
    def addAtEnd(self):
        d=int(input("enter the number to add at end: "))
        n=Node(d)
        self.tail.next=n
        n.next=self.head
        self.tail=n
        self.size+=1                   
    def addAtPosition(self):
        d=int(input("enter the number to add at position: "))
        n=Node(d)
        pos=int(input("enter the position"))
        temp=self.head
        for i in range(pos-2):
            temp=temp.next
        n.next=temp.next
        temp.next=n
        self.tail.next=self.head
        self.size+=1
    def del_beg(self):
        if(self.head is None):
            print("List is empty")
        else:
            temp=self.head
            self.head=temp.next
            self.tail.next=self.head
            self.size-=1
    def del_last(self):
        temp=self.head
        if(self.head is None):
            print("List is empty")
        else:
            while(temp.next!=self.tail):
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            self.size-=1
    def del_at_pos(self):
        pos=int(input("Enter the position to be deleted: "))
        prev=self.head
        temp=prev.next
        c=0
        while(c<pos-2):
            temp=temp.next
            prev=prev.next
            c+=1
            if(temp.next==self.head):
                print("Position out of range")
                break
        prev.next=temp.next
        del temp
        self.size-=1
                 
# n1=Node(10)
l1=CircularLL(5)
# l1.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# l1.tail=n4
# l1.tail.next=l1.head
l1.create()
# l1.addAtBeg()
# l1.addAtEnd()
# l1.display()
# l1.addAtPosition()
# l1.reverse()
# l1.del_beg()
# l1.del_last()
l1.del_at_pos()
l1.display()