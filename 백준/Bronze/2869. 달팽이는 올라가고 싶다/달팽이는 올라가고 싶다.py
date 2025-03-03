import math

n, m, k = map(int, input().split())

print(math.ceil((k-n)/(n-m)+1))