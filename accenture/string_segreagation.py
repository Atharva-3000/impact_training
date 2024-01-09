#take string  input segregate it to get the age
num=int(input("Enter the number of strings you want: "))
n=list(map(str,input().split()))[:num]
# 1234567890M5253
# counter
c=0
for i in n:
    # age=i[-4:-1]
    age=int(i[11:13])
    if(age>=60):
        c=c+1
        print(i[0:10])
print(c)