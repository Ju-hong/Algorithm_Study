import sys 

k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
n, m = map(int, sys.stdin.readline().split())

shirt_count = 0

for i in arr:
    shirt_count += (i-1)//n + 1

print(shirt_count)
print(k//m, k%m)