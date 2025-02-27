import sys

plate = [[0]*100 for _ in range(100)]#list의 곱은 합처럼(당연함 곱이 합임)

num = int(sys.stdin.readline().strip())

for _ in range(num):
    a, b = map(int, sys.stdin.readline().strip().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            plate[i][j] = 1 

print(sum(sum(row) for row in plate))