n=input("Enter the number: ")
ans=""
for i in n:
    d=int(i)
    if(d%2!=0):
        ans+=str(d**2)
print(ans)
