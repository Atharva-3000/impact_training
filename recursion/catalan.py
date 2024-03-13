# finding the nth catlan number using the recursive approach 
#catalan of n is given by: 2n!/((n+1)!*n!)

# def catlan(n):
#     if n<=1:
#         return 1
#     res=0
#     for p in range(n):
#         res=res+catlan(p)*catlan(n-p-1)
#         print(res, end=" ")
#     print()
#     return res

# print(catlan(5))

# print()
# print(catlan(8))
# print()
# print(catlan(10))

# DP APPROACH for catlan number
def catlan(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        for j in range(i):
            dp[i]+=dp[j]*dp[i-j-1]
    return dp[n]
print(catlan(4))

# j=0,1
# catalan[2]=catalan[2]+1*1=2
# catalan[2]=0+1=1
# j=1

# for n value 4 using dp approach
# j=0,1,2,3
# catalan[4]=catalan[4]+1*2=3
# catalan[4]=catalan[4]+2*1=5
# catalan[4]=catalan[4]+5*1=14

# catalan[4]=14