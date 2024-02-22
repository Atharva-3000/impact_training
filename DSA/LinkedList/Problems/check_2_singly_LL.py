#wap to check whether the 2 user inputted linked list are same or not

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next
        print()
        
def checkLL(head1, head2):
    while head1 is not None and head2 is not None:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    if head1 is None and head2 is None:
        return True
    return False

n1=Node(10)
n2=n1.next=Node(20)
n3=n2.next=Node(30)
n4=n3.next=Node(50)

m1=Node(10)
m2=m1.next=Node(20)
m3=m2.next=Node(30)
m4=m3.next=Node(40)
m5=m4.next=Node(50)

l1=sll()
l1.head=n1
l2=sll()
l2.head=m1
if(checkLL(l1.head, l2.head)):
    print("Both linked list are same")
    l1.display()
else:
    print("Both linked list are not same")