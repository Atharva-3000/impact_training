#read 2 give max
a,b =map(int,input("Enter a,b : ").split(","))
#print(a,b)
print(max(a,b))
if(a>b):
    print("Max is a: ",a)
else:
    print("Max is b: ",b)
