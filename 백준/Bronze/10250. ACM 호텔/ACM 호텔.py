import sys
k = int(sys.stdin.readline().strip())

for _ in range(k):
    h, _, n = map(int, sys.stdin.readline().strip().split())
    if h == 1:
        i = str(1)
        j = str(n)

    
    elif not n%h: #나누어 떨어짐
        i = str(h)
        j = str(n//h)
 
    else:
        i = str(n%h)
        j = str(n//h+1)

    if len(j) == 1:
        j = str(0)+j
    print(i+j)