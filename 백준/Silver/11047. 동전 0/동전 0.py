import sys

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n) ]
arr.reverse()

result = 0

for i in arr:
    result += m//i
    m = m % i

print(result)