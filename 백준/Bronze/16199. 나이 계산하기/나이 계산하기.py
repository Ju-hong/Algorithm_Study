a, b, c = map(int, input().split())
d, e, f = map(int, input().split())

print(((d-a)*365+ (e-b)*30 + (f-c))//365)  
print(d-a+1)
print(d-a)