# Result=[]
# scoreList=[]
# a = int(input("Enter the size: "))
# for i in range(0,a):
#     name=input("Enter name: ")
#     score=print("Enter the score: ")
#     lst=list(map(int,input().split()))[:3]
#     s=sum(lst)
#     scoreList.append(s)
#     Result+=[[name, s]]
# b=sorted(list(set(scoreList)))[1]
# for x,y in sorted(Result):
#     if(y==b):
#         print(a)

n=int(input())
d={}
for p in range(n):
    name,*m=input().split()
    # splitting it into 3 parts
    marks=list(map(int,m))
    d.update({name:marks})
print(d)
name=input("Enter the name: ")
m1=d[name]
avg=sum(m1)/len(m1)
print(avg)