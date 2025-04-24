def facto(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n, k = map(int, input().split())

print(int(facto(n)/(facto(n-k))/facto(k)))