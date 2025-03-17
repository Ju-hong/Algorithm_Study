import sys
n = int(sys.stdin.readline().strip())

temp = list(map(int, sys.stdin.readline().strip().split()))

dp = [1]*n


for i in range(1, n): # temp[2]
    for j in range(0, i): # temp[0], temp[1]
        if temp[j] < temp[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
    