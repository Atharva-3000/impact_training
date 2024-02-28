#wap to add a node at the beginning

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
            print(temp.data, end="-->")
            temp=temp.next
    def add_begin(self,data):
        new_node=Node(data)
        temp=self.head
        self.head=new_node
        new_node.next=temp
        temp.prev=new_node
        
    def add_last(self,data):
        new_node=Node(data)
        temp=self.tail
        self.tail=new_node
        new_node.prev=temp
        temp.next=new_node
        
    def add_at_pos(self, pos, data):
        new_node = Node(data)
        temp = self.head
         
        if pos == 1:
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            return

        for i in range(pos - 2):
            if temp is None:
                print("Position is greater than the length of the list")
                return
            temp = temp.next

        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

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
dll.add_begin(5)
dll.display()
dll.add_last(50)
print()
dll.display()
print()
dll.add_at_pos(3,25)
dll.display()