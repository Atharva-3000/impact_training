#wap to add a node at the beginning of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
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
    def add_node_at_beginning(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
n1=Node(30)
n2=Node(20)
n3=Node(10)
n1.next=n2
n2.next=n3
list1=slist()
list1.head=n1
list1.add_node_at_beginning(50)
list1.add_node_at_beginning(60)
list1.display()