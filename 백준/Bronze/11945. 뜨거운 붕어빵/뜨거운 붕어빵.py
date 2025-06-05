import sys

n, m = map(int, sys.stdin.readline().split())
temp = [sys.stdin.readline().rstrip() for _ in range(n)]

for i in range(n):
    print(temp[i][::-1])