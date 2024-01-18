class  Node :
    def __init__(self,data):
        self.data=data
        self.next=None
        
class CircularLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def create(self):
        f=1
        while(f==1):
            d=int(input("enter the number to add in linked list"))
            n=Node(d)
            if(self.head is None):
                self.head=n
                self.tail=n
                n.next=self.head
            else:
                self.tail.next=n
                n.next=self.head
                self.tail=n
            f=int(input("enter the value 1 to take input again"))
            
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
                
                            
        
        
# n1=Node(10)
l1=CircularLL()
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
l1.display()
l1.reverse()
l1.display()