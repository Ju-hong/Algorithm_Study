import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, list(sys.stdin.readline() for _ in range(n))))
sorted_arr = sorted(arr, reverse = True)

result = []

for i in sorted_arr:
    temp = m//i
    result.append(temp)
    m -= temp*i

print(sum(result))