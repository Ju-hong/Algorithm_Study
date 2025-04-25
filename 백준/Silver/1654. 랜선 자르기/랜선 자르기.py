import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readlines()))
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    count = sum(map(lambda x: x//mid, arr))
    if m <= count:
        start = mid + 1
    else:
        end = mid - 1

print(end)