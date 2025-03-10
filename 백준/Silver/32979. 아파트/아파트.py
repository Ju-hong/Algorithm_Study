import sys
from collections import deque

_ = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
queing = deque(map(int, sys.stdin.readline().strip().split()))
count =  list(map(int, sys.stdin.readline().strip().split()))

for i in range(n):
    queing.rotate(-(count[i])+1)
    print(queing[0], end=" ")