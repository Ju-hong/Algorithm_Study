import sys 

_ = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
n, m = map(int, sys.stdin.readline().split())

shirt_count = 0

for i in arr:
    if 1 <= i:
        shirt_count = shirt_count + (i-1)//n + 1

print(shirt_count)
print(sum(arr)//m, sum(arr)%m)