# def _lis(arr,n):
#     global maximum
    
#     # base case
#     if(n==1):
#         return 1
#     maxEndingHere=1
#     for i in range(1,n):
#         res=_lis(arr,i)
#         if(arr[i-1]<arr[n-1] and res+1>maxEndingHere):
#             maxEndingHere=res+1
#     maximum=max(maximum, maxEndingHere)
#     return maxEndingHere


# def lis(arr):
#     global maximum
#     n=len(arr)
#     maximum=1
#     _lis(arr,n);
#     return maximum


# if __name__=="__main__":
#     arr=[10,22,9,33,21,50,41,60]
#     n=len(arr)
#     print("Length of lis is ", lis(arr))


# def lis(arr):
#     n = len(arr)
#     maximum = 1  # Initialize maximum length

#     # Function to find LIS ending at index i
#     def _lis(arr, i, current_max):
#         if i == n:
#             return current_max

#         # Explore possible subsequences
#         res = _lis(arr, i + 1, current_max)

#         # Update current_max if possible
#         if arr[i] < arr[i + 1]:  # Check for increasing order
#             current_max = max(current_max, res + 1)

#         return current_max

#     return _lis(arr, 0, maximum)  # Start at index 0, initialize with maximum

# # Example usage
# if __name__ == "__main__":
#     arr = [10, 22, 9, 33, 21, 50, 41, 60]
#     print("Length of lis is", lis(arr))



# using DYNAIMC PROGRAMMING
def largest_increasing_subsequence(arr):
    n = len(arr)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = 0

    return dp[n - 1][n - 1]

if __name__ == "__main__":
    arr = [3, 2, 1, 4, 5, 6]
    print("Length of lis is", largest_increasing_subsequence(arr))