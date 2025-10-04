# Open the file
fi = open('bai2.inp')

# Read the first line, split it, and convert the first element to an integer
n = int(fi.readline().split()[0])

# Initialize empty lists for A and B
A = [0]
B = [0]

# Read the remaining lines, split them into integers, and append them to A and B
for i in range(n):
    a, b = map(int, fi.readline().split())
    A.append(a)
    B.append(b)

# Print A for verification (optional)
# print(A)

# Initialize the dp array with n + 1 elements (from 0 to n)
dp = [0] * (n + 1)

# Set the base case for dp[n]
dp[n] = A[n]  # Assuming A[n] is valid based on your logic

# Calculate minimum costs using a loop from n-1 to 1 (inclusive)
for i in range(n - 1, 0, -1):
    dp[i] = min(dp[i + 1] + A[i], dp[i + 2] + B[i])

# Print the minimum cost at dp[1]
print(dp[1])

# Close the file
fi.close()
