#reverse the user odefined string and check wheether palindrome or not
n=input()
r=''
i=len(n)
for p in range(len(n)-1,-1,-1):
    r=r+n[p]
if(r==n):
    print("Palindrome")
else:
    print("not Palindrome")