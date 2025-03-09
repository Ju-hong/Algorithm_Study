import sys
k = int(sys.stdin.readline().strip())

for _ in range(k):
    h, _, n = map(int, sys.stdin.readline().strip().split())

    if not n%h: 
        i = h 
        j = n//h
 
    else:
        i = n%h
        j = n//h+1
        
    print(i*100+j)