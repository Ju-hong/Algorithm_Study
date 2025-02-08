import sys

for i in range(int(input())):
    a = sys.stdin.readline().strip().split()
    print(f'Case #{i+1}: {' '.join(a[::-1])}')