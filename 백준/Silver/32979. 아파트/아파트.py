import sys 

_ = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
queing = list(map(int, sys.stdin.readline().strip().split()))
count =  list(map(int, sys.stdin.readline().strip().split()))

num = 0

for i in range(n):
    num = num + count[i] - 1
    if num >= len(queing):
        num = num % len(queing)
    print(queing[num], end=" ")