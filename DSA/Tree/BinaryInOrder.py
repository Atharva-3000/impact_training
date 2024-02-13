class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if(self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if(self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
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
    
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data, end=" ")
        print_tree(root.right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
def search(root, key):
    if root == None:
        return False
    elif root.data == key:
        return key
    s1 = search(root.left, key)
    if s1:
        return True
    s2 = search(root.right, key)
    if s2:
        return True
def depth(root):
    if root is None:
        return 0
    ldepth = depth(root.left)
    rdepth = depth(root.right)
    if(ldepth>rdepth):
        return ldepth+1
    else:
        return rdepth+1
    
def sumOfLeaf(root,isLeft,sum):
    if root is None:
        return 
    if root.left is None and root.right is None and isLeft ==True:
        sum[0]+=root.data
    sumOfLeaf(root.left,1,sum)
    sumOfLeaf(root.right,0,sum)
    
def sumOfLeafRec(root):
    sum=[0]
    sumOfLeaf(root,0,sum)
    return sum[0]

b = Node(27)
b.insert(14)
b.insert(35)
b.insert(10)
b.insert(19)
b.insert(31)
b.insert(42)
print_tree(b)
print()
preorder(b)
print()
postorder(b)
print()
if search(b, 42):
    print("Found")
else:
    print("Not Found")
b.delete(42)
print_tree(b)
print()
print(depth(b))
print()
print(sumOfLeaf(b))