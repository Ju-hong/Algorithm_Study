import sys

while True:
    result = sum(map(int, sys.stdin.readline().split()))
    if result == 0:
        break
    print(result)