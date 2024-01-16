#wap to show deleting from front, from end and from a given position in a doubly linked list

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
    def add_begin(self, data):
        new_node = Node(data)

        if self.head is None:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        
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

    def delete_front(self):
        temp=self.head
        self.head=temp.next
        temp.next.prev=None
        temp=None
    def delete_end(self):
        temp=self.tail
        self.tail=temp.prev
        temp.prev.next=None
        temp=None
    def delete_at_pos(self,pos):
        temp=self.head
        if(pos==1):
            self.head=temp.next
            temp.next.prev=None
            temp=None
            return
        for i in range(pos-2):
            if(temp is None):
                print("Position is greater than the length of the list")
                return
            temp=temp.next
        temp.next=temp.next.next
        if(temp.next is not None):
            temp.next.prev=temp
        temp=None
m1=Node(10)
m2=Node(20)
m3=Node(30)
m4=Node(40)
m1.next=m2
m1.prev=None
m2.prev=m1
m2.next=m3
m3.prev=m2
m3.next=m4
m4.prev=m3
m4.next=None
head=m1
tail=m4
dll=DoublyLinkdeList()
dll.add_begin(10)
dll.add_begin(20)
dll.add_begin(30)
dll.add_begin(40)
dll.add_begin(50)
dll.display()
print()
dll.delete_front()
dll.display()
print()
dll.delete_end()
dll.display()
print()
dll.delete_at_pos(2)
dll.display()