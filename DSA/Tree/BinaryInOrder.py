class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
    def delete(self,key):
        if self.data is None:
            print("Empty Tree")
        elif key <self.data:
            if self.left:
                self.left=self.left.delete(key)
            else:
                print("node doesnot exist")
        elif key >self.data:
            if self.right:
                self.right=self.right.delete(key)
            else:
                print("node doesnot exist")  
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
                temp=self.right.minimum()
                self.data=temp.data
                self.right=self.right.delete(temp.data)
        return self

    def minimum(self):
        current =self
        while(current.left):
            current=current.left
        return current
    
    
    
def Inorder(root):
        if root:
            Inorder(root.left)
            print(root.data,end=' ')
            Inorder(root.right)
        
            

def PostOrder(root):
        if(root):
            PostOrder(root.left)
            PostOrder(root.right)
            print(root.data,end=" ")
            
            
            
def PreOrder(root):
    if(root):
        print(root.data,end=" ")
        PreOrder(root.left)
        PreOrder(root.right)
        
def search(root,key):
    if root==None:
        return False
    elif root.data==key:
        return True
    else:
        return  search(root.left,key) or search (root.right,key)
    
def height(root):
    if root is None:
        return 0
    left=height(root.left)
    right=height(root.right)
    d =max(left,right)    
    return d+1 

def sumNode(root):
    if root is None :
        return 0
    left=sumNode(root.left)
    right=sumNode(root.right)
    return left+right+root.data
#sumof left leaf 
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


#sum of rightleaf
def sumOfRLeaf(root,isRight,sum):
    if root is None:
        return 
    if root.left is None and root.right is None and isRight==True:
        sum[0]+=root.data
    sumOfRLeaf(root.left,0,sum)
    sumOfRLeaf(root.right,1,sum)
def sumOfLeafRecr(root):
    sum=[0]
    sumOfRLeaf(root,0,sum)
    return sum[0]
       
b=Node(27)
b.insert(14)
b.insert(35)
b.insert(10)
b.insert(19)
b.insert(31)
b.insert(42)
# b.insert(127)
# b.insert(256)
Inorder(b)
print()
# PostOrder(b)
# print()
# PreOrder(b) 
# print()
# print(search(b,10))
b.delete(27)
Inorder(b)
print()
print(height(b))

print(sumNode(b))
print(sumOfLeafRec(b))
print(sumOfLeafRecr(b))