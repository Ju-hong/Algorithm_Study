n, m = map(int, input().split())
list_i = list(map(int, input().split()))

for i in list_i:
    print(i - n*m)