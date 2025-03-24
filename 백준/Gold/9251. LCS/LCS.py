import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

len_a = len(a)+1
len_b = len(b)+1

dp = [[0 for _ in range(len_a)] for _ in range(len_b)]


for j in range(1, len_b):
    for i in range(1, len_a):
        if a[i-1] == b[j-1]:
            dp[j][i] = dp[j - 1][i - 1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

        
print(max(dp[-1]))