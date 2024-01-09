#givrn a lost of number, write an algo to remove all the duplicate numbers from the list without converting it into set.
li=list(map(int,input().split()))
ans=[]
for i in li:
    if(i not in ans):
        ans.append(i)
print(*ans)