import sys

for _ in range(3):
    n = int(sys.stdin.readline().rstrip())
    sum_i = sum(int(sys.stdin.readline()) for _ in range(n))
    if sum_i == 0:
        print(0)
    elif sum_i > 0:
        print("+")
    else:
        print("-")