import sys

while True:
    n, m, k = sys.stdin.readline().split()
    if n == '#':
        break
    print(f'{n} Senior' if int(m) > 17 or int(k) >=80 else f"{n} Junior")