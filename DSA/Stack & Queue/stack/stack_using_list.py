s=[]
size=int(input("Enter the size of stack: "))
top=-1
while(True):
    print("1.Push 2.Pop 3.Display 4.Exit")
    opt=int(input("Enter your option: "))
    if(opt==1):
        if(top==size-1):
            print("Stack is full")
        else:
            top+=1
            ele=int(input("Enter the element: "))
            s.append(ele)
    elif(opt==2):
        if(top==-1):
            print("Stack is empty")
        else:
            print("Deleted element is: ",s.pop())
            top-=1
    elif(opt==3):
        if(top==-1):
            print("Stack is empty")
        else:
            print("Stack elements are: ")
            print(*s)
    elif(opt==4):
        break
    else:
        print("Invalid option")