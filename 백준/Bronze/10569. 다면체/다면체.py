import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(2-i+j)
    