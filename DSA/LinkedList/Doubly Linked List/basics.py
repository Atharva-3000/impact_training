class Node:
    def __init__(self,data):
        self.prev=None
        self.next=None
        self.data=data
class DoublyLinkdeList:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
head=n1
tail=n4
dll=DoublyLinkdeList()
dll.head=head
dll.tail=tail
dll.display()