
n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [1]*n

for i in range(1, n):  # temp[2]
    for j in range(0, i): # temp[0], temp[1]
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

max_i = max(dp)
print(max(dp))

result = []

for i in range(n-1, -1, -1):
    if dp[i] == max_i :
        result.append(arr[i])
        max_i -= 1


print(*sorted(result))