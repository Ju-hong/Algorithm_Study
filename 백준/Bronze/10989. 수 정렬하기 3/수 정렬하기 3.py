import sys

n = int(sys.stdin.readline().strip())

temp = [0]*10001

for _ in range(n): # [0, 2, 2, 2, 1, 2, 0, 1, 
    temp[int(sys.stdin.readline().strip())] += 1

for i in range(len(temp)):
    if temp[i] != 0:
        for _ in range(temp[i]):
            print(i)