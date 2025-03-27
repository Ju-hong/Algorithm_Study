import sys
def dp_increasing(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

def dp_decreasing(arr):
    n = len(arr)
    dp = [1 for _ in range(n)]
    arr = arr[::-1]

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

temp =[]

for j in range(n):
    increasing_len_arr = dp_increasing(arr[:j+1]) #아악 +!
    decreasing_len_arr = dp_decreasing(arr[j:])
    a = max(increasing_len_arr) + max(decreasing_len_arr) -1
    temp.append(a)
    

print(max(temp))