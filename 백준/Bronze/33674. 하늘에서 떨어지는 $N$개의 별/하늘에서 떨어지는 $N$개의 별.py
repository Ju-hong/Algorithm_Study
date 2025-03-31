import math

_, d, k = map(int, input().split())
maxi = max(map(int, input().split()))

doom_cycle = k//maxi

print(math.ceil((d-doom_cycle)/doom_cycle))