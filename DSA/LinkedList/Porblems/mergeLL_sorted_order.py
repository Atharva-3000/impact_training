#given two sorted linked listm, merge them such that the resulting linked list is also sorted

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLL(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data < head2.data:
        head1.next = mergeLL(head1.next, head2)
        return head1
    else:
        head2.next = mergeLL(head1, head2.next)
        return head2

def printLL(head):
    while head is not None:
        print(str(head.data) + "->", end="")
        head = head.next
    print("None")
    return

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currData in inputList:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    
    return head

a=takeInput()
b=takeInput()
printLL(a)
printLL(b)
c=mergeLL(a,b)
printLL(c)