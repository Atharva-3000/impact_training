#wap to delete the first node of a linked list

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class slist:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if(temp is None):
            print("Linked List is empty")
        else:
            while(temp):
                print(temp.data, end="-->")
                temp=temp.next
                
    def delete_first_node(self):
        temp=self.head
        self.head=temp.next
    def delete_last_node(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def delete_node_at_given_pos(self, pos):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        if pos == 1:
            self.head = temp.next
            return
        for i in range(1, pos - 1):
            if temp is None or temp.next is None:
                print("Position is greater than the length of the list")
                return
            temp = temp.next
        temp.next = temp.next.next
  

n1=Node(30)
n2=Node(20)
n3=Node(10)
n4=Node(40)
n5=Node(50)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
list1=slist()
list1.head=n1
list1.display()
list1.delete_first_node()
print()
list1.display()
list1.delete_last_node()
print()
list1.display()
list1.delete_node_at_given_pos(1)
print()
list1.display()