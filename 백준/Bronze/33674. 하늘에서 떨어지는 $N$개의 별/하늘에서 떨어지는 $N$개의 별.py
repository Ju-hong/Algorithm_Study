import math

_, d, k = map(int, input().split())

maxi = max(map(int, input().split()))

print(math.ceil((d-k//maxi)/(k//maxi)))