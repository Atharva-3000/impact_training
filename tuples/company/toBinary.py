#convert to binary
n=int(input("Input encoded string: "))
t=[]
while(n):
    d=n%2
    t.append(d)
    n=n//2
t=t[::-1]
print("Binary form is: ")
for p in t:
    print(p,end='')