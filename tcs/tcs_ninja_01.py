s=input("Enter the string: ")
s=s.lower()
r=''
for p in range(97,123):
    d=chr(p)
    if d not in s:
        r=r+d
print(r)
