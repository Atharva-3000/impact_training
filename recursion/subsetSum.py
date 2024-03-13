# recurive solution for subset sum problem

def isSubsetSum(arr, n, sum):
    # base case
    if(sum==0):
        return True
    if(n==0):
        return False
    
    # if last element is greater than sum, then ignore it
    if(arr[n-1]>sum):
        return isSubsetSum(arr, n-1, sum)
    
    # else check if sum can be obtained by any of the following
    # a) including the last element
    # b) excluding the last element
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])

# driver code
arr=[3, 34, 4, 12, 5, 2]
sum=9
n=len(arr)
if(isSubsetSum(arr, n, sum)==True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")


# with dynamic programming
def isSubsetSum(arr, n, sum):
    # The value of subset[i][j] will be True if there is a subset of set[0..j-1]
    # with sum equal to i
    subset=[[False for i in range(sum+1)] for i in range(n+1)]
    
    # if sum is 0, then answer is True
    for i in range(n+1):
        subset[i][0]=True
    
    # if sum is not 0 and set is empty, then answer is False
    for i in range(1, sum+1):
        subset[0][i]=False
    
    # fill the subset table in bottom up manner
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if(j<arr[i-1]):
                subset[i][j]=subset[i-1][j]
            if(j>=arr[i-1]):
                subset[i][j]=subset[i-1][j] or subset[i-1][j-arr[i-1]]
    
    return subset[n][sum]

# driver code
arr=[3, 34, 4, 12, 5, 2]
sum=9
n=len(arr)
if(isSubsetSum(arr, n, sum)==True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
