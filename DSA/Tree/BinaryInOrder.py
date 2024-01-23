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
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data,end=' ')
        print_tree(root.right)
        
def preorder(root):
    if root:
        print(root.data,end="")
        preorder(root.left)   
        print(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)   
        print(root.data,end=' ')
b=Node(27)
b.insert(14 )
b.insert(32 )
b.insert(48 )
print_tree(b)
print()
preorder(b)
print()
postorder(b)