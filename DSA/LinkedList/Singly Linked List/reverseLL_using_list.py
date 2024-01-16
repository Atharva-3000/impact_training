#wap to reverse a linked list

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
    def reverse(self):
        list1=[]
        temp=self.head
        while(temp):
            list1.append(temp.data)
            temp=temp.next
        list1.reverse()
        for i in list1:
            print(i, end="-->")
n1=Node(30)
n2=Node(20)
n3=Node(10)
n1.next=n2
n2.next=n3
list1=slist()
list1.head=n1
list1.display()
print()
list1.reverse()                