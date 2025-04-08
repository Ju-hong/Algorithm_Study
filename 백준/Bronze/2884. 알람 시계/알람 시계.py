n, m = map(int, input().split())

if m-45 < 0 : 
    n -= 1
    m += 15
    
    if n < 0:
        n += 24
else:
    m -= 45
    
print(n, m)