# n=int(input())
# s=set(map(int, input().split()))
# m=int(input())
# t=set(map(int, input().split()))
# ans=[]
# ans.append(s ^ t)
# sorted(ans)
# # print(ans)
# for i in ans:
#     print(*i, end="\n")

n = int(input())
s = set(map(int, input().split()))
m = int(input())
t = set(map(int, input().split()))

# Find the symmetric difference and convert it to a sorted list
ans = sorted(list(s ^ t))

# Print each number in a new line
for num in ans:
    print(num)
