#wap to take 2 numbers and perform the addition in single line
#walrus operators
#print(((a:=int(input())) + (b:=int(input()))))

#conditional operators
#a,b=map(int,input("Enter the values of a and b separated by comma: ").split(","))
#print("a is max") if(a>b) else print("b is max")

#read 3 numbers and return max in just 2 lines 
a,b,c=map(int,input("Enter the values of a ,b and c separated by comma: ").split(","))
print("a,b and c are equal") if(a==b and b==c)  else print("a is max") if(a>b and a>c) else print("b is max") if (b>c and b>a) else print("c is max")
