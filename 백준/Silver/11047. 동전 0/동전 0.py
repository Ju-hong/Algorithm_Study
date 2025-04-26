import sys

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n) ]
arr.reverse()

result = []

for i in arr:
    temp = m//i
    result.append(temp)
    m -= temp*i

print(sum(result))