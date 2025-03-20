import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))
maxi = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = arr[i] + arr[j] + arr[k]
            if a <= m:
                maxi.append(a)
print(max(maxi))