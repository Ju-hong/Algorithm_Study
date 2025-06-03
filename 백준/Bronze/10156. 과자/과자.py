n, m, k = map(int, input().split())
money = n*m
print( money-k if money > k else 0 )


