#wap to calculate depth and height of a binary search tree

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if self.data:
            if(data<self.data):
                if(self.left is None):
                    self.left=Node(data)
                else:
                    self.left.insert(data)
                       
            else:
                if(self.right is None):
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    def delete(self, key):
        if self.data is None:
            print("Tree is empty")
        elif key<self.data:
            if(self.left):
                self.left=self.left.delete(key)
            else:
                print("Node doesnt exist...")
        elif key>self.data:
            if(self.right):
                self.right=self.right.delete(key)
            else:
                print("Node doesn't exist.")
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            elif self.right is None:
                temp=self.left
                self=None
                return temp
            else:
                temp = self.right.minimum()
                self.data=temp.data
                self.right=self.right.delete(temp.data)
        return self
    def minimum(self):
        current=self
        while(current.left is not None):
            current=current.left
        return current
     