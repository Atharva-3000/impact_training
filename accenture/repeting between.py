#wap which prints all the numbers with non repeating digits between a given range (both inclusive)

def common_check(n):
    l=[]
    while(n):
        r=n%10
        if(r in l):
            return False
        l.append(r)
        n=n//10
    return True


n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
count=0

for i in range(n1,n2+1):
    d=common_check(i)
    if(d):
        count+=1
        print(i, end=" ")
print(count)