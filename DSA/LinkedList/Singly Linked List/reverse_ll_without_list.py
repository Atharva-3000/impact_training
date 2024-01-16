#wap to reverse a linked list without using list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class slist:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        if (temp is None):
            print("Linked List is empty")
        else:
            while(temp):
                print(temp.data, end="-->")
                temp = temp.next
    def reverseWithoutList(self):
        prev=None
        curr=self.head
        while(curr is not None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
n1=Node(30)
n2=Node(20)
n3=Node(10)
n1.next=n2
n2.next=n3
list1=slist()
list1.head=n1
list1.display()
list1.reverseWithoutList()
print()
list1.display()