import math

n, d, k = map(int, input().split())
arr = list(map(int, input().split()))

doom_cycle = k//max(arr)

print(math.ceil((d-doom_cycle)/doom_cycle))