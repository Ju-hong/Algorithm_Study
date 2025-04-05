import sys

arr = list(map(int, sys.stdin.readlines()))
print(len(set(i%42 for i in arr)))