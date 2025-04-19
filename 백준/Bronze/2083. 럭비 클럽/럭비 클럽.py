import sys

while True:
    n, m, k = sys.stdin.readline().split()
    if n == '#':
        break
    if int(m) > 17 or int(k) >=80:
        print(n, 'Senior')
    else:
        print(n, 'Junior')
        