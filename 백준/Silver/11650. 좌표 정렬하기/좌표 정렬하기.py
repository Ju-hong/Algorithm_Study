import sys

n = int(sys.stdin.readline().strip())
temp = []

for _ in range(n):
    temp.append(list(map(int, sys.stdin.readline().strip().split())))


for i in sorted(temp):
    i = list(map(str, i))
    print(' '.join(i))