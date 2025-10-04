# n = 4 
# k = 5
# N = [1,5,10,15,17]
# K = [5,20,10,15,25]
n = 3
k = 2
N = [1,2,3]
K = [2,4,3]

def max_sum_dp(n, k, N, K):
    dp = [0] * (n + 1)
    K.append(0)
    for i in range(0, n+1):
        dp[i] = K[i]  # Initialize with the value at index i
        for j in range(1, i):
            if N[i] - N[j] >= k:
                dp[i] = max(dp[i], dp[j] + K[i])
        print(dp)
    return max(dp)  # Return the maximum value in the dp table

result = max_sum_dp(n, k, N, K)
print(result)
